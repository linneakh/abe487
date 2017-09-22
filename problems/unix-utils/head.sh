#!/bin/bash

set -u

if [[ $# -lt 1 ]]; then
	printf "Usage: %s FILE [NUM]\n" $(basename $0)
	exit 1
fi

FILE=$1
HEAD=${2:-3}

if [[ ! -e "$FILE" ]]; then
	echo "\"$FILE\"" is not a file
	exit 1
fi

i=0
while [ $i -lt $HEAD ] && read -r LINE ; do
		let i++
		printf "%s\n" "$LINE"
done < "$FILE"
