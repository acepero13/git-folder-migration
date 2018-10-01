import errno
import os
import shutil
import stat


def error_remove_readonly(func, path, exc):
    excvalue = exc[1]
    if excvalue.errno == errno.EACCES and not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
        func(path)
    else:
        print('Could not delete folder: ' + path + '. Please, try to delete it manually')
        exit(1)


class Folder(object):
    def __init__(self, working_directory):
        self.working_directory = working_directory

    def force_create(self, folder):
        folder_path = self.build_path(folder)
        if not os.path.exists(folder_path):
            self.create(folder_path)
        else:
            self.remove(folder_path)
            self.create(folder_path)
        return folder_path

    @staticmethod
    def create(folder_path):
        os.makedirs(folder_path)

    def remove(self, folder_path):
        shutil.rmtree(self.build_path(folder_path), ignore_errors=False, onerror=error_remove_readonly)

    def build_path(self, folder):
        if self.working_directory is None:
            return folder
        return os.path.join(self.working_directory, folder)
