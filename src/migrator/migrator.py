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
        self.list_folders_to_migrate = dir_discover

    def migrate(self):
        self.prepare_for_migration()
        self.migrate_folders()
        self.clean_up()

    def prepare_for_migration(self):
        self.create_folder_structure()
        Clone(Shell(self.origin), self.config.original_repo, self.origin).execute()

    def migrate_folders(self):
        for folder_path, folder_name in self.list_folders_to_migrate.list():
            self.migrate_folder(folder_name, folder_path)
        print('Migration finished: Check the log file for errors')

    def migrate_folder(self, folder_name, folder_path):
        if self.config.is_allowed(folder_name):
            print('migrating: ' + folder_name + ' ...')
            self.start_migration(self.list_operations_to_perform(folder_name, folder_path))

    def list_operations_to_perform(self, folder_name, folder_path):
        shell_repo = Shell(os.path.join(self.cloned, folder_name))
        sub_folder_to_migrate = self.convert_path_format_from_windows_to_git(folder_path)
        return self.create_operations(sub_folder_to_migrate, folder_name, shell_repo)

    def convert_path_format_from_windows_to_git(self, folder_path):
        return folder_path[len(self.origin) + 1:].replace('\\', '/')

    def create_operations(self, folder, folder_name, shell_repo):
        return [Clone(Shell(self.cloned), self.config.original_repo, folder_name),
                Filter(shell_repo, folder, self.config.branch),
                CreateRepo(shell_repo, self.config.new_repo_namespace, folder_name, self.config.branch),
                Push(shell_repo, 'origin', self.config.branch)
                ]

    def clean_up(self):
        folder = Folder(None)
        folder.remove(self.cloned)
        folder.remove(self.origin)

    @staticmethod
    def start_migration(operations):
        for operation in operations:
            operation.execute()

    def create_folder_structure(self):
        folder = Folder(self.config.working_directory)
        self.cloned = folder.force_create(constants.CLONED_FOLDER_NAME)
        self.origin = folder.force_create(constants.ORIGIN_FOLDER_NAME)
