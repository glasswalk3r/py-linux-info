"""Linux distribution basic information."""


class Distribution:
    """This is a base class that defines the most basic information one could
    retrieve from a Linux distribution.

    You probably want to the take a look of subclasses of this classes, unless
    you looking for creating a entirely new classes tree.

    Also, you probably want to use a factory class to create new instances
    instead doing it manually.

    At the end, modules under the ``Distribution`` tries to rely more in the
    ``/etc/os-release`` file, which is more standardized and includes more
    information."""

    def __init__(self, name: str, id: str, version: str, version_id: str) -> None:
        self.__name = name
        self.__id = id
        self.__version = version
        self.__version_id = version_id

    @property
    def name(self) -> str:
        """Return the name of the Linux distribution."""
        return self.__name

    @property
    def id(self) -> str:
        """Return the ID of the Linux distribution."""
        return self.__id

    @property
    def version(self) -> str:
        """Return the Linux distribution version with additional details,
        like the version code name."""
        return self.__version

    @property
    def version_id(self) -> str:
        """Return the version of the Linux distribution, usually only numbers"""
        return self.__version_id

    def __str__(self) -> str:
        """The string representation of the instance, with name and version
        information"""
        return f"{self.__name} {self.__version}"
