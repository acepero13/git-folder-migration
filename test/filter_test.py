import unittest
from src.commands.filter import Filter
class TestFilterCommand(unittest.TestCase):
    def test_builds_clone_command(self):
        filter  = Filter('extensionName', '//path//to//extensionName//', 'master')
        filter.execute()
        self.assertEquals('git filter-branch --prune-empty --subdirectory-filter extensionName master', filter.asString())