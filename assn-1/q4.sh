#!/bin/bash

# console customization
YELLOW=`tput setaf 3`
GREEN=`tput setaf 2`
RED=`tput setaf 1`
BLUE=`tput setaf 4`
RESET=`tput sgr0`

if [[ $# > 0 ]]; then
    printf "$BLUE%-15s%-10s%-10s%-10s\n$RESET" "File" "printf" "scanf" "int"
    for file in "$@"; do
        if [[ ! -f $file ]]; then
            printf "$RED%-15s%s\n$RESET" $file "$YELLOW[WARN] File does not exist$RESET"
            continue
        fi
	    printfCount=$(grep -o "printf(" $file | wc -l)
	    scanfCount=$(grep -o "scanf(" $file | wc -l)
	    intCount=$(grep -o "int " $file | wc -l)
	    printf "$GREEN%-15s%-10s%-10s%-10s\n$RESET" $file $printfCount $scanfCount $intCount
    done
else
    printf "$YELLOW[WARN] Insufficient arguments$RESET\n"
fi

