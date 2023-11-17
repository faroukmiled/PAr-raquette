import pandas as pd
import numpy as np
import glob
import csv


import os
import xml.etree.cElementTree as et
def get_xml_files(path):#fonction pour extraire les fichiers xml dans un path donné.
    xml_list = []
    for filename in os.listdir(path):
        if filename.endswith(".xml"):
            xml_list.append(os.path.join(path, filename))
    return xml_list
# Il faut penser à changer le path selon votre pc
L=get_xml_files("C:\\Users\\R I B\\ownCloud\\samples\\img")# extraire les ficihers xml ( notre data set annoté)
nom_colonnes=['filename',   'width',   'height',  'xmin',  'ymin',  'xmax',  'ymax']
L2=[]
for ch in L:
    ch=ch.split('\\')[-1]# prednre juste le nom du frame à traiter
    tree=et.parse(ch)
    root=tree.getroot()
    #Définir les inforamtions importantes à garder
    filename1=[]
    width1=[]
    height1=[]
    xmin1=[]
    xmax1=[]
    ymin1=[]
    ymax1=[]
    for filename in root.iter('filename'):
        filename1.append(filename.text)
    for width in root.iter('width'):
        width1.append(width.text)
    for height in root.iter('height'):
        height1.append(height.text)
    for xmin in root.iter('xmin'):
        xmin1.append(xmin.text)
    for xmax in root.iter('xmax'):
        xmax1.append(xmax.text)
    for ymin in root.iter('ymin'):
        ymin1.append(ymin.text)
    for ymax in root.iter('ymax'):
        ymax1.append(ymax.text)
    L1=[filename1[0], width1[0], height1[0],  xmin1[0], ymin1[0],  xmax1[0],   ymax1[0]]
    L2.append(L1)
with open ('csvfile.csv', 'w') as fichier:
    obj = csv.writer(fichier)
    obj.writerows(L2)
        