from shell.shell import Shell


class FakeShell(Shell):
    def __init__(self, working_directory):
        super().__init__(working_directory)
        self.command = []

    def execute(self, command):
        self.command = command

    def get_executed_command(self):
        return ' '.join(self.command)
