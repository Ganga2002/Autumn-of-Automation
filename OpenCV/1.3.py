import cv2

img_BGR = cv2.imread('lena.jpg')
img_RGB  = cv2.cvtColor(img_BGR, cv2.COLOR_BGR2RGB)

cv2.imshow('BGR', img_BGR)
cv2.waitKey(0)

cv2.imshow('RGB', img_RGB)
cv2.waitKey(0)