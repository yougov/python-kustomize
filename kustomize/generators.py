import datetime as dt
import importlib
import os
import sys
from copy import deepcopy
from dataclasses import dataclass, is_dataclass, asdict
from pathlib import Path
from typing import Union

import yaml

SERIALIZABLE_TYPES = (float, bool, bytes, str, int, dt.date, dt.datetime)


@dataclass
class Extension:
    module_name: str
    attr_name: str
    data: dict

    @classmethod
    def from_reference(cls, string: str):
        parts = string.split(':')

        if len(parts) > 1:
            module_name = parts[0]
            attr_name = parts[1]
        else:
            module_name = parts[0]
            attr_name = module_name.split('.')[-1]

        module = importlib.__import__(module_name)
        importlib.reload(module)
        data = to_dict_or_dicts(getattr(module, attr_name))

        return cls(
            module_name=module_name,
            attr_name=attr_name,
            data=data,
        )

    @property
    def build_path(self) -> Path:
        path = Path(*self.module_name.split('.'))
        return path.with_suffix('.yaml')

    def build(self, dest_path: Path) -> Path:
        path = dest_path / self.build_path
        _dump_data(self.data, path)

        return self.build_path


def generate(
        source_path: Path, dest_path: Path, attr_name: str = 'kustomization'):
    source_path = source_path.absolute()
    dest_path = dest_path.absolute()

    for (dirpath, dirnames, filenames) in os.walk(str(source_path)):
        for dirname in dirnames:
            down_source_path = source_path / dirname
            down_dest_path = dest_path / dirname
            generate(down_source_path, down_dest_path, attr_name)

    _generate_for_source(source_path, dest_path, attr_name)


def _generate_for_source(source_path: Path, dest_path: Path, attr_name: str):
    if not (source_path / 'kustomization.py').is_file():
        return

    os.makedirs(str(dest_path), 0o755, exist_ok=True)
    prepended = False
    source_path_str = str(source_path)
    if source_path_str not in sys.path:
        sys.path.insert(0, source_path_str)
        prepended = True
    try:
        kustomization = _get_kustomization_data(attr_name, dest_path)
        kustomization_path = dest_path / 'kustomization.yaml'

        _dump_data(kustomization, kustomization_path)
    finally:
        if prepended:
            sys.path.pop(0)


def _dump_data(data, path):
    with open(str(path), 'w') as f:
        if isinstance(data, tuple):
            yaml.safe_dump_all(clean_data(data), f)
        else:
            yaml.safe_dump(clean_data(data), f)


def clean_data(data: Union[dict, list, tuple]):
    if isinstance(data, tuple):
        return tuple(clean_data(d) for d in data)
    if isinstance(data, list):
        return [clean_data(d) for d in data]
    if not isinstance(data, dict):
        return data
    for k in list(data.keys()):
        v = data[k]
        if v is None:
            del data[k]
        else:
            data[k] = clean_data(data[k])
    return data


def _get_kustomization_data(attr_name, dest_path):
    import kustomization as k_module

    importlib.reload(k_module)
    kustomization = to_dict_or_dicts(getattr(k_module, attr_name))

    extensions_names = (
        'resources',
        'patches',
        'patchesStrategicMerge',
    )

    for extension_name in extensions_names:
        if kustomization.get(extension_name) is None:
            continue
        extensions = [
            Extension.from_reference(string)
            for string in kustomization[extension_name]
        ]
        kustomization[extension_name] = [
            str(resource.build(dest_path)) for resource in extensions
        ]

    if kustomization.get('patchesJson6902') is not None:
        patches = kustomization['patchesJson6902']
        for patch in patches:
            extension = Extension.from_reference(patch['path'])
            patch['path'] = str(extension.build(dest_path))

    return kustomization


def is_attr_class(obj) -> bool:
    try:
        import attr
    except ImportError:  # pragma: no cover
        return False

    return attr.has(type(obj))


def _is_kubernetes(obj):
    return all(
        hasattr(obj, attr)
        for attr in ('to_dict', 'swagger_types', 'attribute_map')
    )


def _k8s_to_serializable(obj):
    """Transforms from Kubernetes model objects into dicts.

    Adapted and modified from the python-kubernetes library:
    https://github.com/kubernetes-client/python

    """

    if obj is None:
        return None
    elif isinstance(obj, SERIALIZABLE_TYPES):
        return obj
    elif isinstance(obj, list):
        return [_k8s_to_serializable(sub_obj) for sub_obj in obj]
    elif isinstance(obj, tuple):
        return tuple(_k8s_to_serializable(sub_obj) for sub_obj in obj)

    if isinstance(obj, dict):
        obj_dict = obj
    else:
        # Convert model obj to dict except
        # attributes `swagger_types`, `attribute_map`
        # and attributes which value is not None.
        # Convert attribute name to json key in
        # model definition for request.
        obj_dict = {
            obj.attribute_map[attr]: getattr(obj, attr)
            for attr, _ in obj.swagger_types.items()
            if getattr(obj, attr) is not None
        }

    return {key: _k8s_to_serializable(val) for key, val in obj_dict.items()}


def to_dict_or_dicts(obj):
    if isinstance(obj, tuple):
        return tuple(to_dict_or_dicts(o) for o in obj)
    if _is_kubernetes(obj):
        return _k8s_to_serializable(obj)
    if hasattr(obj, 'to_dict'):
        obj = obj.to_dict()
    elif is_dataclass(obj):
        obj = asdict(obj)
    elif is_attr_class(obj):
        import attr
        obj = attr.asdict(obj, recurse=True)
    elif hasattr(obj, '__dict__'):
        obj = obj.__dict__

    obj = deepcopy(obj)

    return obj
