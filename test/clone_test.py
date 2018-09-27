import unittest
from src.commands.clone import Clone
class TestCloneCommand(unittest.TestCase):
    def test_builds_clone_command(self):
        clone  = Clone('https://github.com/USERNAME/REPOSITORY-NAME', 'extensionName')
        clone.execute()
        self.assertEquals('git clone https://github.com/USERNAME/REPOSITORY-NAME extensionName', clone.asString())