import sys
import os
#filecheck=os.path.isfile("AI.pl")
filecheck=0
if filecheck == 1:
	file=open('AI.dat', 'r')
	username=raw_input("What is your username?: ")
	if username in file and os.path.isfile("%s.pl" %username):
		print("Welcome %s, how may I help you?" %username)
		command=raw_input("Enter Command: ")
else:
	print("Welcome to the AquaAI setup.")
	username=raw_input("What is your name?: ")
	while " " or "-" in username:
		print("No spaces or special characters allowed!!!")
		username=raw_input("What is your name?: ")
	print("Hello, %s, please answer a few questions about yourself:" %username)
	color=raw_input("What is your favorite color?: ")
	birthday=raw_input("When is your birthday (month/day in numbers)?: ")
	with open('AI.dat', 'w') as file:
		file.write("%s" %username)
	with open('%s.pl', 'w' %username) as file:
		file.write("favoritecolor(%s)." %color)
		file.write("birthday(%s)." %birthday)
