#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 11:30:00 2019

@author: supaul
"""
import os
import hashlib
import shutil
import sys
dicti=dict()
def recurseDir(path):
    
    files=os.listdir(path)
    #print(path)
    if(len(files)==0):
        return
    else:
        for file in files:
            if(file!=".DS_Store"):
                pathnew=path+"/"+file
                if(os.path.isdir(pathnew)):
                    recurseDir(pathnew)
                else:
                   #print(pathnew)
                    openedFile = open(pathnew,'rb')
                    readFile = openedFile.read()
                    md5Hash = hashlib.md5(readFile)
                    dicti[md5Hash.hexdigest()]=pathnew
                    


    



path=sys.argv[1]
recurseDir(path)
#recurse through a dictionary and copy it's elements else where
for key in dicti:
    #print(dicti[key])
    basename=os.path.basename(dicti[key])
    #print(basename)
    newaddress=sys.argv[2]
    newaddress+="/"
    newaddress+=basename;
    shutil.copy(dicti[key],newaddress)
    


        
