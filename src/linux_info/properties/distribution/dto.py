"""DTO classes."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Basic:
    """DTO to be exchanged between distribution finders and factories."""

    distro_id: str
    file_path: str
