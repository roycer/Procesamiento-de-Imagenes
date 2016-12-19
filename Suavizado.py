import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img03.jpg')

# FILTRO
kernel = np.ones((5,5),np.float32)/25
filt = cv2.filter2D(img,-1,kernel)

# FILTRO GAUSIANO
blur = cv2.GaussianBlur(img,(5,5),0)

# FILTRO DE LA MEDIANA
med = cv2.medianBlur(img,5)

# FILTRO BILATERAL
bil = cv2.bilateralFilter(img,9,75,75)

plt.subplot(2,2,1),plt.imshow(img),plt.title('Original'),plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(filt),plt.title('filter2D'),plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(filt),plt.title('GaussianBlur'),plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(filt),plt.title('medianBlur'),plt.xticks([]), plt.yticks([])

plt.show()