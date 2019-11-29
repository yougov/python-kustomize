from dataclasses import dataclass, field

from kustomize.converters import to_dict


@dataclass
class SomeBaseManifest:
    apiVersion: str = 'apps/v1'
    metadata: dict = field(default_factory=dict)
    spec: dict = field(default_factory=dict)


class TestDictConverter:
    def test_converts_manifest_dataclass_to_dict(self):
        manifest = SomeBaseManifest(
            metadata={'foo': 'bar'},
            spec={'foo': 'baz'},
        )

        result = to_dict(manifest)

        assert result == {
            'apiVersion': 'apps/v1',
            'metadata': {'foo': 'bar'},
            'spec': {'foo': 'baz'},
        }
