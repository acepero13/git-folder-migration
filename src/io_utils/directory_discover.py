import os


class DirectoryDiscover(object):
    def __init__(self, working_directory):
        self.working_directory = working_directory

    def list(self):
        directory = self.working_directory
        return [(os.path.join(directory, o), o) for o in os.listdir(directory) if
                os.path.isdir(os.path.join(directory, o))]
