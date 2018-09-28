from commands.git.abstract_git_command import AbstractGitCommand


class Push(AbstractGitCommand):
    def __init__(self, shell, remote_name, branch):
        super().__init__(shell)
        self.remote = remote_name
        self.branch = branch

    def build_command(self):
        super().add('push').add('-u').add(self.remote).add(self.branch)
