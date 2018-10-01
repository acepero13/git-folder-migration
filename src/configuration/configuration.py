import os

from configuration.validator_factory import ValidatorFactory
from constants import constants


class Configuration(object):
    def __init__(self, **kwds):
        self.__dict__['branch'] = constants.BRANCH
        self.__dict__.update(kwds)

    def folder_to_discover(self):
        cwd = self.__dict__['working_directory']
        sub_folder = self.__dict__['sub_folder']
        return os.path.join(cwd, constants.ORIGIN_FOLDER_NAME, sub_folder)

    def is_allowed(self, folder_name):
        validator = ValidatorFactory(self).create()
        return validator.is_valid(folder_name)
