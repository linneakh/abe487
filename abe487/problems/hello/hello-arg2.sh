#!/bin/bash

set -u

if [[ $# -lt 2 ]]; then
	printf "Usage: %s greeting name\n" $(basename $0)
	exit 1
fi

GREETING=$1
NAME=$2

echo "$GREETING, $NAME!"
