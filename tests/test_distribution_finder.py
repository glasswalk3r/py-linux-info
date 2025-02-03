import inspect
from linux_info.properties.distribution.finder import Finder


def test_instance_attributes():
    instance = Finder()
    expected = ("_config_dir", "keep_cache", "custom_source_dir", "custom_file", "distro_info")

    for attribute in expected:
        assert hasattr(instance, attribute)


def test_instance_methods():
    instance = Finder()
    expected = ("has_distro_info", "_read_config_dir")

    for method in expected:
        assert inspect.ismethod(getattr(instance, method))

    assert instance.has_distro_info() is False
    assert instance.config_dir == "/etc"
