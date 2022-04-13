import numpy as np
import matplotlib.pyplot as plt
import copy
import os
import sys
from PIL import Image,ImageFilter



# Chemin d'accès et nom des fichiers image






imageEmpreinte = Image.open('/Users/cyprien/Documents/TIPE/Images/test.jpg')





def creeTableauImage(nomFichier):
    """
    Lit la chaine de caractères correspondant au nom
    du fichier image (de type .png) et retourne le tableau numpy associé.
    Imprime sur console Python la forme du tableau, le type de données,
    le nb de lignes, le nb de colonnes et
    la valeur de la première cellule du tableau.
    """
    tab = plt.imread(nomFichier)
    nblignes  = tab.shape[0]
    nbcols  = tab.shape[1]
    print("")
    print("Caractéristiques du fichier image " + nomFichier)
    print("shape : ", tab.shape)
    print("type de données : ", tab.dtype)
    print("nb de lignes : ", nblignes)
    print("nb de cols : ", nbcols)
    print("1ere cellule : ", tab[0,0])
    print("")
    return(tab)

def afficheImage(tableauImage):
    
    #Affiche l'image associée au tableau tableauImage. Ne retourne rien.
    
    assert type(tableauImage) == np.ndarray
    plt.figure()
    plt.imshow(tableauImage, interpolation='nearest')
    plt.axis('off')
    plt.show()
    return(None)




def noirblanc(tableauImage):                  #fonction transformant l'image en binaire (noir ou blanc)
    ligne = tableauImage.shape[0]
    colonne = tableauImage.shape[1]
    t = np.zeros((ligne, colonne, 3))

    for i in range(0,ligne):
        for j in range(0, colonne):
            if tableauImage[i,j][0]>=200:
                t[i,j]=[1,1,1]
            else:
                t[i,j]=[0,0,0]

    return t

def listej(i, colonne, noiretblanc):          #fonction qui liste pour un ligne fixé, le numéro des colonnes des pixels noirs

    L=[]
    for j in range(0, colonne):
        if noiretblanc[i,j][0]==0:
            L.append(j)

    return L


def f(L):                     #fonction qui prend à part les premieres valeures de la liste des indices de colonnes qui se suivent
    M=[L[0]]
    for i in range(0, len(L)-1):
        if L[i] == L[i+1]-1:
            M.append(L[i+1])
        else :
            return M

def squelette(tableauImage):
    ligne = tableauImage.shape[0]
    colonne = tableauImage.shape[1]
    t = np.zeros((ligne, colonne, 3)) #Création d'un tableau du même nombre de ligne et colonne que l'image, affichant une image noir

    O=[]   #une liste
    m=0
    i=0   #indice de la ligne
    noiretblanc = noirblanc(tableauImage)     #transforme l'image en noir et blanc

    while i != ligne :

            L=listej(i,colonne, noiretblanc)             #mise en liste des coordonnés de la colonne des pixels noirs de la ligne i

            if L==[]:             #si aucun noir sur la ligne, on passe à la ligne suivante
                i+=1

            else:
                while L!=[]:       #si présence de noir sur la ligne i fixé
                    M=f(L)         #Crée une liste des premiers entier qui se suit dans L

                    if M.__class__ == O.__class__:   #Si M de meme classe que O

                        if len(M)==1:       #si une seul valeur, l'indice de colonne a changer et cette valeur
                            m=M[0]
                        elif len(M)%2 == 0:            #sinon prend la valeur du milieu en focntion de si il y un nombre d'indice paire ou impaire
                            m=M[(len(M)//2)-1]
                        else:
                            m=M[(len(M)//2)]

                        t[i,m]=[1,1,1]         #transforme la case du milieu de la suite de pixel noir en blanc

                        L=L[len(M):]          #retir la premiere série de pixel noir de la liste L

                    else :               #pour les dernières valeurs de la liste L qui se suivent car la fonction f(L) bug et ne renvoie rien

                        if len(L)==1:             #on fait la meme chose qu'avec M mais avec L puisque ce sont les derniere valeurs qui se suivent
                            m=L[0]
                        elif len(L)%2 == 0:
                            m=L[(len(L)//2)-1]
                        else:
                            m=L[(len(L)//2)]

                        t[i,m]=[1,1,1]

                        L=L[len(L):]
                i+=1    #puis une fois L vide on pas à la ligne suivante




    afficheImage(t)
    
    return t

def finalcountdown():
    tabl=creeTableauImage(imageEmpreinte)
    return squelette(tabl)
