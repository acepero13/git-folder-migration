import unittest
from commands.git.clone import Clone
from test.fakes.fake_command import FakeShell


class TestCloneCommand(unittest.TestCase):
    def test_builds_clone_command(self):
        shell = FakeShell('/fake/path')
        clone = Clone(shell, 'https://github.com/USERNAME/REPOSITORY-NAME', 'extensionName')
        clone.execute()
        self.assertEqual('git clone https://github.com/USERNAME/REPOSITORY-NAME extensionName',
                         shell.get_executed_command())
