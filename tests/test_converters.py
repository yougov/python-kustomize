from dataclasses import dataclass, field

from kustomize.converters import to_dict


@dataclass
class SomeSimpleManifest:
    apiVersion: str = 'apps/v1'
    metadata: dict = field(default_factory=dict)
    spec: dict = field(default_factory=dict)


@dataclass
class Metadata:
    name: str


@dataclass
class Spec:
    replicas: int = 1


@dataclass
class SomeComplexManifest:
    kind: str
    metadata: Metadata
    spec: Spec
    apiVersion: str = 'apps/v1'


class TestDictConverter:
    def test_converts_simple_manifest_dataclass_to_dict(self):
        manifest = SomeSimpleManifest(
            metadata={'foo': 'bar'},
            spec={'foo': 'baz'},
        )

        result = to_dict(manifest)

        assert result == {
            'apiVersion': 'apps/v1',
            'metadata': {'foo': 'bar'},
            'spec': {'foo': 'baz'},
        }

    def test_converts_complex_manifest_dataclass_to_dict(self):
        manifest = SomeComplexManifest(
            kind='Deployment',
            metadata=Metadata(name='something'),
            spec=Spec(),
        )

        result = to_dict(manifest)

        assert result == {
            'kind': 'Deployment',
            'apiVersion': 'apps/v1',
            'metadata': {'name': 'something'},
            'spec': {'replicas': 1},
        }
