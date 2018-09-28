from commands.command_builder import CommandBuilder
from commands.abstract_command import AbstractCommand


class Push(AbstractCommand):
    def __init__(self, shell, remote_name, branch):
        super().__init__(shell)
        self.remote = remote_name
        self.branch = branch

    def build_commands(self):
        command = CommandBuilder()
        command.add('push').add('-u').add(self.remote).add(self.branch)
        return [command]

