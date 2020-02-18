import pytest
import random
import string


@pytest.fixture(scope="module")
def moduconfig_class():
    from moduconfig import ModuConfig
    return ModuConfig


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


@pytest.fixture
def sample_configuration_data_modes_not_flat(
    sample_configuration_data_no_modes
):
    import string
    import random
    data = sample_configuration_data_no_modes
    key = "".join(
        [random.choice(string.ascii_lowercase) for i in range(0, 20)]
    )
    data["modes"] = {
        key: {
            "not": "flat"
        },
        "production": "is flat"
    }

    return (key, data)


@pytest.fixture
def sample_configuration_data_modes_key_is_int(
    sample_configuration_data_no_modes
):
    # create a modes dictionary and randomly insert int keys
    import random
    modes = {}
    for i in range(40):
        key = "".join(
            [random.choice(string.ascii_lowercase) for i in range(0, 20)]
        )
        modes[key] = key
        if random.randint(0, 3) == 0:
            modes[1] = 0
    data = sample_configuration_data_no_modes
    data["modes"] = modes
    return data


@pytest.fixture
def mode_data_dict():
    return {
        "APPLICATION_VARIABLE": "hello"
    }
