import argparse

from cli.parsers.cli import OptionsParser
from cli.parsers.yaml_parser import YamlParser


class CliParser(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args = None

    def parse(self):
        self.args = self.create_args_options()
        return self.create_parser().parse()

    def create_args_options(self):
        self.parser.add_argument('--source-repo', help='Defines repo to migrate from', required=False)
        self.parser.add_argument('--dst-repo', help='Defines repo (namespace only) to migrate to',
                                 required=False)
        self.parser.add_argument('--cwd', help='Working directory to locate temporary files', required=False)
        self.parser.add_argument('--sub-folder', help='Sub-folders to be migrated', required=False)
        self.parser.add_argument('--includes',
                                 help='Comma separated list of the names of the folders to be included',
                                 required=False)
        self.parser.add_argument('--excludes',
                                 help='Comma separated list of the names of the folders to be excluded',
                                 required=False)
        self.parser.add_argument('--regexp', help='Regular expression for filtering folder names',
                                 required=False)
        self.parser.add_argument('--config-file', help='Use a yaml configuration file instead of arguments. Hint: '
                                                       'edit the config.dist.yaml file', required=False)  # Exclusive
        self.parser.add_argument('--branch', help='Branch to clone from. By default uses master', required=False,
                                 default='master')
        return vars(self.parser.parse_args())

    def create_parser(self):
        if self.args.get('config_file') is not None:
            return YamlParser(self.args['config_file'])
        return OptionsParser(self.args)
