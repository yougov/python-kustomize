import argparse
import logging
import sys
from pathlib import Path


def _get_options(args):
    parser = argparse.ArgumentParser(description="""
        Generates a kustomization directory based on similar Python files.
        The generated directory can then be used by Kustomize.
    """)

    parser.add_argument(
        '--attr-name', '-a', default='kustomization', required=False,
        help='Name of the attribute from the kustomization.py files.'
    )
    parser.add_argument(
        '--verbose', '-v', default=False, action='store_true',
        help='Print debug logs to stdout.'
    )
    parser.add_argument(
        'source_path',
        help='Source directory with Python kustomization files.'
    )
    parser.add_argument(
        'dest_path',
        help=(
            'Destination directory where the Kustomize YAML files will be '
            'put at.')
    )

    return parser.parse_args(args)


def run(args):
    options = _get_options(args)
    if options.verbose:
        level = logging.DEBUG
    else:
        level = logging.INFO
    logging.basicConfig(level=level)
    _generate_from_options(options)


def _generate_from_options(options):
    from kustomize.generators import generate

    source_path = Path(options.source_path)
    dest_path = Path(options.dest_path)
    generate(source_path, dest_path, options.attr_name)


def main():  # pragma: no cover
    run(sys.argv[1:])


if __name__ == '__main__':  # pragma: no cover
    main()
