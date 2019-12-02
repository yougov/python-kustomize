from kustomize.generators import generate
from tests.base import assert_yaml_dirs_equal


def test_generates_simple_dict(cd_fixtures, create_build_path):
    fixtures_path = cd_fixtures('simple_dict')
    build_path = create_build_path()
    python_path = fixtures_path / 'python'
    reference_path = fixtures_path / 'reference'

    generate(python_path, build_path, 'my_kustomization')

    assert_yaml_dirs_equal(build_path, reference_path)


def test_generates_simple_dict_defaults(cd_fixtures, create_build_path):
    fixtures_path = cd_fixtures('simple_dict_defaults')
    build_path = create_build_path()
    python_path = fixtures_path / 'python'
    reference_path = fixtures_path / 'reference'

    generate(python_path, build_path)

    assert_yaml_dirs_equal(build_path, reference_path)


def test_generates_dataclasses(cd_fixtures, create_build_path):
    fixtures_path = cd_fixtures('dataclasses_')
    build_path = create_build_path()
    python_path = fixtures_path / 'python'
    reference_path = fixtures_path / 'reference'

    generate(python_path, build_path)

    assert_yaml_dirs_equal(build_path, reference_path)


def test_generates_base_and_overlays(cd_fixtures, create_build_path):
    fixtures_path = cd_fixtures('base_and_overlays')
    build_path = create_build_path()
    python_path = fixtures_path / 'python'
    reference_path = fixtures_path / 'reference'

    generate(python_path, build_path)

    assert_yaml_dirs_equal(build_path, reference_path)


def test_generates_patchesJson6902(cd_fixtures, create_build_path):
    fixtures_path = cd_fixtures('patchesJson6902')
    build_path = create_build_path()
    python_path = fixtures_path / 'python'
    reference_path = fixtures_path / 'reference'

    generate(python_path, build_path)

    assert_yaml_dirs_equal(build_path, reference_path)
