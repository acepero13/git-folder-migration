from src.commands.clone import Clone
from src.commands.filter import Filter
from src.commands.create_repo import CreateRepo
from src.commands.push import Push
class Migrator(object):
    def __init__(self, config):
        self.config = config

    def migrate(self):
        self.clone()
        self.filterOnlyFolder()
        self.createRepo()
        self.push()

    def clone(self):
        Clone(self.config['repo_url'], self.config['extensionName']).execute()

    def filterOnlyFolder(self):
       Filter(self.config['folderName'], self.config['extensionPath'], 'master').execute()
    

    def createRepo(self):
        CreateRepo(self.config['folderName'], self.config['extensionName'], 'master').execute()
    
    def push(self):
        Push('origin', 'master').execute()