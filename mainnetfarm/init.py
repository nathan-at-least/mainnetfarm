import os
import random
from mainnetfarm.fs import ensure_directory_exists


BASEPORT = random.randrange(1024, 2**16)


def initialize(basedir, number, testnet):
    ensure_directory_exists(basedir)
    for nodenum in range(number):
        nodename = 'node{:02d}'.format(nodenum)
        nodedir = os.path.join(basedir, nodename)
        init_node(nodedir, number, nodenum, nodename, testnet)


def init_node(nodedir, nodecount, nodenum, nodename, testnet):
    ensure_directory_exists(nodedir)

    confpath = os.path.join(nodedir, 'zcash.conf')

    print 'Overwriting: {!r}'.format(confpath)

    baseports = [BASEPORT + 2*i for i in range(nodecount)]

    with file(confpath, 'w') as f:
        def w(tmpl, *a):
            f.write(tmpl.format(*a) + '\n')

        w('onlynet=ipv4')

        myport = BASEPORT + 2*nodenum
        if nodenum == 0:
            for otherport in baseports:
                if otherport != myport:
                    w('connect=127.0.0.1:{}', otherport)
        else:
            w('dnsseed=0')

        w('bind=127.0.0.1')
        w('port={}', myport)
        w('rpcbind=127.0.0.1')
        w('rpcport={}', BASEPORT + 2*nodenum + 1)
        w('rpcuser={}', nodename)
        w('rpcpassword={}',
          os.urandom(32)
          .encode('base64')
          .rstrip()
          .rstrip('='))
        w('gen={}', 1 if nodenum == 0 else 0)
        w('debug=pow')

        if testnet:
            w('testnet=1')
