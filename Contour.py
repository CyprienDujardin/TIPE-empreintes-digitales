import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image
os.chdir('/Users/cyprien/Documents/TIPE/Images/')


img=Image.open('/Users/cyprien/Documents/TIPE/Images/R.jpg')


def Norme(p1,p2,p3,p4):
        n = np.sqrt((p1[0]-p3[0])*(p1[0]-p3[0]) + (p2[0]-p4[0])*(p2[0]-p4[0]))    #Calcul de la norme euclidienne pour un pixel
        return n


def contour():
    colonne,ligne = img.size                #obtention des dimensions de l'image 
    imgC = Image.new(img.mode,img.size)     #Création d'une image blanche de même dmension
    seuil = 80                              #À adapter en focntion de l'exigence souhaité 
    L=[]
    for i in range(1,ligne-1):
        for j in range(1,colonne-1):        #On parcours l'image pixel par pixel
            p1 = img.getpixel((j-1,i))      #P1 -> Pixel "au dessus" du pixel séléctioné 
            p2 = img.getpixel((j,i-1))      #P2 -> Pixel "à droite" du pixel séléctioné 
            p3 = img.getpixel((j+1,i))      #P3 -> Pixel "en dessous" du pixel séléctioné 
            p4 = img.getpixel((j,i+1))      #P4 -> Pixel "à gauche" du pixel séléctioné 
            n = Norme(p1,p2,p3,p4)
            if n < seuil:
                p = (255,255,255)
            else:
                L.append([i,j])  
                p = (0,0,0)
            imgC.putpixel((j,i),p)
    return imgC,L                           #Renvoie les contours de l'image d'entrée, La liste des coordonées de ces contours

