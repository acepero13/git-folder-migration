import unittest
from commands.git.push import Push
from test.fakes.fake_command import FakeShell


class TestPushCommand(unittest.TestCase):
    def test_builds_push_command(self):
        shell = FakeShell('/fake/path')
        push = Push(shell, 'origin', 'master')
        push.execute()
        self.assertEqual('git push -u origin master', shell.get_executed_command())
