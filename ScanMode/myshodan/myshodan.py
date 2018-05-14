#!/usr/bin/python

import shodan

def main():
        print "[+] Retrieving API Key..."
	try:
		file = open("shodanKey.txt","r")
		for line in file.readlines():
			SHODAN_API_KEY = str(line.strip("\n"))
		file.close()
		print "[+] Retrieved latest API Key..."
		searchFunc(SHODAN_API_KEY)
	except Exception, E:
		print "[-] Could not retrieve Shodan API key..."+str(E)

def searchFunc(shodanKey):
	api = shodan.Shodan(shodanKey)
	try:
        	# Search Shodan
        	results = api.search('apache')
        	# Show the results
        	print 'Results found: %s' % results['total']
        	for result in results['matches']:
                	print 'IP: %s' % result['ip_str']
                	print result['data']
                	print ''
	except shodan.APIError, e:
        	print 'Error: %s' % e

if __name__ == "__main__":
	main()
