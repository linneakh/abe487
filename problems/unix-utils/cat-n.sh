#!/bin/bash

set -u

FILE = $1

if [[$# -lt 1]]; then
	printf "Usage: %s 
