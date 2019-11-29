from dataclasses import asdict


def to_dict(manifest) -> dict:
    return asdict(manifest)
