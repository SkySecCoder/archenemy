#!/usr/bin -

echo "[+] Required services for archenemy will be loaded."
sudo apt-get update -y
sudo apt-get upgrade -y

echo "[+] Installing shodan."
sudo apt-get install python-pip
sudo apt-get install python-setuptools
easy_install shodan
easy_install -U shodan

