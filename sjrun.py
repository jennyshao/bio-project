#!/usr/bin/python
import sys,os
import fileinput
import tarfile
import socket
import string
import subprocess
import random
import time


print "this is  2nd version!"

Lid = []
num =1

def downloadfile(urloffile):
	urloffile='wget -q '+urloffile   #-q means quite, Turn off Wget’s output.
        purduesquid='http://squid.rcac.purdue.edu'
	purduematcstring='purdue.edu'
	numwgetretries=3
	osgsquid=os.getenv('OSG_SQUID_LOCATION')
	print "osgsquid is set to: "+str(osgsquid)
	hostname=socket.gethostname()
	print "hostname is set to: "+str(hostname)
	if osgsquid != None and string.find(osgsquid.upper(), 'UNAVAILABLE') < 0:
		os.putenv('http_proxy', osgsquid)
	elif string.find(hostname,purduematcstring) >=0:
		os.putenv('http_proxy', purduesquid)
	else:
		os.unsetenv('http_proxy')
	succefulldownload = False
	print "using Proxy: "+str(os.getenv('http_proxy'))
	print "Max download trials: "+str(numwgetretries)
	for i in range(numwgetretries):
		print "Trial #: "+str(i)
		process=subprocess.Popen(urloffile, shell=True)
		process.wait()
		returncode=process.poll()
		if returncode==0:
			succefulldownload=1
			break
		sleepfor=(random.random())*180 # seconds
		print "Sleeping for %s seconds before retrying"%(sleepfor)
		time.sleep(sleepfor)

	if not succefulldownload: #try unsetting the squid and going directly
		os.unsetenv('http_proxy')
		print "Not using using Proxy"
		print "Max download trials: "+str(numwgetretries)
		for i in range(numwgetretries):
			print "Trial #: "+str(i)
			process=subprocess.Popen(urloffile, shell=True)
			process.wait()
			returncode=process.poll()
			if returncode==0:
				succefulldownload=1
				break
			sleepfor=(random.random())*180 # seconds
			print "Sleeping for %s seconds before retrying"%(sleepfor)
			time.sleep(sleepfor)
	if not succefulldownload:
		print "Unable to download: "+urloffile
		sys.exit(1)
	else:
		print "Succesfully downloaded: "+urloffile



downloadfile("http://hcc-server.unl.edu/BENSON/rpstblastn")
os.popen("chmod 755 rpstblastn")

# run main program 
Input_list=sys.argv[1]
OutBase=sys.argv[2]
cddIndex=sys.argv[3]
print "this is"+ cddIndex
os.popen("mkdir "+OutBase)
downloadfile("http://hcc-server.unl.edu/BENSON/CDD%s.tar"%(cddIndex))
os.popen("tar -xvf CDD%s.tar"%(cddIndex));
# os.remove("CDD%s.tar"%(cddIndex))

#********** RUN MAIN***********************
for line in fileinput.input(sys.argv[1]):
         Lid.append(line)
         if len(Lid) == 2:
                w=open("Temp","w")
                L="".join(Lid)
                w.write("%s"%L)
                w.close()
                Out_name = OutBase+'/'+OutBase+'.'+str(num); num = num + 1
                Run1=("./rpstblastn -query Temp -db CDD%s/Cdd%s -evalue 0.0001 -outfmt 6 -out %s"%(cddIndex, cddIndex, Out_name))
                os.popen(Run1)
                Lid=[]
                flagdownloaded=1


os.popen('tar cvzf TAR_'+OutBase+'.tar.gz '+OutBase+'* ')
print os.path.abspath(__file__)
os.popen('rm -rf rpstblastn CDD* Cdd* Temp '+Input_list+' '+OutBase)
#os.popen('rm -rf '+OutBase+'*')
