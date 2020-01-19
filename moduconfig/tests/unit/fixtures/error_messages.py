import pytest


@pytest.fixture
def error_messages_module(scope="module"):
    from moduconfig.utils import error_messages

    return error_messages
