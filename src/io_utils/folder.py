import os
import shutil


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

    def create(self, folder_path):
        os.makedirs(folder_path)

    def remove(self, folder_path):
        shutil.rmtree(self.build_path(folder_path), ignore_errors=False)

    def build_path(self, folder):
        if self.working_directory is None:
            return folder
        return os.path.join(self.working_directory, folder)
