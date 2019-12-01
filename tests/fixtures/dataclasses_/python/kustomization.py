from dataclasses import dataclass
from typing import List


@dataclass
class CommonLabels:
    app: str


@dataclass
class MyKustomization:
    commonLabels: CommonLabels
    resources: List[str]


kustomization = MyKustomization(
    commonLabels=CommonLabels(app='hello'),
    resources=[
        'deployment',
        'service',
        'configMap',
    ],
)
