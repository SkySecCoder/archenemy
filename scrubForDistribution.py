#!/usr/bin/python

def main():
	filesToScrub = ["./ScanMode/myshodan/shodanKey.txt"]
	for item in filesToScrub:
		print "[+] Scrubbing "+str(item)
		try:
			file = open(item,"w")
			file.write("")
			file.close()
			print "[+] File has been scrubbed...\n"
		except Exception, E:
			print "[-] Error : "+str(E)

if __name__ == "__main__":
	main()
