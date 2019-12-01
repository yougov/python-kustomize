from kustomize.main import run
from tests.base import assert_yaml_dirs_equal


def test_generates_simple_dict(cd_fixtures, create_build_path):
    fixtures_path = cd_fixtures('simple_dict')
    build_path = create_build_path()
    python_path = fixtures_path / 'python'
    reference_path = fixtures_path / 'reference'

    args = [
        '--attr-name', 'my_kustomization',
        str(python_path),
        str(build_path),
    ]

    run(args)

    assert_yaml_dirs_equal(build_path, reference_path)
