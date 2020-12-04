#!/bin/bash

GREEN=`tput setaf 2`
MAGENTA=`tput setaf 5`
YELLOW=`tput setaf 3`
RED=`tput setaf 1`
RESET=`tput sgr0`
BOLD=`tput bold`

function disp_prompt() {
    printf "${GREEN}BCSE-III@ $1$ $RESET "
}

function newfolder() 
{
	if [ $# -eq 0 ]
	then 
		echo "${RED}[ Error ]${RESET} No argument provided. Please enter only one argumnent"
	elif [ $# -gt 1 ]
	then 
		echo "${RED}[ Error ]${RESET} Please enter only one argument"
	else
		if [ ! -d "$1" ]; then
			mkdir "$1"
			echo "${GREEN}[ SUCCESS ]${RESET} $1 : Directory successfully created"
		else
			echo -e "${RED}[ Error ]${RESET} $1 is the name of already existing directory!"
		fi
	fi
}

function editfile() 
{
	if [ $# -eq 0 ]
	then
		echo "${YELLOW}[ WARNING ]${RESET} No filename provided creating a new one!"
		nano
	elif [ $# -gt 1 ]
	then 
		echo "${RED}[ Error ]${RESET} Please enter only one argument"
	else
		nano "$1"
	fi 
}


function getinfo()
{
	filepath=$( realpath "$1" )
	filesize=$( stat --printf="%s" "$1" )
	lastdate=$( stat -c %y "$1" )
	creatorname=$( stat -c '%U' "$1" )

	echo "Path of the file       : ${MAGENTA}$filepath${RESET}"
	echo "Size of the file       : ${MAGENTA}$filesize${RESET}"
	echo "Last modification date : ${MAGENTA}$lastdate${RESET}"
	echo "Name of the creator    : ${MAGENTA}$creatorname${RESET}"
}

function info()
{
	if [ $# -eq 0 ]
	then 
		getinfo .
	elif [ ! -e "$1" ]
	then
		echo "Error : File does not exist."
	elif [ $# -gt 1 ]
	then
		echo "Error : Please enter only one argument"
	else 
		getinfo "$1"
	fi
}

function exitbcse() 
{
	echo "${YELLOW}[ WARNING ]${RESET} Exiting from JUBCSEIII shell"
}

function getmessage() 
{
    curtime=$(date +%H:%M )
    if [[ "$curtime" > "00:01" ]] && [[ "$curtime" < "12:00" ]]; then
	message="Morning"
    elif [[ "$curtime" > "12:01" ]] && [[ "$curtime" < "18:00" ]]; then
        message="Afternoon"
    elif [[ "$curtime" > "18:01" ]] && [[ "$curtime" < "00:00" ]]; then
        message="Evening"	
    else
    	message="Day"
    fi
    echo "${GREEN}Hi! Good $message                                             Time : $curtime${RESET}"
}


function intro()
{
    banner "BCSEIII-20"
    echo "----------------------------BCSEIII-2020 Shell-----------------------------"
    getmessage
    echo "newfolder <directoryname>              ${MAGENTA}(Create a new directory)${RESET}"
    echo "editfile [filename]                    ${MAGENTA}(Open existing/new file in vi editor)${RESET}"
    echo "info [filename]                        ${MAGENTA}(Display information about the file)${RESET}"
    echo "exitnewshell                           ${MAGENTA}(Exit from JUBCSEIII shell)${RESET}"
    echo "----------------------------------------------------------------------------"
    echo
}




function main()
{
	#intoduction
	intro
	#get user
	user=$(whoami)
	#Command loop
	while true; do
	    disp_prompt "${user}"
	    read command filename
	    if [ "$command" == "newfolder" ]; then
	 	newfolder $filename
	    elif [ "$command" == "editfile" ]; then
		editfile $filename
	    elif [ "$command" == "info" ]; then
		info $filename
 	    elif [ "$command" == "exitnewshell" ]; then
		exitbcse
		break
	    else
		echo "${RED}[ ERROR ]${RESET} $command: Command not found!"
	    fi
	done
}


# Main program
clear
main
