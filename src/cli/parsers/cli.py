from cli.parsers.abstract_parser import AbstractParser
from configuration.configuration import Configuration


class OptionsParser(AbstractParser):
    def __init__(self, args):
        self.required = ['source_repo', 'dst_repo', 'cwd', 'sub_folder']
        self.args = args
        self.check_optional_values()
        self.check_required()

    def parse(self):
        return Configuration(original_repo=self.args['source_repo'],
                             new_repo_namespace=self.args['dst_repo'],
                             working_directory=self.args['cwd'],
                             sub_folder=self.args['sub_folder'],
                             allowed_folders=self.args['includes'],
                             not_allowed_folders=self.args['excludes'],
                             regex_for_folder_name=self.args['regexp'],
                             branch=self.args['branch']
                             )

    def check_optional_values(self):
        if self.args.get('includes') is None:
            self.args['includes'] = []
        if self.args.get('excludes') is None:
            self.args['excludes'] = []
        if self.args.get('regexp') is None:
            self.args['regexp'] = ''

    def check_required(self):
        missing = list()
        for required_arg in self.required:
            if self.args.get(required_arg) is None:
                missing.append(required_arg)
        if len(missing) > 0:
            print('Error: the following argument(s) are required: ' + ', '.join(
                missing) + '. Type python main.py --help to see the help')
            exit(1)
