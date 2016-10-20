from mainnetfarm.fs import ensure_directory_exists


def initialize(basedir, zcashcli, number):
    ensure_directory_exists(basedir)
    for nodenum in range(number):
        raise NotImplementedError()
