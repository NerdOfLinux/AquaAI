import sys
import os
#filecheck=os.path.isfile("AI.pl")
filecheck=os.path.isfile("AI.dat")
if filecheck == 1:
	with open('AI.dat', 'r') as file:
		contents=file.read()
	username=raw_input("What is your username?: ")
	if username in contents and os.path.isfile("%s.pl" %username):
		print("Welcome %s, how may I help you?" %username)
		command=raw_input("Enter Command: ")
else:
	print("Welcome to the AquaAI setup.")
	print("No spaces or special characters allowed.")
	username=raw_input("What is your name?: ")
	username=username.lower()
	print("Hello, %s, please answer a few questions about yourself:" %username)
	color=raw_input("What is your favorite color?: ")
	birthday=raw_input("When is your birthday (month/day in numbers)?: ")
	with open('AI.dat', 'w') as file:
		file.write("%s" %username)
		file.write("\n")
	with open('%s.pl' %username, 'w') as file:
		file.write("favoritecolor(%s)." %color)
		file.write("\n")
		file.write("birthday(%s)." %birthday)
