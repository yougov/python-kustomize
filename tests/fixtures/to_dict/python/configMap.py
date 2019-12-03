class Metadata:
    name: str

    def __init__(self, name: str):
        self.name = name

    def to_dict(self) -> dict:
        return {
            'name': self.name,
        }


class ConfigMap:
    metadata: Metadata
    data: dict
    apiVersion: str = 'v1'
    kind: str = 'ConfigMap'

    def __init__(
            self, metadata: Metadata, data: dict,
            apiVersion: str = 'v1', kind: str = 'ConfigMap',
    ):
        self.metadata = metadata
        self.data = data
        self.apiVersion = apiVersion
        self.kind = kind

    def to_dict(self) -> dict:
        return {
            'metadata': self.metadata.to_dict(),
            'data': self.data,
            'apiVersion': self.apiVersion,
            'kind': self.kind,
        }


configMap = ConfigMap(
    metadata=Metadata(name='the-map'),
    data={'altGreeting': 'Good Morning!', 'enableRisky': 'false'},
)
