#!/usr/bin/python -

import os
import json

def main():
	fileToScrub = "./data"
	commitMessage = raw_input("[+] Please enter a commit message : ")
	print "[+] Scrubbing "+str(fileToScrub)
	try:
		file = open(fileToScrub,"r")
		jsonData = file.read()
		data = json.loads(jsonData)
		file.close()
		file = open(fileToScrub,"w")
		file.write("")
		file.close()
		os.system("git add --all")
		os.system('git commit -m "'+commitMessage+'"')
		os.system("git push")
		file = open(fileToScrub,"w")
		file.write(json.dumps(data, sort_keys=True, indent=4))
		file.close()
		print "[+] File has been scrubbed...\n"
	except Exception, E:
		print "[-] Error : "+str(E)

if __name__ == "__main__":
	main()
