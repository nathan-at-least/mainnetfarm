import os
import errno


def ensure_directory_exists(path):
    try:
        os.mkdir(path)
    except os.error as e:
        if e.errno != errno.EEXIST:
            raise
    else:
        print 'Created directory: {!r}'.format(path)
