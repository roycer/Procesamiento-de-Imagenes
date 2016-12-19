import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img01.jpg',0)

umbral1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)[1]
umbral2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)[1]
umbral3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)[1]
umbral4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)[1]
umbral5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)[1]

titulo = ['Original','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
imagen = [img, umbral1, umbral2, umbral3, umbral4, umbral5]

for i in xrange(6):
    plt.subplot(2,3,i+1),plt.imshow(imagen[i],'gray')
    plt.title(titulo[i])
    plt.xticks([]),plt.yticks([])

plt.show()