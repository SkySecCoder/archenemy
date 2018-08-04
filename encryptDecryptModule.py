#!/usr/bin/python -

import os

def main():
	text = "aakashisthebest"
	print "Encrypting text : "+text+"\n"
	key = os.popen("echo '"+text+"' | openssl enc -nosalt -nopad -e -aes-256-cbc -nosalt -base64 -pass pass:aakashtemppassword").read()
	print "Generated key : "+str(key)+"\n"
	print "Decrypting key : "+str(key)+"\n"
	decryptedText = os.popen("echo '"+str(key)+"' | openssl enc -nosalt -nopad -d -aes-256-cbc -nosalt -base64 -pass pass:aakashtemppassword").read()
	print "Decrypted Text : "+str(decryptedText)

if __name__ == "__main__":
	main()