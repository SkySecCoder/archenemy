#!/usr/bin/python - 

import sys
import os

def main():
	print "\n[+] Entering Manage Mode...\n"
	allMode = {}
	genCounter = 1
	directories = os.listdir("./ManageMode")
	allMode[0] = "Exit"
	for name in directories:
		if '.' not in name:	
			allMode[genCounter] = name
			genCounter = genCounter + 1
	genCounter = 0 
	for key in allMode:
		print "["+str(key)+"] "+allMode[key]
	choice = raw_input("\nType choice: ")
	if choice != "0":
		os.system("python ./ManageMode/"+allMode[int(choice)]+"/"+allMode[int(choice)].lower()+".py")
	else:
		print "Exiting..."

if __name__ == "__main__":
	main()