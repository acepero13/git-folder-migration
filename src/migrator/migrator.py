from commands.git.clone import Clone
from commands.git.filter import Filter
from commands.git.create_repo import CreateRepo
from commands.git.push import Push


class Migrator(object):
    def __init__(self, config, shell):
        self.config = config
        self.shell = shell

    def migrate(self):
        self.clone()
        self.filter_only_folder()
        self.create_repo()
        self.push()

    def clone(self):
        Clone(self.shell, self.config['repo_url'], self.config['extensionName']).execute()

    def filter_only_folder(self):
        Filter(self.shell, self.config['folderName'], self.config['extensionPath'], 'master').execute()

    def create_repo(self):
        CreateRepo(self.shell, self.config['folderName'], self.config['extensionName'], 'master').execute()

    def push(self):
        Push(self.shell, 'origin', 'master').execute()
