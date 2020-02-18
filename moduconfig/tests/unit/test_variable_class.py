import pytest
from .fixtures.moduconfig import (
    moduconfig_class,
    valid_sample_configuration_data,
    sample_configuration_data_no_variables
)
from .fixtures.variable import variable_class, valid_variable


def test_variable_class_init(variable_class, valid_variable):
    variable_name, moduconfig_inst, variable_data = valid_variable

    variable_inst = variable_class(
        variable_name, variable_data, moduconfig_inst)

    assert variable_inst.moduconfig == moduconfig_inst
    assert variable_inst.name == variable_name
    assert variable_inst.data == variable_data


def test_name_must_be_str(variable_class, valid_variable):
    variable_name, moduconfig_inst, variable_data = valid_variable
    variable_class(variable_name, variable_data, moduconfig_inst)

    for i in [1, {"hello": "hello"}, None, False]:
        with pytest.raises(TypeError) as err:
            variable_class(i, variable_data, moduconfig_inst)
        assert str(err.value) == "name must be of type str, recieved type %s" % type(
            i
        ).__name__


def test_data_must_be_dict(variable_class, valid_variable):
    variable_name, moduconfig_inst, variable_data = valid_variable

    variable_class(variable_name, variable_data, moduconfig_inst)

    for i in [1, ["hello", "hello"], None, "hello"]:
        with pytest.raises(TypeError) as err:
            variable_class(variable_name, i, moduconfig_inst)

        assert str(err.value) == "data must be of type dict, recieved type %s" % type(
            i
        ).__name__


def test_moduconfig_must_be_ModuConfig(variable_class, valid_variable):
    variable_name, moduconfig_inst, variable_data = valid_variable

    variable_class(variable_name, variable_data, moduconfig_inst)

    for i in [1, {"hello": "hello"}, None, "hello"]:
        with pytest.raises(TypeError) as err:
            variable_class(variable_name, variable_data, i)

        assert str(err.value) == "moduconfig must be an instance of ModuConfig, recieved type %s" % type(
            i
        ).__name__
