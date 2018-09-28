from commands.command_builder import CommandBuilder
from commands.abstract_command import AbstractCommand


class CreateRepo(AbstractCommand):
    def __init__(self, shell, remote_url, repo_name, branch):
        super().__init__(shell)
        self.remote = remote_url
        self.repo = repo_name
        self.branch = branch

    def build_commands(self):
        return [self.create_push_command(), self.create_set_remote_command()]

    def create_set_remote_command(self):
        command = CommandBuilder()
        command.add('remote').add('set-url').add('origin').add(self.build_repo_url())
        return command

    def create_push_command(self):
        command = CommandBuilder()
        command.add('push').add('--set-upstream').add(self.build_repo_url()).add(self.branch)
        return command

    def build_repo_url(self):
        return self.remote + self.repo + '.git'

