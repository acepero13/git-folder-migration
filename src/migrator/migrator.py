from commands.git.clone import Clone
from commands.git.filter import Filter
from commands.git.create_repo import CreateRepo
from commands.git.push import Push
from shell.shell import Shell


class Migrator(object):
    def __init__(self, config, shell, dir_discover):
        self.config = config
        self.shell = shell
        self.dir_discover = dir_discover

    def migrate(self):
        Clone(Shell(self.config['initial-cwd']), self.config['repo_url'], self.config['initial-cwd']).execute()
        folders_to_migrate = self.dir_discover.list()
        for folder_path, folder_name in folders_to_migrate:
            shell = Shell(self.config['cwd'])
            shell_repo = Shell(self.config['cwd'] + '\\' + folder_name)
            folder = folder_path[len(self.config['initial-cwd'])+1:].replace('\\', '/')
            operations = [Clone(shell, self.config['repo_url'], folder_name),

                          Filter(shell_repo, folder, folder, 'master'),
                          CreateRepo(shell_repo, self.config['new-repo'], folder_name, 'master'),
                          Push(shell_repo, 'origin', 'master')
                          ]
            self.start_migration(operations)

    def start_migration(self, operations):
        for operation in operations:
            operation.execute()
