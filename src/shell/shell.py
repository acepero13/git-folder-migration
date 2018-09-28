from subprocess import Popen, PIPE


class Shell(object):
    def __init__(self, working_directory):
        self.working_directory = working_directory

    def execute(self, command):
        git_query = Popen(command, cwd=self.working_directory, stdout=PIPE, stderr=PIPE)
        (result, error) = git_query.communicate()
        print(error)
        if git_query.poll() == 0:
            pass
