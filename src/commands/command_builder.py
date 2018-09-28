class CommandBuilder(object):
    def __init__(self, initial=None):
        if initial is None:
            initial = ['git']
        self.command = initial

    def add(self, argument):
        self.command.append(argument)
        return self

    def get_command(self):
        return self.command
