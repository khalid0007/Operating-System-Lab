#!/bin/bash

tot_files=$(find . -type f | wc -l)

echo "Total files in curr dir: " $tot_files

echo -e "\nFile info for subdirectories:\n"

find . -mindepth 1 -maxdepth 1 -type d -print0 |
while read -r -d '' line; do
    echo $line "->" $(find "$line" -maxdepth 1 -type f | wc -l) "file(s)"
    find "$line" -mindepth 1 -maxdepth 1 -type f -print0 |    
    while read -r -d '' filename; do
        echo -e "\t" $filename
    done
done

echo -e "\nFile created between 2018 and 2020: \n"
find . -type f -mtime -3 -name "*" -newermt 2018-01-01 ! -newermt 2019-12-31 -print0 |
while read -r -d '' filename; do
    echo -e $filename
done
