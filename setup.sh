if [ $(which espeak) ]
then
	clear
	make ; ./AI
else
	if [ $(whoami) = "root" ]
	then
		sudo apt install espeak
	else
		echo "Please run as root"
		echo "Or manually install espeak."
		exit 0
	fi
fi
make ; ./AI
