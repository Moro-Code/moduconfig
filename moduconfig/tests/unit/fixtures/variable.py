import pytest
from .moduconfig import moduconfig_class, sample_configuration_data_no_variables


@pytest.fixture
def variable_class():
    from moduconfig import Variable
    return Variable


@pytest.fixture
def valid_variable(sample_configuration_data_no_variables, moduconfig_class):
    data = sample_configuration_data_no_variables
    data["variables"] = {}
    data["variables"]["VALID_VARIABLE"] = {
        "required": True,
        "default": "hello",
        "type": str
    }
    return ("VALID_VARIABLE",
            moduconfig_class(data),
            data["variables"]["VALID_VARIABLE"])
