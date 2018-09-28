from configuration.folder_validator.validator import Validator


class Default(Validator):

    def is_valid(self, folder_name):
        return True
