import attr


@attr.s(auto_attribs=True)
class Metadata:
    name: str


@attr.s(auto_attribs=True)
class ConfigMap:
    metadata: Metadata
    data: dict
    apiVersion: str = 'v1'
    kind: str = 'ConfigMap'


configMap = ConfigMap(
    metadata=Metadata(name='the-map'),
    data={'altGreeting': 'Good Morning!', 'enableRisky': 'false'},
)
