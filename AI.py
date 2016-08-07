#Import required libraries
import sys
import os
import random
#filecheck=os.path.isfile("AI.pl")
#Check which OS this is running on
OSCheck=sys.platform
#Check if the file exists
filecheck=os.path.isfile("users.dat")
#If the file exists, ask for a username
if filecheck == 1:
	with open('users.dat', 'r') as file:
		contents=file.read()
	#Ask user for username
	username=raw_input("What is your username?: ")
	#Make the username all upercase
	username=username.upper()
	#Make the username lowercase
	username=username.lower()
	#If the user is in AI.dat and has their own file
	if username.lower() in contents and os.path.isfile("%s.dat" %username):
		#Open the commands file
		file=open('%s.dat' %username, 'a')
		#If the OS is Mac use say
		if OSCheck == "darwin":
			os.system("echo Welcome, %s | say" %username)
		#Begin a loop
		while True:
			print("Welcome %s, how may I help you?" %username)
			#Ask for a command
			command=raw_input("Enter Info or Question: ")
			#Set basic commands
			#If the command is exit then exit using sys
			if command.lower() == "exit":
				sys.exit()
			#If command is help explain how to use AI
			elif command.lower() == "help":
				print("To tell me about yourself, say a fact about yourself followed by a period. To ask about yourself, ask a question followed by a question mark. I am still learning to have my own favorites.")
			#If the command is clear or cls
			elif command.lower() == "clear" or command.lower() == "cls":
				#If the OS is Windows use the cls command
				if OSCheck == "win32":
					os.system("cls")
				#If the OS is not Windows, it is probably Mac or Linux
				else:
					os.system("clear")
				
			#If a period is in the command, save it to a file
			if "." in command.lower() and "my" in command.lower():
				file.write(command.lower())
				file.write("\n")
			#If there is a question mark in the command
			elif "?" in command.lower() and "my" in command.lower():
				#Open the file as read only
				readfile=open('%s.dat' %username, 'r')
				#Set it to all lowercase
				query=command.lower()
				#Spilt the string after the word is
				query=query.split("is ", 1)[1]
				#Cut off the question mark
				query=query.split("?", 1)[0]
				#Search for answer in Commands.dat
				for line in readfile:
					#Cut off the newline
					line=line.rstrip()
					#If the query is in the current line
					if query in line:
						#Set the answer to the current line
						answer=line
						exit
				#Take my out of the query
				query=query.split("my", 1)[1]
				#Split the answer after is
				answer=answer.split("is", 1) [1]
				#Return the answer to the user
				print("Your %s is%s" %(query, answer))
			#If there is a question mark in the command
			elif "?" in command.lower() and "your" in command.lower():
				#Open the file as read only
				readfile=open('AI.dat', 'r')
				#Set it to all lowercase
				query=command.lower()
				#Replace your with my so it can be found.
				query=query.replace("your", "my")
				#Spilt the string after the word is
				query=query.split("is ", 1)[1]
				#Cut off the question mark
				query=query.split("?", 1)[0]
				#Search for answer in Commands.dat
				for line in readfile:
					#Cut off the newline
					line=line.rstrip()
					#If the query is in the current line
					if query in line:
						#Set the answer to the current line
						answer=line
						exit
				#Take my out of the query
				query=query.split("my", 1)[1]
				#Split the answer after is
				answer=answer.split("is", 1) [1]
				#Return the answer to the user
				print("My%s is%s" %(query, answer))
				
		
else:
	print("Welcome to the AquaAI setup.")
	print("No spaces or special characters allowed.")
	#Ask for the username
	username=raw_input("What is your name(all lowercase)?: ")
	#Save the username in lowercase
	username=username.lower()
	#Write the username to a file
	with open('users.dat', 'w') as file:
		file.write("%s" %username)
		file.write("\n")
	with open('%s.dat' %username, 'w') as file:
		file.write("")
	colors = ['yellow', 'red', 'blue', 'purple', 'orange']
	with open ('AI.dat', 'w') as file:
		file.write("my favorite color is %s. \n" %random.choice(colors))
		file.write("my favorite number is %i." %random.randint(0, 999))
