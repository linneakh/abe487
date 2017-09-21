#!/bin/bash

set -u

if [[ $# -lt 1 ]]; then
	printf "Usage: %s name\n" $(basename $0)
	exit 1
fi

NAME=$1

echo Hello, $NAME!

