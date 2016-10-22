#!/bin/bash
if [ $(which espeak) ]
then
	clear
	make ; ./AI; rm a.out
else
	if [ $(whoami) = "root" ]
	then
		sudo apt install espeak
		sudo apt-add-repository ppa:swi-prolog/stable
                sudo apt-get install swi-prolog
		sudo apt-get update
	else
		echo "Please run as root"
		echo "Or manually install espeak."
		exit 0
	fi
fi
