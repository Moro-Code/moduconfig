import moduconfig.moduconfig as moduconfig_class


class Variable:
    def __init__(self, name: str, data: dict, moduconfig: moduconfig_class.ModuConfig):
        if not isinstance(name, str):
            raise TypeError(
                "name must be of type str, recieved type %s" % type(
                    name
                ).__name__
            )

        if not isinstance(data, dict):
            raise TypeError(
                "data must be of type dict, recieved type %s" % type(
                    data
                ).__name__
            )

        if not isinstance(moduconfig, moduconfig_class.ModuConfig):
            raise TypeError(
                "moduconfig must be an instance of ModuConfig, " +
                "recieved type %s" % type(
                    moduconfig
                ).__name__
            )
        self.name = name
        self.data = data
        self.moduconfig = moduconfig
