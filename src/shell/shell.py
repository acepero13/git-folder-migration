import logging
from subprocess import Popen, PIPE

logging.basicConfig(filename='../shell.log', level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.basicConfig()


class Shell(object):
    def __init__(self, working_directory):
        self.working_directory = working_directory

    def execute(self, command):
        git_query = Popen(command, cwd=self.working_directory, stdout=PIPE, stderr=PIPE)
        (result, error) = git_query.communicate()
        self.log(result, error)
        if git_query.poll() == 0:
            pass

    @staticmethod
    def log(result, error):
        logging.info(result)
        if error:
            logging.error(error)
