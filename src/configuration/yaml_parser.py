import os

import yaml

from configuration.configuration import Configuration


class YamlParser(object):
    def __init__(self, file):
        self.file = file

    def parse(self):
        if not os.path.isfile(self.file):
            raise Exception('Configuration file: ' + self.file + 'does not exists')
        with open(self.file, 'r') as stream:
            data_loaded = yaml.safe_load(stream)
        migrator = data_loaded['migrator']
        config = Configuration(original_repo=migrator['original_repo'],
                               new_repo_namespace=migrator['new_repo_namespace'],
                               working_directory=migrator['working_directory'],
                               sub_folder=migrator['sub_folder'],
                               allowed_folders=migrator['includes'],
                               not_allowed_folders=migrator['excludes'],
                               regex_for_folder_name=migrator['regex_folder_name']
                               )
        return config
