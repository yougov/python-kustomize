class Metadata:
    name: str

    def __init__(self, name: str):
        self.name = name


class ConfigMap:
    metadata: dict
    data: dict
    apiVersion: str = 'v1'
    kind: str = 'ConfigMap'

    def __init__(
            self, metadata: Metadata, data: dict,
            apiVersion: str = 'v1', kind: str = 'ConfigMap',
    ):
        self.metadata = metadata.__dict__
        self.data = data
        self.apiVersion = apiVersion
        self.kind = kind


configMap = ConfigMap(
    metadata=Metadata(name='the-map'),
    data={'altGreeting': 'Good Morning!', 'enableRisky': 'false'},
)
