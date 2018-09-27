from src.commands.abstract_git_command import AbstractGitCommand
class Clone(AbstractGitCommand):
    def __init__(self, repo_url, folderName):
        super().__init__()
        self.url = repo_url
        self.name = folderName

    def buildCommand(self):
        super().add('clone').add(self.url).add(self.name)
        