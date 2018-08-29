#!/usr/bin/python -

import sys
import os
import crypt
import getpass

def main():
	choice = raw_input("[1] Encrypt\n[2] Decrypt\n\nChoice : ")
	password = getpass.getpass("[?] Enter password : ")
	initialSalt = generateInitialSalt(password)
	print "[.] Initial Salt = "+initialSalt
	AESkey = generateAESKey(password, initialSalt)
	print "[.] AES key = "+AESkey
	file = open("data","r")
	data = file.read()
	file.close()
	if choice == '1':
		#Encrypting
		enc = os.popen("echo '"+data+"' | openssl enc -nosalt -e -aes-256-cbc -base64 -pass pass:"+AESkey).read()
		print "\n[+] Print ENC data = "+enc
		file = open("data","w")
		file.write(enc)
		file.close
	elif choice == '2':
		#Decrypting
		dec = os.popen("echo '"+data+"' | openssl enc -nosalt -d -aes-256-cbc -base64 -pass pass:"+AESkey).read()
		print "\n[+] Print DEC data = "+dec
		file = open("data","w")
		file.write(dec)
		file.close()
	else:
		print "[-] Wrong Choice..."

def generateInitialSalt(password):
	if len(password) > 8:
		salt = crypt.crypt(password, ("$6$"+password[(len(password)-8):len(password)]))
	else:
		salt = password[len(password)/2:len(password)]
		salt = salt+"vD7sMqYc"
		salt = salt[0:8]
		salt = crypt.crypt(password, ("$6$"+salt))
	salt = salt[12:20]
	return salt

def generateAESKey(password, salt):
	key = ""
	i = 0
	while i < 101:
		i += 1
		genPassword = crypt.crypt(password,("$6$" + salt))
		password = genPassword[12:len(genPassword)]
		salt = password[0:8]
		if i == 100:
			key = password
	return key

if __name__ == "__main__":
	main()
