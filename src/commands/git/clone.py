from commands.command_builder import CommandBuilder
from commands.git.abstract_git_command import AbstractGitCommand


class Clone(AbstractGitCommand):
    def __init__(self, shell, repo_url, folder_name):
        super().__init__(shell)
        self.url = repo_url
        self.name = folder_name

    def build_commands(self):
        command = CommandBuilder()
        command.add('clone').add(self.url).add(self.name)
        return [command]

