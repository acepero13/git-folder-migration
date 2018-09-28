import abc

from configuration.folder_validator.validator import Validator


class Decorator(Validator, metaclass=abc.ABCMeta):
    """
    Maintain a reference to a Component object and define an interface
    that conforms to Component's interface.
    """

    def __init__(self, validator):
        self._validator = validator

    @abc.abstractmethod
    def is_valid(self, folder_name):
        pass
