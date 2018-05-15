#!/usr/bin/python

import optparse
import sys
import zipfile
import crypt
from termcolor import colored

def main():
	parser = optparse.OptionParser("usage %prog [-z <zipfile> -d <dictionary>][-b <hashfile> -d <dictionary>]")
	parser.add_option('-z', dest='zname', type='string',help='Specify zip file')
	parser.add_option('-d', dest='dname', type='string',help='Specify dictionary file')
	parser.add_option('-b', dest='bname', type='string',help='Specify the file name that contains the hashes to be cracked')
	#parser.add_option('-x', dest='xname', type='string',help='To generate your own hash')
	(options, args) = parser.parse_args()
	if ((options.dname == None) & (options.zname == None)) | ((options.dname == None) & (options.bname ==None)):
		makeBanner("HashBrown")
		print "\n1. Hash breaking\n2. Generate hash\n3. Extract Zip file"
		choice=raw_input("\nEnter your choice(1-3): ")
		if str(choice)=="1":	
			filename = raw_input(colored("\nEnter the file that contains user's name and hashes: ","green"))
			dname = raw_input(colored("Enter the file that contains possible passwords: ","green"))	
			crack(filename,dname)
		elif str(choice)=="2":
			genHash()
		else:
			print			
			zname = raw_input(colored("\nEnter the name of the zip file (example: example.zip): ","green"))
			dname = raw_input(colored("Enter the name of the file that contains password list: ","green"))
			#zipopener("test.zip","dictionary.txt")
			zipopener(zname,dname)
	elif (options.bname == None):
		zname = options.zname
		dname = options.dname
		zipopener(zname,dname)
	else:
		dname = options.dname
		bname = options.bname
		crack(bname,dname)
	print "\n[*] Exiting..."

def zipopener(ftoopen,passfile):
	file=open(passfile,"r")
	print "\n["+colored("***","green")+"]Using passwords from "+colored(passfile,"green")+" to crack the zip file "+colored(ftoopen,"green")+"\n"
	for line in file.readlines():
		line=line.strip('\n')
		line=line.strip(" ")
		try:
			zfile=zipfile.ZipFile(str(ftoopen))
        		zfile.extractall(pwd=str(line))
			print "\n\n["+colored("+","green")+"] File successfully extracted with password "+colored(line,"green")
			return 0
		except Exception,e:
			print "["+colored("-","red")+"] Error for password "+colored(line,"red")+": "+str(e)

############################################################################################
def crack(filename,dname):
	print "\n["+colored("***","green")+"]Using passwords from "+colored(dname,"green")+" to crack the hash file "+colored(filename,"green")+"\n"
	file=open(filename,"r")
	for list in file.readlines():
		user=list.split(":")[0]
		hash = list.strip(user+":")
		crack2(hash,user,dname)

def crack2(hash,user,dname):
	type=hash[1:2]
	salt=hash[0:11]
	hash1 = hash.strip("$"+type)
	hash1 = hash1.strip("$"+salt)
	filename=dname#"dictionary.txt"
	f=open(filename,"r")
	for word in f.readlines():
		word=word.strip("\n")
		word=word.strip(" ")
		#temp=hashlib.sha512(word).hexdigest()
		temp= crypt.crypt(word,salt)
		comp = str(temp)
		if comp in hash:
			print "["+colored("+","green")+"] Password match found for "+colored(user,"green")+": "+colored(word,"green")
			if str(type)=="6":
        	        	print "	This is SHA512"
			elif str(type)=="5":
				print"	This is SHA256"
			elif str(type)=="2a":
				print "	This is Blowfish"
			else:
				print "	This is MD5"
			return
	print "["+colored("-","red")+"] Password match not found for "+colored(user,"red")
############################################################################################

def genHash():
	salt = raw_input(colored("\nEnter salt for your SHA512 hash(must be 8 characters): ","green"))
	toHash = raw_input(colored("Enter string to be hashed: ","green"))
	if len(salt) < 8:
		print "\n["+colored("-","red")+"] Salt is too small, please make sure it is 8 characters long."
		return 0	
	salt = salt[0:8]
	Hash = crypt.crypt(toHash,("$6$"+salt))
	print "\n["+colored("***","green")+"]Generating Hash:"
	print "\n["+colored("+","green")+"] Salt used for your hash is: "+colored(salt,"green")
	print "["+colored("+","green")+"] Hashed string: "+colored(toHash,"green")
	print "["+colored("+","green")+"] Hash Value: "+colored(Hash,"green")

def makeBanner(name):
    i=j=0
    while j!= 15:
        if j==0 or j==14:
            while i != 40:
                if i==0:
                    print "*",
                elif i==39:
                    print "*"
                else:
                    print "=",
                i = i+1
        i = 0
        if j>0 and j<12:
            if j == 7:
                k = 30
            elif j == 6:
                k = 40 - len(name) + 5
            else:
                k = 40
            while i != k:
                if i == 0:
                    print "|",
                elif i == k-1:
                    print "|"
                elif i == k/2 and j == 7:
                    print "- by SkySecCoder     ",
                elif i == k/2 and j == 6:
                    print name,
                else:
                    print " ",
                i = i + 1
        j = j + 1


if __name__=="__main__":
	main()
