from .utils.error_messages import (
    RequiredKeyIsMissing,
    RequiredKeyIsWrongType,
    DirectiveStructureError
)


from typing import Optional, Dict


class ModuConfig:
    def __init__(self, config_data: dict, mode_data: Optional[Dict[str, str]] = None):

        if config_data is None:
            raise ValueError("config_data must not be None")

        self.config_data = config_data
        self.mode_data = mode_data

        self.applicationName = config_data.get("applicationName")
        if self.applicationName is None:
            raise ValueError(
                RequiredKeyIsMissing.format(
                    key_name="applicationName"
                )
            )
        elif not isinstance(self.applicationName, str):
            raise TypeError(
                RequiredKeyIsWrongType.format(
                    key_name="applicationName",
                    invalid_type=type(self.applicationName).__name__,
                    expected_type="str"
                )
            )

        self.modes = config_data.get("modes")
        if self.modes is None:
            raise ValueError(
                RequiredKeyIsMissing.format(
                    key_name="modes"
                )
            )
        elif not isinstance(self.modes, dict):
            raise TypeError(
                RequiredKeyIsWrongType.format(
                    key_name="modes",
                    invalid_type=type(self.modes).__name__,
                    expected_type="dict"
                )
            )
        for mode in self.modes:
            if not isinstance(mode, str):
                raise ValueError(
                    DirectiveStructureError.format(
                        directive="modes",
                        problem="modes must be of type Dict[str,str] " +
                        "detected key with type %s" % type(mode).__name__
                    )
                )
            if not isinstance(self.modes[mode], str):
                raise ValueError(
                    DirectiveStructureError.format(
                        directive="modes",
                        problem="modes must be of type Dict[str,str]"
                    ) + "Offending mode is `%s`" % mode
                )

        self.variables = config_data.get("variables")
        if self.variables is None:
            raise ValueError(
                RequiredKeyIsMissing.format(
                    key_name="variables"
                )
            )
        elif not isinstance(self.variables, dict):
            raise TypeError(
                RequiredKeyIsWrongType.format(
                    key_name="variables",
                    invalid_type=type(self.variables).__name__,
                    expected_type="dict"
                )
            )
