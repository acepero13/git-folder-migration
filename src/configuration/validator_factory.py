from configuration.folder_validator.default import Default
from configuration.folder_validator.excluded import Excluded
from configuration.folder_validator.included import Included
from configuration.folder_validator.regexp import RegExp


class ValidatorFactory(object):

    def __init__(self, config):
        self.config = config

    def create(self):
        validator = Default()
        if self.config.allowed_folders is not None and len(self.config.allowed_folders) > 0:
            validator = Included(validator, self.config.allowed_folders)
        if self.config.not_allowed_folders is not None and len(self.config.not_allowed_folders) > 0:
            validator = Excluded(validator, self.config.not_allowed_folders)
        if self.config.regex_for_folder_name is not None and len(self.config.regex_for_folder_name) > 0:
            validator = RegExp(validator, self.config.regex_for_folder_name)
        return validator
