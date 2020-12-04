#!/bin/bash

GREEN=`tput setaf 2`
YELLOW=`tput setaf 3`
RESET=`tput sgr0`
MAGENTA=`tput setaf 5`

read -p "Enter file name: " filename

if [[ ! -f $filename ]]; then
    printf "$YELLOW[ WARN ] File does not exist.$RESET\n"
    exit 1
fi

if [[ ! -r $filename ]]; then
    printf "$YELLOW[ WARN ] File is not readable$RESET\n"
    exit 1
fi

read -p "Enter search string: " searchterm

freq=$(grep -o $searchterm $filename | wc -l)

if [[ $freq == 0 ]]; then
    printf "Search string $GREEN%s$RESET not found in file $GREEN%s$RESET\n" $searchterm $filename
    exit 0
fi

printf "\nTotal Frequency: $MAGENTA%d$RESET\n\n" $freq
printf "%-8s    %s\n" "Line" "Frequency"

# (grep) [line-number]:search-term ->
# (uniq) occurrences [line-number]:search-term ->
# (cut) occurrences [line-number] -> pipe to while
grep -on $searchterm $filename | uniq -c | cut -d : -f 1 |
# Exctract line number and frequency
while read -r line;do
    #echo $line
    tokens=($line)
    # 0-th index is frequency and 1st index is line
    printf "$GREEN%-8s$RESET    $GREEN%s$RESET\n" ${tokens[1]} ${tokens[0]}
done

