import pytest


@pytest.fixture(scope="module")
def moduconfig_class():
    from moduconfig import ModuConfig
    return ModuConfig
