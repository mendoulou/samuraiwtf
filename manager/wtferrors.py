class WTFError(Exception):
    pass


class ModuleNotFound(WTFError):

    def __init__(self, module):
        self.message = "Module not found: {}".format(module)


class NotImplemented(WTFError):

    def __init__(self, name, provisioner):
        self.message = "Function '{}' is not implemented for the provisioner {}.".format(name, provisioner)

    def __init__(self, name, provisioner, module):
        self.message = "Function '{}' is not implemented in the module '{}'.".format(name, module)


class MissingFunction(WTFError):

    def __init__(self, func, task_type):
        self.message = "Function '{}' is missing from the '{}' plugin.".format(func, task_type)


class MissingRequiredParam(WTFError):

    def __init__(self, param, plugin_name):
        self.message = "Plugin '{}' requires parameter '{}', but this parameter appears to be missing.".format(
            plugin_name, param)
