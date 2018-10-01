import unittest
from commands.git.filter import Filter
from test.fakes.fake_command import FakeShell


class TestFilterCommand(unittest.TestCase):
    def test_builds_clone_command(self):
        shell = FakeShell('/fake/path')
        filter = Filter(shell, 'extensionName', 'master')
        filter.execute()
        self.assertEqual('git filter-branch --prune-empty --subdirectory-filter extensionName master',
                         shell.get_executed_command())
