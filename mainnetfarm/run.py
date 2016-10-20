import os
import re
import subprocess


NAME_RGX = re.compile(r'node(\d{2})')


def run(basedir, zcashcli):

    procs = {}

    for n in basedir:
        path = os.path.join(basedir, n)
        m = NAME_RGX.match(n)
        if m is None:
            print 'Unexpected junk: {!r}'.format(path)
            continue

        args = [zcashcli, '-datadir={}'.format(path)]
        print 'Launching {}: {!r}'.format(n, args)
        proc = subprocess.Popen(args)
        procs[proc.pid] = n

    while procs:
        (pid, status) = os.waitpid(0, 0)
        print '{} exited with status: {!r}'.format(procs.pop(pid), status)
