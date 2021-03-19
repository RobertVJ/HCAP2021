import cv2

import numpy as np

#cargar la imagen a color

IRGB=cv2.imread('004.jpg')
print(IRGB)
print(IRGB.shape)

print("Este es una modificacion en la rama principal para generar conflicto")
print(len(IRGB))

