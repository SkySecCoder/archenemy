#!/usr/bin/python -s

import shodan
import os
import json

def main():
	
	print "[+] Retrieving API Key..."
	try:
		#SHODAN_API_KEY = readKey()
		#searchFunc(SHODAN_API_KEY)
		readKey()
	except Exception, E:
		print "[-] Could not retrieve Shodan API key..."+str(E)

def searchFunc(shodanKey):
	api = shodan.Shodan(shodanKey)
	try:
        	# Search Shodan
        	results = api.search('apache')
        	# Show the results
        	print 'Results found: %s' % results['total']
        	for result in results['matches']:
                	print 'IP: %s' % result['ip_str']
                	print result['data']
                	print ''
	except shodan.APIError, e:
        	print 'Error: %s' % e

def readKey():
	currDir = os.listdir(".")
	shodanKeyPath = "./"
	choice = "n/a"
	flag = 0
	if ("myshodan.py" in currDir):
		loopbreak = 0
		while loopbreak == 0:
			choice = raw_input("\n[?] It appears that you are using 'myshodan.py' directly, \n    do you want to use the key in current directory? : ")
			if (choice == "y") or (choice == "n"):
				loopbreak = 1
			else:
				print "\n[-] Please enter valid option (y/n): "
		if (choice == 'Y') or (choice == 'y'):
			if ("data" in currDir):
				shodanKey = readDataFile(shodanKeyPath)
			else:
				createDatafile(shodanKeyPath)
				shodanKey = readDataFile(shodanKeyPath)
		else:
			shodanKeyPath = "../../"
			flag = 1
	if (flag == 1):
		print "\n[+] Trying to read 'data' in archenemy root..."
		if "data" not in os.listdir(shodanKeyPath):
			createDatafile(shodanKeyPath)
			shodanKey = readDataFile(shodanKeyPath)
		else:
			shodanKey = readDataFile(shodanKeyPath)
	if ("archenemy.py" in currDir):
		if "data" not in currDir:
			createDatafile(shodanKeyPath)
			shodanKey = readDataFile(shodanKeyPath)
		else:
			shodanKey = readDataFile(shodanKeyPath)
	return shodanKey

def createDatafile(shodanKeyPath):
	newKey = raw_input("[-] The key has not been provided\n[?] Please enter new shodan key : ")
	file = open(shodanKeyPath+"data", "w")
	dataTemplate = {"encryptFlag":["1"], "shodanKey":[newKey]}
	file.write(json.dumps(dataTemplate, sort_keys=True, indent=4))
	file.close()

def readDataFile(shodanKeyPath):
	file = open(shodanKeyPath+"data", "r")
	jsonData = file.read()
	file.close()
	data = json.loads(jsonData)
	if "shodanKey" in data.keys():
		shodanKey = data["shodanKey"][0]
	else:
		print "\n[-] Data file exists but it does not have a 'shodanKey'"
		shodanKey = raw_input("\n[?] Please enter a shodan key : ")
		data["shodanKey"] = [shodanKey]
		file = open(shodanKeyPath+"data", "w")
		file.write(json.dumps(data, sort_keys=True, indent=4))
		file.close()
	return shodanKey	

if __name__ == "__main__":
	main()
