import os
import shutil
from pathlib import Path

import pytest


@pytest.fixture
def fixtures_path():
    return Path(__file__).parent / 'fixtures'


@pytest.fixture
def cd_fixtures(request, fixtures_path):
    prev_dir = os.getcwd()

    def back():
        os.chdir(prev_dir)

    def next_dir(path):
        next_path = fixtures_path / path
        os.chdir(next_path)
        return next_path

    request.addfinalizer(back)

    return next_dir


@pytest.fixture
def create_build_path(request):
    def create():
        path = Path(__file__).parent / 'build'
        os.makedirs(str(path), exist_ok=True)

        def remove():
            shutil.rmtree(path)

        request.addfinalizer(remove)

        return path

    return create
