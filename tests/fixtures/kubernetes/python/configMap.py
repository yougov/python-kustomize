import datetime as dt


class Metadata:
    swagger_types = {
        'name': 'str',
        'labels': 'dict',
    }

    attribute_map = {
        'name': 'name',
        'labels': 'labels',
    }

    def __init__(self, name: str, labels: dict):
        self.name = name
        self.labels = labels

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'labels': self.labels,
        }


class ConfigMap:
    swagger_types = {
        'metadata': 'Metadata',
        'data': 'dict',
        'api_version': 'str',
        'kind': 'str',
    }

    attribute_map = {
        'metadata': 'metadata',
        'data': 'data',
        'api_version': 'apiVersion',
        'kind': 'kind',
    }

    def __init__(
            self, metadata: Metadata, data: dict,
            api_version: str = 'v1', kind: str = 'ConfigMap',
    ):
        self.metadata = metadata
        self.data = data
        self.api_version = api_version
        self.kind = kind

    def to_dict(self) -> dict:
        return {
            'metadata': self.metadata.to_dict(),
            'data': self.data,
            'api_version': self.api_version,
            'kind': self.kind,
        }


configMap = ConfigMap(
    metadata=Metadata(
        name='the-map',
        labels={
            'when': dt.datetime(2019, 1, 1),
            'ignore': None,
            'numbers': [1, 2],
            'others': (3, 4),
        }
    ),
    data={'altGreeting': 'Good Morning!', 'enableRisky': 'false'},
)
