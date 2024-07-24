import inspect

from linux_info.properties.distribution.dto import Basic


def tests_class():
    assert inspect.isclass(Basic)


def test_instance():
    source_file = "/etc/os-release"
    distro = "ubuntu"
    instance = Basic(distro_id=distro, file_path=source_file)
    assert isinstance(instance, Basic)

    for attribute in ("distro_id", "file_path"):
        assert hasattr(instance, attribute)

    assert instance.distro_id == distro
    assert instance.file_path == source_file
