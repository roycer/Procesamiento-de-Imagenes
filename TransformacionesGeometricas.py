import cv2
import numpy as np

img = cv2.imread('img01.jpg')
alto, ancho = img.shape[:2]

# ESCALAMIENTO
sca = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)

# TRASLACION
T = np.float32([[1,0,100],[0,1,50]])
tras = cv2.warpAffine(img,T,(ancho,alto))

# ROTACION
R = cv2.getRotationMatrix2D((ancho/2,alto/2),90,0.5)
rot = cv2.warpAffine(img,R,(ancho,alto))

cv2.imshow('ORIGINAL',img)
cv2.imshow('ESCALAMIENTO',sca)
cv2.imshow('TRASLACION',tras)
cv2.imshow('ROTACION',rot)

cv2.waitKey(0)
cv2.destroyAllWindows()