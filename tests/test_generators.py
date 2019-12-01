from pathlib import Path

import yaml

from kustomize.generators import generate


def assert_yaml_dirs_equal(a, b):
    a_files = list(Path(a).rglob('*.yaml'))
    b_files = list(Path(b).rglob('*.yaml'))

    assert len(a_files) == len(b_files)

    for a_file, b_file in zip(a_files, b_files):
        with open(str(a_file)) as f:
            a_data = yaml.safe_load(f)
        with open(str(b_file)) as f:
            b_data = yaml.safe_load(f)

        assert a_data == b_data


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
