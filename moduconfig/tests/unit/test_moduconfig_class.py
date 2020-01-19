import pytest
from .fixtures.moduconfig import moduconfig_class
from .fixtures.error_messages import error_messages_module

################################################# FIXTURES #############################################################################
@pytest.fixture
def valid_sample_configuration_data():
    return {
        "applicationName": "MY_AWESOME_APP",
        "modes": {
            "testing": "Mode for integration tests to ensure application is functioning correctly",
            "development": "Mode for developing the application, should only be used to develop locally and not to serve clients",
            "production": "Mode for running the application to serve clients"
        },
        "variables": {
            "APPLICATION_VARIABLE": {
                "required": True,
                "default": "Hello",
                "type": str
            }
        }
    }


@pytest.fixture
def sample_configuration_data_no_applicationName(valid_sample_configuration_data):
    data = valid_sample_configuration_data
    del data["applicationName"]
    return data


@pytest.fixture
def sample_configuration_data_no_modes(valid_sample_configuration_data):
    data = valid_sample_configuration_data
    del data["modes"]
    return data


@pytest.fixture
def sample_configuration_data_no_variables(valid_sample_configuration_data):
    data = valid_sample_configuration_data
    del data["variables"]
    return data


@pytest.fixture
def sample_configuration_data_applicationName_wrong_type(
    sample_configuration_data_no_applicationName
):
    data = sample_configuration_data_no_applicationName
    data["applicationName"] = 1
    return data


@pytest.fixture
def sample_configuration_data_modes_wrong_type(
    sample_configuration_data_no_modes
):
    data = sample_configuration_data_no_modes
    data["modes"] = 1
    return data


@pytest.fixture
def sample_configuration_data_variables_wrong_type(
    sample_configuration_data_no_variables
):
    data = sample_configuration_data_no_variables
    data["variables"] = 1
    return data

#####################################################################################


################################################ TESTS #############################

def test_ModuConfig_init(
    moduconfig_class,
    valid_sample_configuration_data
):
    new_moduconfig = moduconfig_class(valid_sample_configuration_data)


def test_ModuConfig_init_sets_config_data(
    moduconfig_class,
    valid_sample_configuration_data
):
    new_moduconfig = moduconfig_class(valid_sample_configuration_data)
    assert new_moduconfig.config_data == valid_sample_configuration_data


def test_ModuConfig_init_sets_application_name(
    moduconfig_class,
    valid_sample_configuration_data
):
    new_moduconfig = moduconfig_class(valid_sample_configuration_data)
    assert new_moduconfig.applicationName == valid_sample_configuration_data[
        "applicationName"
    ]


def test_ModuConfig_init_sets_modes(
    moduconfig_class,
    valid_sample_configuration_data
):
    new_moduconfig = moduconfig_class(valid_sample_configuration_data)
    assert new_moduconfig.modes == valid_sample_configuration_data["modes"]


def test_ModuConfig_init_sets_variables(
    moduconfig_class,
    valid_sample_configuration_data
):
    new_moduconfig = moduconfig_class(valid_sample_configuration_data)
    assert new_moduconfig.variables == valid_sample_configuration_data["variables"]


def test_ModuConfig_init_no_application_name_raises_value_error(
    moduconfig_class,
    sample_configuration_data_no_applicationName,
    error_messages_module
):
    with pytest.raises(
        ValueError,
        match=error_messages_module.RequiredKeyIsMissing.format(
            key_name="applicationName"
        )
    ):
        new_moduconfig = moduconfig_class(
            sample_configuration_data_no_applicationName
        )


def test_ModuConfig_init_no_mode_raises_value_error(
    moduconfig_class,
    sample_configuration_data_no_modes,
    error_messages_module
):
    with pytest.raises(
        ValueError,
        match=error_messages_module.RequiredKeyIsMissing.format(
            key_name="modes"
        )
    ):
        new_moduconfig = moduconfig_class(
            sample_configuration_data_no_modes
        )


def test_ModuConfig_init_no_variables_raises_value_error(
    moduconfig_class,
    sample_configuration_data_no_variables,
    error_messages_module
):
    with pytest.raises(
        ValueError,
        match=error_messages_module.RequiredKeyIsMissing.format(
            key_name="variables"
        )
    ):
        new_moduconfig = moduconfig_class(
            sample_configuration_data_no_variables
        )


def test_ModuConfig_init_applicationName_wrong_type(
    moduconfig_class,
    sample_configuration_data_applicationName_wrong_type,
    error_messages_module
):
    with pytest.raises(
        TypeError,
        match=error_messages_module.RequiredKeyIsWrongType.format(
            key_name="applicationName",
            invalid_type="int",
            expected_type="str"
        )
    ):
        new_moduconfig = moduconfig_class(
            sample_configuration_data_applicationName_wrong_type
        )


def test_ModuConfig_init_modes_wrong_type(
    moduconfig_class,
    sample_configuration_data_modes_wrong_type,
    error_messages_module
):
    with pytest.raises(
        TypeError,
        match=error_messages_module.RequiredKeyIsWrongType.format(
            key_name="modes",
            invalid_type="int",
            expected_type="dict"
        )
    ):
        new_moduconfig = moduconfig_class(
            sample_configuration_data_modes_wrong_type
        )


def test_ModuConfig_init_variables_wrong_type(
    moduconfig_class,
    sample_configuration_data_variables_wrong_type,
    error_messages_module
):
    with pytest.raises(
        TypeError,
        match=error_messages_module.RequiredKeyIsWrongType.format(
            key_name="variables",
            invalid_type="int",
            expected_type="dict"
        )
    ):
        new_moduconfig = moduconfig_class(
            sample_configuration_data_variables_wrong_type
        )
