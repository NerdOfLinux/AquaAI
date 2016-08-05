#Import required libraries
import sys
import os
#filecheck=os.path.isfile("AI.pl")
#Check if the file exists
filecheck=os.path.isfile("AI.dat")
#If the file exists, ask for a username
if filecheck == 1:
	with open('AI.dat', 'r') as file:
		contents=file.read()
	username=raw_input("What is your username?: ")
	#If the user is in AI.dat and has their own file
	if username in contents and os.path.isfile("%s.pl" %username):
		#Open the commands file
		file=open('Commands.dat', 'a')
		#Begin a loop
		while True:
			print("Welcome %s, how may I help you?" %username)
			#Ask for a command
			command=raw_input("Enter Command: ")
			#If the word my or i is in the command, save it to a file
			if "my" or "i" in command.lower():
				file.write(command.lower())
				
		
else:
	print("Welcome to the AquaAI setup.")
	print("No spaces or special characters allowed.")
	#Ask for the username
	username=raw_input("What is your name(all lowercase)?: ")
	#Save the username in lowercase
	username=username.lower()
	print("Hello, %s, please answer a few questions about yourself:" %username)
	#Get the user's favorite color
	color=raw_input("What is your favorite color?: ")
	#Get the user's birthday
	birthday=raw_input("When is your birthday (month/day in numbers)?: ")
	#Write the username to a file
	with open('AI.dat', 'w') as file:
		file.write("%s" %username)
		file.write("\n")
	#Write user information to a prolog file
	with open('%s.pl' %username, 'w') as file:
		file.write("favoritecolor(%s)." %color)
		file.write("\n")
		file.write("birthday(%s)." %birthday)
	with open('Commands.dat', 'w') as file:
		file.write("")
