import unittest
from src.commands.create_repo import CreateRepo
class TestCreateRepoCommand(unittest.TestCase):
    def test_builds_clone_command(self):
        create  = CreateRepo('git@gitlab.example.com:namespace/', 'extensionName', 'master')
        create.execute()
        self.assertEquals('git push --set-upstream git@gitlab.example.com:namespace/extensionName.git master', create.asString())