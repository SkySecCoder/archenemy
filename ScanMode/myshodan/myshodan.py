#!/usr/bin/python -s

#import shodan
import os
import json
import base64
import Crypto

dataEncrypted = 0

def main():
	shodanKey = decryptKey()
	print shodanKey
	'''
	print "[+] Retrieving API Key..."
	try:
		file = open("shodanKey.txt","r")
		for line in file.readlines():
			SHODAN_API_KEY = str(line.strip("\n"))
		file.close()
		print "[+] Retrieved latest API Key..."
		searchFunc(SHODAN_API_KEY)
	except Exception, E:
		print "[-] Could not retrieve Shodan API key..."+str(E)
	'''

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

def decryptKey():
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
				shodanKey = decryptReadDataFile(shodanKeyPath)
			else:
				decryptCreateDataFile(shodanKeyPath)
				shodanKey = decryptReadDataFile(shodanKeyPath)
		else:
			shodanKeyPath = "../../"
			flag = 1
	if (flag == 1):
		print "\n[+] Trying to read 'data' in archenemy root..."
		if "data" not in os.listdir(shodanKeyPath):
			decryptCreateDataFile(shodanKeyPath)
			shodanKey = decryptReadDataFile(shodanKeyPath)
		else:
			shodanKey = decryptReadDataFile(shodanKeyPath)
	if ("archenemy.py" in currDir):
		if "data" not in currDir:
			decryptCreateDataFile(shodanKeyPath)
			shodanKey = decryptReadDataFile(shodanKeyPath)
		else:
			decryptReadDataFile(shodanKeyPath)
	return shodanKey

def decryptCreateDataFile(shodanKeyPath):
	newKey = raw_input("[-] The key has not been provided\n[?] Please enter new shodan key : ")
	file = open(shodanKeyPath+"data", "w")
	newKey = encryptKey(newKey)
	dataTemplate = {"encryptFlag":["1"], "shodanKey":[newKey]}
	file.write(json.dumps(dataTemplate, sort_keys=True, indent=4))
	file.close()

def decryptReadDataFile(shodanKeyPath):
	file = open(shodanKeyPath+"data", "r")
	jsonData = file.read()
	file.close()
	data = json.loads(jsonData)
	if "shodanKey" in data.keys():
		shodanKey = data["shodanKey"][0]
	else:
		print "\n[-] Data file exists but it does not have a 'shodanKey'"
		shodanKey = raw_input("\n[?] Please enter a shodan key : ")
		shodanKey = encryptKey(shodanKey)
		data["shodanKey"] = [shodanKey]
		file = open(shodanKeyPath+"data", "w")
		file.write(json.dumps(data, sort_keys=True, indent=4))
		file.close()
	return shodanKey	

def encryptKey(toEncrypt):
	key = raw_input("[+] Please enter a key to unlock the data file : ")
	key = SHA256.new(key).digest()
	IV = Random.new().read(AES.block_size)  # generate IV
	encryptor = AES.new(key, AES.MODE_CBC, IV)
	padding = AES.block_size - len(toEncrypt) % AES.block_size  # calculate needed padding
	toEncrypt += bytes([padding]) * padding  # Python 2.x: source += chr(padding) * padding
	data = IV + encryptor.encrypt(toEncrypt)  # store the IV at the beginning and encrypt
	encryptedKey = base64.b64encode(data).decode("latin-1") if encode else data
	return encryptedKey

if __name__ == "__main__":
	main()
