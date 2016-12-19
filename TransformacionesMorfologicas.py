import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('img02.png')
img1 = cv2.imread('img03.png')
img2 = cv2.imread('img04.png')

# EROSION
kernel = np.ones((5,5),np.uint8)
ero = cv2.erode(img,kernel,iterations = 1)
plt.subplot(2,5,1),plt.imshow(img),plt.title(''),plt.xticks([]), plt.yticks([])
plt.subplot(2,5,6),plt.imshow(ero),plt.title('erode'),plt.xticks([]), plt.yticks([])

# DILATION
dil = cv2.dilate(img,kernel,iterations = 1)
plt.subplot(2,5,2),plt.imshow(img),plt.title(''),plt.xticks([]), plt.yticks([])
plt.subplot(2,5,7),plt.imshow(dil),plt.title('dilate'),plt.xticks([]), plt.yticks([])

# OPENING
ope = cv2.morphologyEx(img1, cv2.MORPH_OPEN, kernel)
plt.subplot(2,5,3),plt.imshow(img1),plt.title(''),plt.xticks([]), plt.yticks([])
plt.subplot(2,5,8),plt.imshow(ope),plt.title('OPEN'),plt.xticks([]), plt.yticks([])

# CLOSING
clos = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)
plt.subplot(2,5,4),plt.imshow(img2),plt.title(''),plt.xticks([]), plt.yticks([])
plt.subplot(2,5,9),plt.imshow(clos),plt.title('CLOSE'),plt.xticks([]), plt.yticks([])

# MORPHOLOGICAL GRADIENT
grad = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.subplot(2,5,5),plt.imshow(img),plt.title(''),plt.xticks([]), plt.yticks([])
plt.subplot(2,5,10),plt.imshow(grad),plt.title('GRADIENT'),plt.xticks([]), plt.yticks([])


plt.show()