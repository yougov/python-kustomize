import importlib
import os
import sys
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass
class Resource:
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
        data = getattr(module, attr_name)

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
        with open(str(path), 'w') as f:
            yaml.safe_dump(self.data, f)

        return self.build_path


def generate(
        source_path: Path, dest_path: Path, attr_name: str = 'kustomization'):
    source_path = source_path.absolute()
    dest_path = dest_path.absolute()
    os.makedirs(str(dest_path), 0o755, exist_ok=True)

    prepended = False
    source_path_str = str(source_path)
    if source_path_str not in sys.path:
        sys.path.insert(0, source_path_str)
        prepended = True

    try:
        import pprint; pprint.pprint(sys.path)
        import kustomization as k_module

        importlib.reload(k_module)

        kustomization = deepcopy(getattr(k_module, attr_name))
        resources = [
            Resource.from_reference(string)
            for string in kustomization['resources']
        ]
        kustomization['resources'] = [
            str(resource.build(dest_path)) for resource in resources
        ]

        kustomization_path = dest_path / 'kustomization.yaml'

        with open(str(kustomization_path), 'w') as f:
            yaml.safe_dump(kustomization, f)
    finally:
        if prepended:
            sys.path.pop(0)