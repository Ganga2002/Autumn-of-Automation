import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img_color = cv2.imread('lena.jpg')
img_gray  = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
ret, img_BnW   = cv2.threshold(img_gray, 150, 255, cv2.THRESH_BINARY_INV)

cv2.imshow('org', img_BnW)
cv2.waitKey(0)

cv2.imshow('gray', img_gray)
cv2.waitKey(0)


#ret, img_BnW   = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)
