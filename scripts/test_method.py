# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 17:53:18 2022

@author: R I B
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
from math import *
import csv
import PIL
from PIL import ImageOps, Image
import os
import xml.etree.cElementTree as et
Zone=[570, 500, 717, 584]#513
def get_img_files(path):
    ''' fonction pour extraire les fichiers xml dans un path donné.'''
    xml_list = []
    for filename in os.listdir(path):
        if filename.endswith(".jpg"):
            xml_list.append(os.path.join('', filename))
    return xml_list
# Il faut penser à changer le path selon votre pc
L=get_img_files("C:\\Users\\R I B\\Desktop\\wooow\\annoted data")
''' extraire les ficihers jpg '''
for i in range(len(L)):
    A=[]
    xmin,ymin,xmax,ymax=0,0,0,0
    image=Image.open(L[i])
    
    box=Zone

    area=image.crop(box)
    area=ImageOps.grayscale(area)
    M=np.array(area)
    N,P=M.shape
    pas=31
    for k in range((N//pas)):
        for m in range((P//pas)):
            a=M[(k+1)*pas-pas//2][(m+1)*pas-pas//2] # pixels du centre de gravité
            T=M[((k+1)*pas-pas//2)-pas//4:((k+1)*pas-pas//2)+pas//4,((m+1)*pas-pas//2)-pas//4:((m+1)*pas-pas//2)+pas//4]
            test=True
            s1,s2=T.shape
            for p in range(s1):
                for s in range(s2):
                    if T[s][p]>110:
                        test=False
                        break
            if test==True:
                   xmin=((k+1)*pas-pas//2)-pas//2
                   xmax=((k+1)*pas-pas//2)+pas//2
                   ymax=((m+1)*pas-pas//2)+pas//2
                   ymin=((m+1)*pas-pas//2)-pas//2
                   A.append([xmin,ymin,xmax,ymax])
                   break
    area=image.crop(box)
    M=np.array(area)
    if len(A)>0:
        xmin,ymin,xmax,ymax=A[-1][0],A[-1][1],A[-1][2],A[-1][3]
        for l in range(xmin,xmax):
            for t in range(ymin,ymax):
                M[xmax-1][t]=[0,255,0]
                M[l][ymin]=[0,255,0]
                M[xmin][t]=[0,255,0]
                M[l][ymax-1]=[0,255,0]
    plt.imshow(M,interpolation='nearest')
    plt.show()
              