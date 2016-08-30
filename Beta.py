#!/usr/bin/python
#Import required libraries
import sys, os
import random
import speech_recognition as sr
#filecheck=os.path.isfile("AI.pl")
filecheck=os.path.isfile("users.dat")
#Check which OS this is running on
OSCheck=sys.platform
#Better define the OS
#win32 is Windows
if OSCheck == "win32":
	OSCheck = "Windows"
#darwin is Mac
elif OSCheck == "darwin":
	OSCheck = "Mac"
#linux2 is Linux
elif OSCheck == "linux2":
	OSCheck = "Linux"
#Make function speak to make speaking faster
def speak( speech ):
	#If the OS is mac, use the speak command
	if OSCheck == "Mac":
		os.system("echo %s | say" %speech)
	#If the OS is Linux, use espeak
	elif OSCheck == "Linux":
		os.system("echo %s | espeak" %speech)
#Make function to determine if input is a question or statement
def question( audio ):
	audio=audio.split()
	if audio[0] == "my":
		is_question=0
	elif audio[0] == "what" or audio[0] == "when":
		is_question=1
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
	if username in contents and os.path.isfile("%s.dat" %username):
		#Open the commands file
		file=open('%s.dat' %username, 'a')
		print("Please use correct grammar(ex: end a question with a question mark!)")
		#Begin a loop
		while True:
			#set the answer to zero
			answer=0
			#Get audio
			speak("How may I help you, %s?" %username)
			r = sr.Recognizer()
			with sr.Microphone() as source:
				audio = r.listen(source)
			#Speech Recognition
			try:
				command=r.recognize_sphinx(audio)
				print(command)
			except sr.UnknownValueError:
				speak("Please try agian, I didn't understand.")
				continue
				
			#Set basic commands
			#Make command lowercase
			command=command.lower()
			#If the command is exit then exit using sys
			if command == "exit":
				sys.exit()
			#If command is bye then exit
			if command == "bye":
				speak("Bye, %s." %username)
				sys.exit()
			#If command is help explain how to use AI
			elif command == "help":
				speak("To tell me about yourself, say a fact about yourself followed by a period. To ask a queston, put a question mark at the end of it.")
			elif command == "list":
				speak("A few example of things you can ask me are: my favorite color, when I was born, and my favorite color.")
			
			#If the command is clear or cls
			elif command == "clear" or command.lower() == "cls":
				#If the OS is Windows use the cls command
				if OSCheck == "win32":
					os.system("cls")
				#If the OS is not Windows, it is probably Mac or Linux
				else:
					os.system("clear")
			#Check if command is a question or statement
			question(command)
			#If a period is in the command, save it to a file
			if is_question == 0 and "my" in command:
				file.write(command.lower())
				file.write("\n")
			#If there is a question mark in the command
			elif  is_question == 1 and "my" in command:
				#Open the file as read only
				readfile=open('%s.dat' %username, 'r')
				#Set it to all lowercase
				query=command
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
				#Check if answer is empty
				if answer == 0:
					speak("I don't believe you told me.")
				else:
					#Take my out of the query
					query=query.split("my", 1)[1]
					#Split the answer after is
					answer=answer.split("is", 1) [1]
					#Return the answer to the user
					speak("Your %s is%s" %(query, answer))
			#If there is a question mark in the command
			elif "?" in command and "your" in command:
				#Open the file as read only
				readfile=open('AI.dat', 'r')
				#Set it to all lowercase
				query=command
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
				#If the answer is empty, say the error
				if answer == 0:
					speak("I haven't thought of that yet.")
				else:
					#Take my out of the query
					query=query.split("my", 1)[1]
					#Split the answer after is
					answer=answer.split("is", 1) [1]
					#Return the answer to the user
					print("My%s is%s" %(query, answer))
				
	else:
		print("You are not a user yet.")
		create=raw_input("Would you like to create a new account y)es or n)o?: ")
		if create == "n":
			sys.exit()
		elif create == "y":
			username=raw_input("What would you like your username to be?: ")
			username=username.lower()
			with open('users.dat', 'a') as file:
				file.write("%s \n" %username)
			with open('%s.dat' %username, 'w') as file:
				file.write("my name is %s. \n" %username)
else:
	print("Welcome to the AquaAI setup.")
	print("No spaces or special characters allowed.")
	#Ask for the username
	username=raw_input("What is your name(all lowercase)?: ")
	#Save the username in lowercase
	username=username.lower()
	#Write the username to a file
	with open('users.dat', 'w') as file:
		file.write("%s \n" %username)
	#Make a new file
	with open('%s.dat' %username, 'w') as file:
		file.write("my name is %s. \n" %username)
	#Define colors
	colors = ['yellow', 'red', 'blue', 'purple', 'orange']
	#Define food
	food = ['electricity', 'RAM', 'CPU']
	#Define letter
	letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	#Generate AI favorites
	with open ('AI.dat', 'w') as file:
	#Write to AI.dat
		#Make favorite color
		file.write("my favorite color is %s. \n" %random.choice(colors))
		#Generate favorite number
		file.write("my favorite number is %s. \n" %random.randint(0,999))
		#Birthday is the original date of when AquaAI was started
		file.write("my birthday is on July 19th. \n")
		#Generate favorite food
		file.write("my favorite food is %s. \n" %random.choice(food))
		#Make favorite OS equal to current OS
		file.write("my favorite os is %s. \n" %OSCheck)
		#Generate favorite letter
		file.write("my favorite letter is %s. \n" %random.choice(letter) )
		#Set name to Aqua
		file.write("my name is Aqua.")
