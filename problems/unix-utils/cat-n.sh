#!/bin/bash

set -u


if [[ $# -lt 1 ]]; then
	printf "Usage: %s file \n" $(basename $0)
	exit 1
fi

FILE=$1

if [[ ! -e "$FILE" ]]; then
	echo "\"$FILE\"" is not a file
	exit 1
fi

i=0

while read -r LINE; do
	let i++
	echo $i $LINE 
done < "$FILE"

