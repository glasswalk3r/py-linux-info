from abc import abstractmethod
from typing import Dict, Tuple

from linux_info.properties.distribution.base import Distribution


class MissingStandardProperty(ValueError):
    def __init__(self, file_path: str, missing: str) -> None:
        super().__init__(f"Missing a expected property on {file_path}: {missing}")
        self.file_path = file_path
        self.missing = missing


class InvalidKeyValueLine(ValueError):
    def __init__(self, line: str) -> None:
        super().__init__(f"Unexpected line format: {line}")
        self.line = line


def parse(file_path: str) -> Dict[str, str]:
    data = {}

    with open(file_path, "r") as fp:
        for line in fp:
            line = line.strip()

            if line == "":
                continue

            pieces = line.split("=")

            try:
                data[pieces[0].lower()] = pieces[1].replace('"', "")
            except IndexError:
                raise InvalidKeyValueLine(line)

    return data


def default_source_file() -> str:
    return "/etc/os-release"


class OSRelease(Distribution):
    def __init__(self, source: str = default_source_file()):
        self.source = source
        self.cache: Dict[str, str] = parse(self.source)
        self.pretty_name: None | str = None
        self.id_like: None | Tuple[str, ...] = None
        self.home_url: None | str = None
        self._parse()

    @staticmethod
    def default_file() -> str:
        return default_source_file()

    def _parse(self) -> None:
        super().__init__(
            name=self.cache["name"],
            id=self.cache["id"],
            version=self.cache["version"],
            version_id=self.cache["version_id"],
        )

        wanted = ("pretty_name", "home_url")

        try:
            for attrib in wanted:
                setattr(self, attrib, self.cache[attrib])
        except ValueError as e:
            raise MissingStandardProperty(self.source, str(e))

        if "id_like" in self.cache:
            distros = self.cache["id_like"].split(" ")
            self.id_like = tuple(distros)

    @staticmethod
    def parse_from_file(file_path: str = "/etc/os-release") -> Dict[str, str]:
        return parse(file_path)

    def clean_cache(self) -> None:
        """This class caches the information read from the source file into memory, so
        subclasses can reuse this information to handle additional attributes.

        After that, the information is usually not necessary anymore and should be
        removed by invoking this method."""
        self.cache = {}

    @abstractmethod
    def _handle_missing(self, data: Dict[str, str]) -> None:
        """ "Handle missing fields.

        It should be overrided by subclasses of this class.

        It expects as positional parameter the returned value of the ``parsed``
        method."""
        pass
