#!/bin/bash

GREEN=`tput setaf 2`
RESET=`tput sgr0`

if [[ ! -f $1 ]]; then
    echo "File does not exist"
    exit 1
fi

blocks=$(stat --format=%b $1)

printf "%s occupies $GREEN%d$RESET blocks.\n" "$1" ${blocks}
#df $1
