import pytest
from moduconfig import ModuConfig


@pytest.fixture
def config_scafold():
    return {
        "applicationName": "MY_AWESOME_APPLICATION",
        "modes": {
            "testing": "testing mode",
            "development": "develop mode",
            "production": "production mode"
        },
        "variables": {}
    }


@pytest.fixture
def valid_variable(config_scafold):
    config_scafold["variables"]["VALID_VARIABLE"] = {
        "required": True,
        "default": "hello",
        "type": str
    }
    return "VALID_VARIABLE",
    ModuConfig(config_scafold),
    config_scafold["variables"]["VALID_VARIABLE"]
