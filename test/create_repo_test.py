import unittest
from commands.git.create_repo import CreateRepo
from test.fakes.fake_command import FakeShell


class TestCreateRepoCommand(unittest.TestCase):
    def test_builds_clone_command(self):
        shell = FakeShell('/fake/path')
        create = CreateRepo(shell, 'git@gitlab.example.com:namespace/', 'extensionName', 'master')
        create.execute()
        self.assertEqual('git remote add origin git@gitlab.example.com:namespace/extensionName.git',
                         shell.get_executed_command())
