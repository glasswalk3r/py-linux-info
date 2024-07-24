from linux_info.properties.distribution.base import Distribution


def test_instance():
    instance = Distribution(
        name="Ubuntu",
        version="22.04.4 LTS (Jammy Jellyfish)",
        version_id="22.04",
        id="ubuntu",
    )

    for i in ("name", "version", "version_id", "id"):
        hasattr(instance, i)

    assert str(instance) == "Ubuntu 22.04.4 LTS (Jammy Jellyfish)"
