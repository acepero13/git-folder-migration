from abc import ABC, abstractmethod
class AbstractGitCommand(ABC):
    def __init__(self):
        self.commands = ['git']

    def add(self, arg):
        self.commands.append(arg)
        return self

    def execute(self):
        self.buildCommand()

    @abstractmethod
    def buildCommand(self):
        pass

    def asString(self):
        return ' '.join(self.commands)

    

    
    
    
