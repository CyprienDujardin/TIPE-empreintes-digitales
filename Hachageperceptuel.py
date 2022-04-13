from PIL import Image
import imagehash
import os
os.chdir('/Users/cyprien/Documents/TIPE/Images/')

def Hashter():

    image1 = Image.open("test.jpg")             #Ouverture des images
    image2 = Image.open("test2.png")
    hash1 = imagehash.average_hash(image1)      #Calcul des empreintes numériques des images via la fonction python average_hash
    hash2 = imagehash.average_hash(image2)
    print(hash1)

    print(hash2)

    return hash1 - hash2                        #Calcul de la distance des deux empreintes (Nombre de carractère differents)
