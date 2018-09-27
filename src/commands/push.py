from src.commands.abstract_git_command import AbstractGitCommand
class Push(AbstractGitCommand):
    def __init__(self, remote_name, branch):
        super().__init__()
        self.remote = remote_name
        self.branch = branch

    def buildCommand(self):
        super().add('push').add('-u').add(self.remote).add(self.branch)
        