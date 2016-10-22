#!/bin/bash
set -eu -o pipefail


function usage_error {
    echo "Usage: $0 ( zcash | bitcoin ) [args...]"
    exit 1
}

if [ $# -gt 0 ]
then
    if [ "$1" = 'zcash' ]
    then
        BASE="$HOME/.mnf-fresh"
        DAEMON="$HOME/zecc/zcash.mainnet-mining/src/zcashd"

    elif [ "$1" = 'bitcoin' ]
    then
        BASE="$HOME/.mnf-bitcoin"
        DAEMON="$HOME/3p/github.com/bitcoin/bitcoin/src/bitcoind"

    else
        usage_error
    fi
else
    usage_error
fi

shift


export PATH="$HOME/tmp/mnfvenv/bin:$PATH"

set -x

pip-reinstall ~/zecc/mainnetfarm/

! [ -d "$BASE" ] || rm -r "$BASE"

mainnetfarm --base "$BASE" init
mainnetfarm --base "$BASE" run --zcashd "$DAEMON" "$@"
