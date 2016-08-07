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
		#Begin a loop
		while True:
			print("Welcome %s, how may I help you?" %username)
			#Ask for a command
			command=raw_input("Enter Command: ")
			#Set basic commands
			#If the command is exit then exit using sys
			if command.lower() == "exit":
				sys.exit()
			elif command.lower() == "help":
				print("To tell me about yourself, say a fact about yourself followed by a period. To ask about yourself, ask a question followed by a question mark. I am still learning to have my own favorites.")
				
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
				print("Your %s is %s" %(query, answer))
				
		
else:
	print("Welcome to the AquaAI setup.")
	print("No spaces or special characters allowed.")
	#Ask for the username
	username=raw_input("What is your name(all lowercase)?: ")
	#Save the username in lowercase
	username=username.lower()
	#print("Hello, %s, please answer a few questions about yourself:" %username)
	#Get the user's favorite color
	#color=raw_input("What is your favorite color?: ")
	#Get the user's birthday
	#birthday=raw_input("When is your birthday (month/day in numbers)?: ")
	#Write the username to a file
	with open('AI.dat', 'w') as file:
		file.write("%s" %username)
		file.write("\n")
	#Write user information to a prolog file
	#with open('%s.pl' %username, 'w') as file:
	#	file.write("favoritecolor(%s)." %color)
	#	file.write("\n")
	#	file.write("birthday(%s)." %birthday)
	with open('%s.dat' %username, 'w') as file:
		file.write("")
