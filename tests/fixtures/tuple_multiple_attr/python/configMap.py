import attr


@attr.s(auto_attribs=True)
class ConfigMap:
    apiVersion: str
    kind: str
    metadata: dict
    data: dict


configMap = (
    ConfigMap(
        apiVersion='v1',
        kind='ConfigMap',
        metadata={'name': 'the-map'},
        data={'altGreeting': 'Good Morning!', 'enableRisky': 'false'},
    ),
    ConfigMap(
        apiVersion='v1',
        kind='ConfigMap',
        metadata={'name': 'another-map'},
        data={'altGreeting': 'Good Evening!', 'enableRisky': 'true'},
    ),
)
