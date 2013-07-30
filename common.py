#!/usr/bin/python
#filename=common.py

import os
import sys
import tarfile
import socket
import string
import subprocess
import random
import time

Lid=[]
num=1

@classmethod
def downloadfile(urladdress):
#	urladdress="wget -q"+urladdress
        purduesquid="http://squid.rcac.purdue.edu"
	purduename="purdue.edu"
	numgetretries=3
	osgsqquid=os.getenv("OSG_SQUID_LOCATION")
	print "osg squid is set to:"+str(osgsquid
	hostname=socket.gethostname()
	print "hostname is set to:"+str(hostname)
	#if 
	if string.find(hostname,purduename)>=0:
		os.putenv("http_proxy",purduesquid)
	elif osgsquid != None and string.find(osgsquid.upper(),"UNAVAILABLE")<0:
		os.putenv("http_proxy",osgsquid)
	else:
		os.unsetenv("http_proxy")

 	successdownload=False
	print "using proxy: "+str(os.getenv("http_proxy"))
	print "Max Download trials is: "+str(numgetretries)
	
	#try to download three times from http_proxy	
	for i in range(numgetretries):
		print "Trial #: "+str(i)
		child=subprocess.Popen(["wget","-q",urladdress],shell=True)
		child.wait()
		returncode=child.poll()
		if returncode ==0:
			successdownload ==1
			break
		else:
                        #after sleepfor second, try to download again
			timeofsleep=(random.random())*180
			time.sleep(timeofsleep)

         #after three times , still can't download,then unset the suqid, go to download directly
	if not successdownload:
		os.unsetenv("http_proxy")
 		print "Do Not Use Proxy"
		print "Max Download Trials #: "+str(numgetretries)
		for i in range(numgetretries)





				print "Unable to download :"+urladdress	
