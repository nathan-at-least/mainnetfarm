import os
import sys
import argparse
from mainnetfarm.init import initialize
from mainnetfarm.run import run


def main(args=sys.argv[1:]):
    '''zc fr tool'''
    opts = parse_args(args)
    opts.cmdfunc(opts)


def parse_args(args):
    p = argparse.ArgumentParser(description=main.__doc__)

    p.add_argument('--base',
                   dest='BASEDIR',
                   type=str,
                   default=os.path.expanduser('~/.mainnetfarm'),
                   help='Path to zcash-cli.')

    subs = p.add_subparsers(title='subcommands')
    for n, v in globals().iteritems():
        if n.startswith('cmd_'):
            cmdname = n[4:].replace('_', '-')
            subp = subs.add_parser(cmdname, description=v.__doc__)
            cmdfunc = v(subp)
            subp.set_defaults(cmdfunc=cmdfunc)

    return p.parse_args(args)


def cmd_init(subp):
    '''initialize.'''
    subp.add_argument('--number',
                      dest='NUMBER',
                      type=int,
                      default=3,
                      help='Number of nodes to create.')

    def cmdfunc(opts):
        initialize(opts.BASEDIR, opts.NUMBER)

    return cmdfunc


def cmd_run(subp):
    '''run.'''
    subp.add_argument('--zcash-cli',
                      dest='ZCASHCLI',
                      type=str,
                      default='./src/zcash-cli',
                      help='Path to zcash-cli.')

    def cmdfunc(opts):
        run(opts.BASEDIR, opts.ZCASHCLI)

    return cmdfunc
