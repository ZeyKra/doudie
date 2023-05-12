# Créé par LesPenibles, le 13/12/2022 en Python 3.7
from PIL import Image


##Image.crop(box=None)[source]
##Returns a rectangular region from this image. The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate. See Coordinate System.
##Note: Prior to Pillow 3.4.0, this was a lazy operation.
##Parameters:
##box – The crop rectangle, as a (left, upper, right, lower)-tuple.
##Return type: Image
##Returns: An Image object.

nom = "appears"

nom_image = "appears.png"
img_a_traiter = Image.open(nom_image) #chargement de l'image en mémoire
colonne=[7,7,7,7,8,8,8,8,9,9,9,9,6,6,6,6,13,13,13,13,6]
for i in range(21) :
    print("ligne -->",i,"  colonne -->",end="")
    for j in range(colonne[i]):
        print(j," ; ",end="")
        img= img_a_traiter.crop((64*j,64*i,64*(j+1),64*(i+1)))
        numero="0"*(2-len(str(i)))+str(i)+"_"+"0"*(2-len(str(j)))+str(j)
        nom= "appears_"+numero+".png"
        img.save(nom)
    print()
