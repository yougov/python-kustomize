from dataclasses import dataclass


@dataclass
class Metadata:
    name: str


@dataclass
class ConfigMap:
    metadata: Metadata
    data: dict
    apiVersion: str = 'v1'
    kind: str = 'ConfigMap'


configMap = ConfigMap(
    metadata=Metadata(name='the-map'),
    data={'altGreeting': 'Good Morning!', 'enableRisky': 'false'},
)
