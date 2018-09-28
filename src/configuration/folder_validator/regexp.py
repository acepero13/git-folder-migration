import re

from configuration.folder_validator.decorator import Decorator


class RegExp(Decorator):
    def __init__(self, validator, regexp):
        super().__init__(validator)
        self.regexp = regexp

    def is_valid(self, folder_name):
        return self._validator.is_valid(folder_name) and re.match(self.regexp, folder_name)
