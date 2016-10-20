import os
import re
import subprocess


NAME_RGX = re.compile(r'node(\d{2})')


def run(basedir, zcashd):

    pw = ProcWaiter()

    debuglogs = []

    for n in os.listdir(basedir):
        path = os.path.join(basedir, n)
        m = NAME_RGX.match(n)
        if m is None:
            print 'Unexpected junk: {!r}'.format(path)
            continue

        pw.spawn(n, zcashd, '-datadir={}'.format(path))

        debuglogs.append(os.path.join(path, 'debug.log'))

    #pw.spawn('tail', 'tail', '-F', *debuglogs)
    pw.wait_for_all()


class ProcWaiter (object):
    def __init__(self):
        self.procs = {}

    def spawn(self, name, *args):
        print 'Launching {}: {!r}'.format(name, args)
        proc = subprocess.Popen(args)
        self.procs[proc.pid] = name

    def wait_for_all(self):
        while self.procs:
            (pid, status) = os.waitpid(0, 0)
            name = self.procs.pop(pid)
            print '{} exited with status: {!r}'.format(
                name,
                status
            )
