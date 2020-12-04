#!/bin/bash

NUMBER=^[-+]?[0-9]+\.?[0-9]*$

read -p "Enter v: " v

if [[ $v =~ NUMBER ]]; then
    echo $v "is a number"
else
    echo $v "is not a number"
fi
