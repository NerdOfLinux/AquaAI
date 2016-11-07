#!/bin/bash

if [ $(which espeak; which swi-prolog) ]
then
	cd ../Aqua-cpp
	make ; ./Aqua; rm a.out
else
	if [ $(whoami) = "root" ]
	then
		sudo apt-add-repository ppa:swi-prolog/stable
		sudo apt-get update
                sudo apt-get install swi-prolog
		sudo apt install espeak
	else
		echo "Please run as root"
		echo "Or manually install espeak and swi prolog."
		exit 0
	fi
fi
