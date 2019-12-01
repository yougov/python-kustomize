from pathlib import Path

import yaml


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
