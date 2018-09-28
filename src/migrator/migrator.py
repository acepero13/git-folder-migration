import os

from commands.git.clone import Clone
from commands.git.filter import Filter
from commands.git.create_repo import CreateRepo
from commands.git.push import Push
from io_utils.folder import Folder
from shell.shell import Shell
from constants import constants


class Migrator(object):
    def __init__(self, config, dir_discover):
        self.cloned = ''
        self.origin = ''
        self.config = config
        self.dir_discover = dir_discover

    def migrate(self):
        self.prepare_for_migration()
        self.migrate_folders()
        self.clean_up()

    def migrate_folders(self):
        folders_to_migrate = self.dir_discover.list()
        for folder_path, folder_name in folders_to_migrate:
            if not self.config.is_allowed(folder_name):
                continue
            operations = self.prepare_folder_migration(folder_name, folder_path)
            self.start_migration(operations)

    def prepare_for_migration(self):
        self.create_folder_structure()
        Clone(Shell(self.origin), self.config.original_repo, self.origin).execute()

    def prepare_folder_migration(self, folder_name, folder_path):
        shell_repo = Shell(os.path.join(self.cloned, folder_name))
        folder = folder_path[len(self.origin) + 1:].replace('\\', '/')
        return [Clone(Shell(self.cloned), self.config.original_repo, folder_name),
                Filter(shell_repo, folder, folder, 'master'),
                CreateRepo(shell_repo, self.config.new_repo_namespace, folder_name, 'master'),
                Push(shell_repo, 'origin', 'master')
                ]

    def clean_up(self):
        folder = Folder(None)
        folder.remove(self.cloned)
        folder.remove(self.origin)

    def start_migration(self, operations):
        for operation in operations:
            operation.execute()

    def create_folder_structure(self):
        folder = Folder(self.config.working_directory)
        self.cloned = folder.force_create(constants.CLONED_FOLDER_NAME)
        self.origin = folder.force_create(constants.ORIGIN_FOLDER_NAME)
