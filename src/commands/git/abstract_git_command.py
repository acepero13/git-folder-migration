from abc import ABC, abstractmethod


class AbstractGitCommand(ABC):
    def __init__(self, shell):
        self.commands = ['git']
        self.shell = shell;

    def add(self, arg):
        self.commands.append(arg)
        return self

    def execute(self):
        self.build_command()
        self.shell.execute(self.commands)

    @abstractmethod
    def build_command(self):
        pass

