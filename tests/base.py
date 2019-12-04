from pathlib import Path

import yaml


def assert_yaml_dirs_equal(a, b):
    a_files = list(Path(a).rglob('*.yaml'))
    b_files = list(Path(b).rglob('*.yaml'))

    assert len(a_files) == len(b_files)

    for a_file, b_file in zip(a_files, b_files):
        with open(str(a_file)) as f:
            a_data = tuple(yaml.safe_load_all(f))
        with open(str(b_file)) as f:
            b_data = tuple(yaml.safe_load_all(f))

        for a_datum, b_datum in zip(a_data, b_data):
            assert a_data == b_data, f"""
            Got from {a}: {a_data}
            Expected from {b}: {b_data}
            """
