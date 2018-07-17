#!/usr/bin/python - 

import sys
import os
import socket
import getpass
 
def main():
	miniBanner()
	makeChoice()

def makeChoice():
	allMode = {}
	genCounter = 2
	directories = os.listdir("./")
	allMode[0] = "Exit"
	allMode[1] = "Install Dependencies"
	for name in directories:
		if name[(len(name)-4):len(name)] == "Mode":	
			allMode[genCounter] = name
			genCounter = genCounter + 1
	allMode[genCounter] = "MakeBanner"	
	genCounter = 0 
	for key in allMode:
		print "["+str(key)+"] "+allMode[key]
	#choice = raw_input("\nType choice: ")
	choice = 4 ##########hard coded for testing
	if choice == 0:
		print "[+] Exiting..."
	elif choice == 1:
		os.system("sudo bash loadAllServices.sh")
	elif (choice > 1) and (choice < 6):
		os.system("python ./"+allMode[int(choice)]+"/"+allMode[int(choice)].lower()+".py")
	else:
		print "[-] Exiting due to wrong option..."

def miniBanner():
	try:
		localIP = socket.gethostbyname(socket.gethostname())
		username = getpass.getuser()
		hostname = socket.gethostname()
		cwd = os.getcwd()
		print "\n"+"System information:\n\n"+"System IP address:"+ localIP + "   \nCurrent user:" + username + "   \nHostname:" + hostname + "   \nCurrent working directory:" + cwd
	except:
		pass
	welcomeMsg = ["Welcome to Archenemy", "Version 1.0 ", "Choose a mode "]
	widthOfMsg = 35 # Adjusting width of welcome message
	print "\n",
	for msg in welcomeMsg:
		print "        ~[ "+msg,
		if len(msg) < widthOfMsg:
			numOfSpace = ((widthOfMsg - len(msg))/2)
			while numOfSpace != 0:
				print " ",
				numOfSpace = numOfSpace - 1
			print "]~"
	print "\n",
	

if __name__ == "__main__":
	main()