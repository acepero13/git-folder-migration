from src.commands.abstract_git_command import AbstractGitCommand


class Filter(AbstractGitCommand):
    def __init__(self, folderName, folderPath, branch):
        super().__init__()
        self.name = folderName
        self.branch = branch

    def buildCommand(self):
        super().add('filter-branch').add('--prune-empty').add(
            '--subdirectory-filter').add(self.name).add(self.branch)
