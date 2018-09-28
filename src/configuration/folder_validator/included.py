from configuration.folder_validator.decorator import Decorator


class Included(Decorator):
    def __init__(self, validator, allowed_folders):
        super().__init__(validator)
        self.allowed_folders = allowed_folders

    def is_valid(self, folder_name):
        return self._validator.is_valid(folder_name) and folder_name in self.allowed_folders
