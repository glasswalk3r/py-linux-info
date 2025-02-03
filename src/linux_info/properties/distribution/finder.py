from pathlib import Path
from collections import deque


class Finder:
    """Search for candidate files to identify a Linux distribution."""

    __release_files = {
        "gentoo-release": "gentoo",
        "fedora-release": "fedora",
        "centos-release": "centos",
        "enterprise-release": "oracle enterprise linux",
        "turbolinux-release": "turbolinux",
        "mandrake-release": "mandrake",
        "mandrakelinux-release": "mandrakelinux",
        "debian_version": "debian",
        "debian_release": "debian",
        "SuSE-release": "suse",
        "knoppix-version": "knoppix",
        "yellowdog-release": "yellowdog",
        "slackware-version": "slackware",
        "slackware-release": "slackware",
        "redflag-release": "redflag",
        "redhat-release": "redhat",
        "redhat_version": "redhat",
        "conectiva-release": "conectiva",
        "immunix-release": "immunix",
        "tinysofa-release": "tinysofa",
        "trustix-release": "trustix",
        "adamantix_version": "adamantix",
        "yoper-release": "yoper",
        "arch-release": "arch",
        "libranet_version": "libranet",
        "va-release": "va-linux",
        "pardus-release": "pardus",
        "system-release": "amazon",
        "CloudLinux-release": "CloudLinux",
    }

    __slots__ = (
        "custom_source_dir",
        "custom_file",
        "_config_dir",
        "distro_info",
        "keep_cache",
    )

    def __init__(self, config_dir: str = "/etc", keep_cache: bool = False) -> None:
        self._config_dir = config_dir
        self.keep_cache = keep_cache
        self.custom_source_dir = False
        self.custom_file = False
        self.distro_info = None

    def has_distro_info(self) -> bool:
        """Returns "true" (1) if the instance has already cached distribution information.

        Otherwise, returns "false" (0).
        """
        if self.distro_info is not None:
            return True

        return False

    @property
    def config_dir(self) -> str:
        """Return the default configuration directory used by a instance."""
        return self._config_dir

    @config_dir.setter
    def config_dir(self, dir: str) -> None:
        """Change the default configuration directory used by a instance.

        Useful for unit testing with mocks.
        """
        self._config_dir = dir
        self.custom_source_dir = True

    def _read_config_dir(self) -> deque[Path]:
        p = Path(self.config_dir)
        candidates: deque[Path] = deque()

        for file in p.glob("*version", case_sensitive=True):
            candidates.append(file)

        for file in p.glob("*release", case_sensitive=True):
            candidates.append(file)

        return candidates
