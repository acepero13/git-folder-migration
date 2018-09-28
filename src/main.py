from io_utils.directory_discover import DirectoryDiscover
from migrator.migrator import Migrator
from shell.shell import Shell

if __name__ == '__main__':
    config = dict()
    config['repo_url'] = 'https://gitlab.com/alvaromoltomedia13/mytestproject.git'
    config['new-repo'] = 'https://gitlab.com/migrator-sorter-tmp/' #TODO: Check valid url / or not /
    config['cwd'] = 'C:\\Users\\amador\\Documents\\Projects\\table-sorter' #TODO: Check valid url / or not /

    cwd = config['cwd'] + '\\origin\\src\\sorter\\'
    dir_discover = DirectoryDiscover(cwd)
    shell = Shell(cwd)
    migrator = Migrator(config, shell, dir_discover)
    migrator.migrate()
