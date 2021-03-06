from commands.command_builder import CommandBuilder
from commands.abstract_command import AbstractCommand


class Filter(AbstractCommand):
    def __init__(self, shell, folder_name, branch):
        super().__init__(shell)
        self.folder = folder_name
        self.branch = branch

    def build_commands(self):
        command = CommandBuilder()
        command.add('filter-branch').add('--prune-empty').add(
            '--subdirectory-filter').add(self.folder).add(self.branch)
        return [command]
