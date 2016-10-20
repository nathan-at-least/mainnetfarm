import os
from mainnetfarm.fs import ensure_directory_exists


BASEPORT = 2953


def initialize(basedir, number):
    ensure_directory_exists(basedir)
    for nodenum in range(number):
        nodename = 'node{:02d}'.format(nodenum)
        nodedir = os.path.join(basedir, nodename)
        init_node(nodedir, nodenum, nodename)


def init_node(nodedir, nodenum, nodename):
    ensure_directory_exists(nodedir)

    confpath = os.path.join(nodedir, 'zcash.conf')
    if os.path.isfile(confpath):
        return

    print 'Writing: {!r}'.format(confpath)

    with file(confpath, 'w') as f:
        def w(tmpl, *a):
            f.write(tmpl.format(*a) + '\n')

        w('onlynet=ipv4')
        w('connect=127.0.0.1:{}', BASEPORT)
        w('bind=127.0.0.1:{}', BASEPORT + 2*nodenum)
        w('rpcbind=127.0.0.1:{}', BASEPORT + 2*nodenum + 1)
        w('rpcuser={}', nodename)
        w('rpcpassword={}',
          os.urandom(32)
          .encode('base64')
          .rstrip()
          .rstrip('='))
        w('gen={}', 1 if nodenum == 0 else 0)
