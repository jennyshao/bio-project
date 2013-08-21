#!/usr/bin/python
#filename=run.py

import os
from sjcommon import *

A=sjcommon()
filerpst="http://hcc-server.unl.edu/BENSON/rpstblastn"
A.download(filerpst)
os.popen("chmod 755 rpstblastn")

# run main program
Input_list=sys.argv[1]
OutBase=sys.argv[2]
cddIndex=sys.argv[3]
print "this is cddIndenx:"+ cddIndex
os.popen("mkdir "+OutBase)
filecddIndex="http://hcc-server.unl.edu/BENSON/CDD%s.tar"%(cddIndex)
downloadfile(filecddIndex)
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

