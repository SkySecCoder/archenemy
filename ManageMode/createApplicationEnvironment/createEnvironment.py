#!/usr/bin/python -
#working

import os

def main():
	print "Welcome to Django Setup"
	os.system("sudo apt-get update -y")
	os.system("sudo apt-get upgrade -y")
	os.system("sudo apt-get install python-pip -y")
	os.system("sudo pip install Django==1.11")
	os.system("sudo apt-get install apache2 -y")
	os.system("sudo apt-get install python-setuptools -y")
	os.system("sudo apt-get install libapache2-mod-wsgi -y")
	os.system("sudo django-admin.py startproject myNAS")
	os.system("sudo mv myNAS /var/www/")
	os.system("mkdir /var/www/logs && touch /var/www/logs/error.log")

	apachedefaultconf = """<VirtualHost *:80>\n\t# The ServerName directive sets the request scheme, hostname and port that\n\t# the server uses to identify itself. This is used when creating\n\t# redirection URLs. In the context of virtual hosts, the ServerName\n\t# specifies what hostname must appear in the request's Host: header to\n\t# match this virtual host. For the default virtual host (this file) this\n\t# value is not decisive as it is used as a last resort host regardless.\n\t# However, you must set it for any further virtual host explicitly.\n\t#ServerName www.example.com\n\n\tServerName mynas.io\n\tServerAlias www.mynas.io\n\tServerAdmin prasad.aakash@gmail.com\n\tDocumentRoot /var/www/myNAS\n\tWSGIScriptAlias / /var/www/myNAS/myNAS/wsgi.py\n\n\t# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,\n\t# error, crit, alert, emerg.\n\t# It is also possible to configure the loglevel for particular\n\t# modules, e.g.\n\t#LogLevel info ssl:warn\n\n\tErrorLog /var/www/logs/error.log\n\tCustomLog /var/www/logs/custom.log combined\n\n\t# For most configuration files from conf-available/, which are\n\t# enabled or disabled at a global level, it is possible to\n\t# include a line for only one particular virtual host. For example the\n\t# following line enables the CGI configuration for this host only\n\t# after it has been globally disabled with "a2disconf".\n\t#Include conf-available/serve-cgi-bin.conf\n</VirtualHost>"""

	file = open("/etc/apache2/sites-available/000-default.conf","w")
	file.write(apachedefaultconf)
	file.close()

	file = open("/etc/apache2/apache2.conf","r")
	apache2conf = file.read()
	apache2conf = apache2conf + "\n" + "WSGIPythonPath /var/www/myNAS"
	file.close()
	file = open("/etc/apache2/apache2.conf","w")
	file.write(apache2conf)
	file.close()
	#sudo cp 000-default.conf /etc/apache2/sites-available/000-default.conf
	os.system("python /var/www/myNAS/manage.py startapp myapp")

	file = open("/var/www/myNAS/myNAS/settings.py","r")
	settingspy = file.read()
	file.close()
	file = open("/var/www/myNAS/myNAS/settings.py","w")
	settingspy = settingspy.replace("'django.contrib.staticfiles',","'django.contrib.staticfiles',\n    'myNAS',")
	file.write(settingspy)
	file.close()
	#sudo cp settings.py /var/www/myNAS/myNAS/settings.py 

	# python manage.py syncdb

	os.system("sudo chmod 755 /var/www/myNAS/")
	os.system("sudo chown www-data /var/www/myNAS/db.sqlite3")
	os.system("sudo chown www-data /var/www/myNAS/")
	os.system("sudo service apache2 start")

if __name__ == "__main__":
	main()