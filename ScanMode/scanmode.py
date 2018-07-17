#!/usr/bin/python -

import os

def main():
	print "\n[+] In Scanning Mode...\n"
	allMode = {}
	genCounter = 1
	directories = os.listdir("./ScanMode")
	allMode[0] = "Exit"
	for name in directories:
		if "." not in name:
			allMode[genCounter] = name
			genCounter = genCounter + 1
	allMode[genCounter] = "MakeBanner"	
	genCounter = 0 
	for key in allMode:
		print "["+str(key)+"] "+allMode[key]
	#choice = raw_input("\nType choice: ")
	choice = 2 		##########hard coded for testing
	print
	if choice != "0":
		os.system("python ./ScanMode/"+allMode[int(choice)]+"/"+allMode[int(choice)].lower()+".py")
	else:
		print "Exiting..."

if __name__ == "__main__":
	main()