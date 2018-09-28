import unittest

from io_utils.directory_discover import DirectoryDiscover


class ListDirectoriesTest(unittest.TestCase):
    def test_list_only_directories(self):
        discover = DirectoryDiscover(
            'C:\\Users\\amador\\Documents\\Projects\\TableSorter-master\\mytestproject\\src\\sorter\\')
        self.assertEqual(6, len(discover.list()))
