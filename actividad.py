import numpy as np
import cv2

def convolucion(IOriginal,Kernel):
    fr=len(IOriginal)-(len(Kernel)-1)
    cr=len(IOriginal[0])-(len(Kernel[0])-1)
    Resultado=np.zeros((fr,cr),np.uint8)
    #Numero de elementos calculado por fila/columna
    #For para recorrer filas
    for i in range(len(Resultado)):
        #For para recorder columnas
        for j in range(len(Resultado[0])):
            suma=0
            for m in range(len(Kernel)):
                for n in range(len(Kernel[0])):
                        suma+=Kernel[m][n]*IOriginal[m+i][n+j]
                if suma <= 255:
                    Resultado[i][j]=round(suma)
                else:
                    Resultado[i][j]=255
    return Resultado
#Imagenes
K=[[-1,0,1],[-1,0,1],[-1,0,1]]
I=[[2,0,1,1,1],[3,0,0,0,2],[1,1,1,1,1],[3,1,1,1,2],[1,1,1,1,1]]
#Iamagenes a nuypay arrays
In=np.array(I)
Kn=np.array(K)

# Para cargar imagenes reales
IRGB=cv2.imread('004.jpg')
IGS=cv2.cvtColor(IRGB,cv2.COLOR_BGR2GRAY)
print(IGS.shape)

#Funcion de convolucion
R=convolucion(IGS,Kn)
print(R)
print(R.shape)
cv2.imwrite('004C.jpg',R)

