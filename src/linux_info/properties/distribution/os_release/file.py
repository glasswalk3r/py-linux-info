"""Implementation details of the os_release file."""


class MissingStandardProperty(ValueError):
    def __init__(self, file_path: str, missing: str) -> None:
        super().__init__(f"Missing a expected property on {file_path}: {missing}")
        self.file_path = file_path
        self.missing = missing


class InvalidKeyValueLine(ValueError):
    def __init__(self, line: str) -> None:
        super().__init__(f"Unexpected line format: {line}")
        self.line = line


def parse(file_path: str) -> dict[str, str]:
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
