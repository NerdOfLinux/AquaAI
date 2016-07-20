import sys
import os
filecheck=os.path.isfile("AI")
if filecheck == 1:
	print("Hello")
else:
	print("Welcome to the AquaAI setup.")
	username=raw_input("What is your name?: ")
	print("Hello, %s, please answer a few questions about yourself:" %username)
	color=raw_input("What is your favorite color?: ")
	birthday=raw_input("When is your birthday (month/day in numbers)?: ")