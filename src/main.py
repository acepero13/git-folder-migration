from configuration.yaml_parser import YamlParser
from io_utils.directory_discover import DirectoryDiscover
from migrator.migrator import Migrator

if __name__ == '__main__':
    config = YamlParser('../resources/hydac.yaml').parse()
    dir_discover = DirectoryDiscover(config.folder_to_discover())
    migrator = Migrator(config, dir_discover)
    migrator.migrate()
