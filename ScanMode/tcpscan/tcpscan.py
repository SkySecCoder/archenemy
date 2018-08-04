#!/usr/bin/python - 

import sys
import os
import socket

def main():
	returnedip = getlocalip()
	temp = returnedip.split('.')
	iprangetoscan = temp[0]+"."+temp[1]+"."+temp[2]+"."
	i = 1
	while i < 255:
		myip = iprangetoscan+str(i)
		i += 1
		socket.setdefaulttimeout(3)
		s = socket.socket()
		s.connect((myip,22))
		buff = s.recv(1024)
		print "[+] Scanned "+myip+": "+buff
		s.close

def getlocalip():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	myip = s.getsockname()[0]
	s.close()
	return myip

if __name__ == "__main__":
	main()