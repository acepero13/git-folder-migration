import unittest
from src.commands.push import Push
class TestPushCommand(unittest.TestCase):
    def test_builds_push_command(self):
        push  = Push('origin', 'master')
        push.execute()
        self.assertEquals('git push -u origin master', push.asString())