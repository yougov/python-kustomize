import os
import shutil

import pytest
import yaml

from kustomize.generators import generate


@pytest.fixture(scope='function')
def simple_dict_path(request, fixtures_path):
    path = fixtures_path / 'simple_dict'
    build_path = path / 'build'
    os.makedirs(str(build_path), exist_ok=True)

    def remove():
        shutil.rmtree(build_path)

    request.addfinalizer(remove)

    return path


def assert_yaml_equal(a, b):
    with open(a) as f:
        a_data = yaml.safe_load(f)
    with open(b) as f:
        b_data = yaml.safe_load(f)

    assert a_data == b_data


def test_generates_simple_dict(simple_dict_path):
    python_path = simple_dict_path / 'python'
    build_path = simple_dict_path / 'build'
    reference_path = simple_dict_path / 'reference'

    generate(python_path, 'my_kustomization', build_path)

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
