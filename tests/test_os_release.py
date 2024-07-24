import os

from linux_info.properties.distribution.os_release.base import (
    OSRelease,
    default_source_file,
    parse,
)


def test_default_source():
    assert default_source_file() == "/etc/os-release"


def test_parse():
    data = parse(default_source_file())
    assert isinstance(data, dict)
    assert len(data.keys()) == 12
    wanted = (
        "pretty_name",
        "name",
        "version_id",
        "version",
        "version_codename",
        "id",
        "id_like",
        "home_url",
        "support_url",
        "bug_report_url",
        "privacy_policy_url",
    )

    for key in wanted:
        assert key in data


def test_instance():
    source_file = os.path.join("tests", "fixtures", "os-releases", "ubuntu")
    instance = OSRelease(source=source_file)
    assert isinstance(instance, OSRelease)
    assert instance.name == "Ubuntu"
    assert instance.version_id == "22.04"
    assert instance.version == "22.04.4 LTS (Jammy Jellyfish)"
    assert instance.id == "ubuntu"
    assert instance.source == source_file
