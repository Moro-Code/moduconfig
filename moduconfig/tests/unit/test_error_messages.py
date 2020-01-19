import pytest
from .fixtures.error_messages import error_messages_module


def test_RequiredKeyIsMissing(error_messages_module):

    assert error_messages_module.RequiredKeyIsMissing == \
        "No value was found for the required key `{key_name}`"


def test_RequiredKeyIsWrongType(error_messages_module):
    assert error_messages_module.RequiredKeyIsWrongType == \
        (
            "Required key `{key_name}` has the wrong " +
            "type of `{invalid_type}`. The value of this key " +
            "should have the type `{expected_type}`"
        )
