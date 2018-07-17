#!/usr/bin -

echo "[+] Required services for archenemy will be loaded."
sudo apt-get update
sudo apt-get upgrade

echo "[+] Installing shodan."
sudo easy_install shodan
sudo easy_install -U shodan

echo "[+] Installing Crypto"
sudo pip install Crypto
