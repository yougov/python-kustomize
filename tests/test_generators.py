import yaml

from kustomize.generators import generate


def assert_yaml_equal(a, b):
    with open(a) as f:
        a_data = yaml.safe_load(f)
    with open(b) as f:
        b_data = yaml.safe_load(f)

    assert a_data == b_data


def test_generates_simple_dict(cd_fixtures, create_build_path):
    fixtures_path = cd_fixtures('simple_dict')
    build_path = create_build_path()
    python_path = fixtures_path / 'python'
    reference_path = fixtures_path / 'reference'

    generate(python_path, build_path, 'my_kustomization')

    assert_yaml_equal(
        build_path / 'kustomization.yaml',
        reference_path / 'kustomization.yaml',
    )
    assert_yaml_equal(
        build_path / 'deployment.yaml',
        reference_path / 'deployment.yaml',
    )
    assert_yaml_equal(
        build_path / 'configMap.yaml',
        reference_path / 'configMap.yaml',
    )
    assert_yaml_equal(
        build_path / 'service.yaml',
        reference_path / 'service.yaml',
    )


def test_generates_simple_dict_defaults(cd_fixtures, create_build_path):
    fixtures_path = cd_fixtures('simple_dict_defaults')
    build_path = create_build_path()
    python_path = fixtures_path / 'python'
    reference_path = fixtures_path / 'reference'

    generate(python_path, build_path)

    assert_yaml_equal(
        build_path / 'kustomization.yaml',
        reference_path / 'kustomization.yaml',
    )
    assert_yaml_equal(
        build_path / 'deployment.yaml',
        reference_path / 'deployment.yaml',
    )
    assert_yaml_equal(
        build_path / 'configMap.yaml',
        reference_path / 'configMap.yaml',
    )
    assert_yaml_equal(
        build_path / 'service.yaml',
        reference_path / 'service.yaml',
    )
