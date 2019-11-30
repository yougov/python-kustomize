import importlib
import os
import sys
from copy import deepcopy
from dataclasses import dataclass
from pathlib import Path
from typing import Optional

import yaml


@dataclass
class Resource:
    module_name: str
    attr_name: str
    data: dict

    @classmethod
    def from_reference(cls, string: str):
        parts = string.split(':')

        module_name = parts[0]
        attr_name = parts[1]

        module = importlib.__import__(module_name)
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


def generate(source_path: Path, attr_name: str, dest_path: Path):
    source_path_str = str(source_path)
    if source_path_str not in sys.path:
        sys.path.insert(0, source_path_str)
    os.makedirs(str(dest_path), 0o755, exist_ok=True)

    import kustomization as k_module

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
