from PIL import Image
from PIL import ImageOps
import matplotlib.pyplot as plt
import numpy as np
image=Image.open("frame100.jpg")# ouvrir une image de frame100
image_gray=ImageOps.grayscale(image) #convertir l'image en échelle noir et blanc(grayscale)
array=np.array(image_gray) #conversion de l'image en matrice
box=(613,257,644,287)
area=image_gray.crop(box) #prendre la partie de l'image correspondante au box
print(area.size)
area.show()

M=np.array(area)
box1=(0,0,15,15)
area1=area.crop(box1)
M1=np.array(area1) # partie basse gauche du bounding box
area1.show()
print (M1)

box2=(15,0,31,15)
area2=area.crop(box2)
M2=np.array(area2)  #partie basse droite du bounding box
area2.show()
print(M2)

box3=(0,15,15,31)
area3=area.crop(box3)
M3=np.array(area3)  #partie haute gauche du bounding box
area3.show()
print(M3)

box4=(15,15,31,31)
area4=area.crop(box4)
M4=np.array(area4)  #partie haute droite du bounding box
area4.show()
print(M4)
