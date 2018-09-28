import os

from commands.git.clone import Clone
from commands.git.filter import Filter
from commands.git.create_repo import CreateRepo
from commands.git.push import Push
from io_utils.folder import Folder
from shell.shell import Shell


class Migrator(object):
    def __init__(self, config, shell, dir_discover):
        self.cloned = ''
        self.origin = ''
        self.config = config
        self.shell = shell
        self.dir_discover = dir_discover
        self.create_folder_structure()

    def migrate(self):
        Clone(Shell(self.origin), self.config['repo_url'], self.origin).execute()
        folders_to_migrate = self.dir_discover.list()
        for folder_path, folder_name in folders_to_migrate:
            operations = self.prepare_migration(folder_name, folder_path)
            self.start_migration(operations)
        self.clean_up()

    def prepare_migration(self, folder_name, folder_path):
        shell_repo = Shell(os.path.join(self.cloned, folder_name))
        folder = folder_path[len(self.origin) + 1:].replace('\\', '/')
        operations = [Clone(Shell(self.cloned), self.config['repo_url'], folder_name),
                      Filter(shell_repo, folder, folder, 'master'),
                      CreateRepo(shell_repo, self.config['new-repo'], folder_name, 'master'),
                      Push(shell_repo, 'origin', 'master')
                      ]
        return operations

    def clean_up(self):
        folder = Folder(None)
        folder.remove(self.cloned)
        folder.remove(self.origin)

    def start_migration(self, operations):
        for operation in operations:
            operation.execute()

    def create_folder_structure(self):
        folder = Folder(self.config['cwd'])
        self.cloned = folder.force_create('clone_tmp')
        self.origin = folder.force_create('origin')
