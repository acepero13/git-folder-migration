from abc import ABC, abstractmethod


class AbstractGitCommand(ABC):
    def __init__(self, shell):
        self.shell = shell

    def execute(self):
        for command in self.build_commands():
            self.shell.execute(command.get_command())

    @abstractmethod
    def build_commands(self):
        pass

