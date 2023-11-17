# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 00:49:08 2023

@author: R I B
"""
from os import listdir
from os.path import isfile, join
directory="train\labels"
fichier=open("labels.csv",'a')
fichiers = [f for f in listdir(directory) if isfile(join(directory, f))]
for f in fichiers:
    a=open(directory+'/'+f,"r")
    L=a.readlines()
    if len(L)>0:
        fichier.write(f[5:15]+' '+L[0]+'\n')
    if len(L)>1:
        fichier.write(f[5:15]+' '+L[1]+'\n')
    if len(L)>2:
        fichier.write(f[5:15]+' '+L[2]+'\n')
    if len(L)>3:
        fichier.write(f[5:15]+' '+L[3]+'\n')
fichier.close()
    
