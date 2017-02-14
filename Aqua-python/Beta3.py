#Import required libraries
import sys
import os
import subprocess
#Get OS name
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
#If OS is not Mac or Linux
if OSCheck != "Linux" and OSCheck != "Mac":
    #Print error and exit
    print("Sorry, this program requires Mac or a Linux Distro")
    sys.exit()
#Check if file exists
if os.path.isfile("Data.py") != True:
    #Create the file
    with open("Data.py", "w") as datafile:
        #Put text in file
        datafile.write("#Do NOT edit this data file.\n")
    #Add to file
    with open("Data.py", "a") as datafile:
        datafile.write("import sys \n")
        datafile.write("command=sys.argv[1] \n")
#Else
else:
    #Begin a loop
    while True:
        #Get user command into string
        command=input("How may I help you?: ")
        response=subprocess.check_output("python Data.py \"%s\""%(command), shell=True)
        #If result is blank
        if response == "":
            print("I don't know the answer to that.")
            answer=input("What is the correct response?: ")
            #Write if statement to file
            with open("Data.py", "a") as datafile:
                datafile.write("if command == \"%s\": \n"%(command))
                #Write response to file
                datafile.write("    print(\"%s\")\n"%(answer))
        #Else
        else:
            #Print the answer
            print(response)
            
