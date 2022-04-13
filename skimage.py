import skimage
from skimage.morphology import skeletonize
from skimage import data
import matplotlib.pyplot as plt
from skimage.util import invert
import os
import numpy as np


imageEmpreinte = Image.open('/Users/cyprien/Documents/TIPE/Images/R.jpg')


def creeTableauImage(nomFichier):
    """
    Lit la chaine de caractères correspondant au nom
    du fichier image (de type .png) et retourne le tableau numpy associé.
    Imprime sur console Python la forme du tableau, le type de données,
    le nb de lignes, le nb de colonnes et
    la valeur de la première cellule du tableau.
    """
    tab = plt.imread(nomFichier)
    nblignes = tab.shape[0]
    nbcols = tab.shape[1]
    print("")
    print("Caractéristiques du fichier image " + nomFichier)
    print("shape : ", tab.shape)
    print("type de données : ", tab.dtype)
    print("nb de lignes : ", nblignes)
    print("nb de cols : ", nbcols)
    print("1ere cellule : ", tab[0, 0])
    print("")
    return(tab)


def noirblanc(tableauImage):  # fonction transformant l'image que en noir ou en blanc
    ligne = tableauImage.shape[0]
    colonne = tableauImage.shape[1]
    t = np.zeros((ligne, colonne, 3))

    for i in range(0, ligne):
        for j in range(0, colonne):
            if norme(tableauImage[i, j]) >= 10:
                t[i, j] = [1, 1, 1]
            else:
                t[i, j] = [0, 0, 0]

    return t


def skeletonized():
    pop1 = creeTableauImage(imageEmpreinte)
    pop = noirblanc(pop1)
# Invert the horse image
    image = invert(pop)

# perform skeletonization
    skeleton = skeletonize(image)

# display results
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(8, 4),
                             sharex=True, sharey=True)

    ax = axes.ravel()

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].axis('off')
    ax[0].set_title('original', fontsize=20)

    ax[1].imshow(skeleton, cmap=plt.cm.gray)
    ax[1].axis('off')
    ax[1].set_title('skeleton', fontsize=20)

    fig.tight_layout()
    plt.show()
    return skeleton


def CN():
    tabl = noirblanc(skeletonized())
    print(tabl)
    p = tabl.shape[0]
    k = tabl.shape[1]
    L = [0, 0, 0, 0, 0]
    for i in range(0, p-1):
        for j in range(0, k-1):
            P = [int(tabl[i-1][j][0]), int(tabl[i-1][j-1][0]), int(tabl[i-1][j+1][0]), int(tabl[i][j-1][0]), int(tabl[i]
                                                                                                                 [j+1][0]), int(tabl[i+1][j][0]), int(tabl[i+1][j-1][0]), int(tabl[i+1][j+1][0]), int(tabl[i-1][j][0])]
            cn = 0
            for u in range(8):
                cn = cn + 0.5*np.abs(P[u]-P[u+1])

            if cn == 0:
                L[0] = L[0]+1  # erreur -> point isolé
            elif cn == 1:
                L[1] = L[1]+1  # terminaison
            elif cn == 2:
                L[2] = L[2]+1  # erreur --> point sillon
            elif cn == 3:
                L[3] = L[3]+1  # divergence ou bifurcation
            elif cn == 4:
                L[4] = L[4]+1  # erreur -> minutie à 4 branches
    return L


