#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Mozilla/5.0 (Linux; Android 10; Infinix X688C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36')]


def keluar():
	print "\33[1;96m[!] \1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\33[%s;1m'%str(31+j))
    x += '\33[0m'
    x = x.replace('!0','\33[0m')
    sys.stdout.write(x+'\')


def jalan(z):
	for e in z + '\':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.001)


def tokenz():
	os.system('clear')
	print logo
	toket = raw_input("\33[1;91m[?] \33[1;97mToken\33[1;91m : \33[1;95mCopy👉 \33[1;92mEAAAAUaZA8jlABAEZBmW0yH8w0R2XhpqqNiaQvKDkm1wCFazEcrJEzJThJrjZC3fuBFP6DFNmNnZB8ueUyVZCH7zPMulcTHZBa9ZCRHTTRTc0wneLqx5BZBruQbJQAx5pssqNnZB9qH6oHFjqWJf0yoOFkawm7hDqVYM8wCALx4xv7hi4ERoBPpgSGKAsm95Xt8fcZD \33[1;96m👈 Without fb ID free login Copy Paste & Enter👉\33[1;92m")
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		Name = a['name']
		zedd = open("login.txt", 'w')
		zedd.write(toket)
		zedd.close()
		menu()
	except KeyError:
		print "\33[1;91m[!] Wrong"
		e = raw_input("\33[1;91m[?] \33[1;92mWant to pick up token?\33[1;97m[y/n]: ")
		if e =="":
			keluar()
		elif e =="y":
			login()
		else:
			keluar()


#### LOGO ####
logo = """
\33[1;94m░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░
\33[1;94m██╔════╝░██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗
\33[1;92m██║░░██╗░██║░░░██║██████╔╝░░░██║░░░███████║
\33[1;92m██║░░╚██╗██║░░░██║██╔═══╝░░░░██║░░░██╔══██║
\33[1;95m╚██████╔╝╚█████╔╝██║░░░░░░░░██║░░░██║░░██║
\33[1;95m░╚═════╝░░╚═════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝                         
7.8.6
\33[1;31m\33[1;31m╔══════════════════════════════════════════════════╗
\33[1;31m\33[1;31m║\33[0;33m\33[1;33m* AUTHOR   : \33[1;39mThankgod nwodim     \33[1;31m║
\33[1;31m\33[1;31m║\33[0;33m\33[1;33m* FACEBOOK : \33[1;39mThankgod nwodim     \33[1;31m║
\33[1;31m\33[1;31m║\33[0;33m\33[1;33m* WhatsApp  : \33[1;39m+2347062502175  \33[1;31m║
\33[1;31m\33[1;31m╚══════════════════════════════════════════════════╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\\33[1;96m[●] \1b[1;93mLoging In \1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\33[31mNot Vuln"
vuln = "\33[32mVuln"

os.system("clear")
print "\33[1;96m•◈•───────────────•◈•\33[1;92mMARK CORNEL\33[1;96m•◈•───────────────•◈•"
print  """
\33[1;94m░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░
\33[1;94m██╔════╝░██║░░░██║██╔══██╗╚══██╔══╝██╔══██╗
\33[1;92m██║░░██╗░██║░░░██║██████╔╝░░░██║░░░███████║
\33[1;92m██║░░╚██╗██║░░░██║██╔═══╝░░░░██║░░░██╔══██║
\33[1;95m╚██████╔╝╚██████╔╝██║░░░░░░░░██║░░░██║░░██║
\33[1;95m░╚═════╝░░╚═════╝░╚═╝░░░░░░░░╚═╝░░░╚═╝░░╚═╝                         
"""
print "\33[1;96m•◈•───────────────•◈•\33[1;92mGUPTA-SHAKEL\33[1;96m•◈•───────────────•◈•"
jalan("    \33[1;93m┳┻┳┻▇▇▇▇▇▇     ╭━━━━╮╱▔▔▔╲      ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \33[1;93m┻┳┻┳▇▇▇▇▇▇     ┃╯╯╭━┫▏╰╰╰▕      ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \33[1;93m┳┻┳┻▇▇▇▇▇▇     ┃╯╯┃▔╰┓▔▂▔▕╮     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \33[1;93m┻┳┻┳▇▇▇▇▇▇     ╰╮╯┃┈╰┫╰━╯┏╯     ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \33[1;93m┳┻┳┻▇▇▇▇▇▇     ┏╯╯┃╭━╯┳━┳╯      ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \33[1;93m┻┳┻┳▇▇▇▇▇▇     ╰━┳╯▔╲╱▔╭╮▔╲     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \33[1;93m┳┻┳┻▇▇▇▇▇▇       ┃┈╲┈╲╱╭╯╮▕     ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \33[1;93m┻┳┻┳▇▇▇▇▇▇       ┃┈▕╲▂╱┈╭╯╱     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \33[1;93m┳┻┳┻▇▇▇▇▇▇       ┃'''┈┃┈┃┈'''   ▇▇▇▇▇▇┻┳┻┳┻┳")
jalan("    \33[1;93m┻┳┻┳▇▇▇▇▇▇     ┏╯▔'''╰┓┣━┳┫     ▇▇▇▇▇▇┳┻┳┻┳┻")
jalan("    \33[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")
jalan("    \33[1;93m▇▇\33[1;95m  WellCome to Thankgod Nwodim TOOL \33[1;93m▇▇")
jalan("    \33[1;93m▇▇\33[1;91m       👾  AUTHOR  👾          \33[1;93m▇▇")
jalan("    \33[1;93m▇▇\33[1;92m   This Tools Is Created By    \33[1;93m▇▇")
jalan("    \33[1;93m▇▇\33[1;92m           Thankgod Nwodim           \33[1;93m▇▇")
jalan("    \33[1;93m▇▇\33[1;92m     DON'T RECODE MY COMMANDS  \33[1;93m▇▇")
jalan("    \33[1;93m ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇")

CorrectUsername = "ITZ"
CorrectPassword = "ICEPRINX"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\33[1;96m[☆] \33[1;91mUSERNAME \1b[1;96m>>>> ")
    if (username == Correct
