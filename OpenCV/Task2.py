def translation(img, nx, ny):
	rows, cols, ch = img.shape
	M = np.float32([[1, 0, cols // nx], [0, 1, rows // ny]])
	dst1 = cv2.warpAffine(img, M, (cols, rows))
	return dst1

def rotation(img, angle, magnification):
	rows, cols, ch = img.shape
	N = cv2.getRotationMatrix2D((cols//2, rows//2), angle, magnification)  
	dst2 = cv2.warpAffine(img, N, (cols, rows))   
	return dst2

def Affine(img, nx, ny):
	cols, rows, ch = img.shape
	pt1 = np.float32([[cols//nx, rows//ny], [cols//nx, rows-rows//ny], [cols-cols//nx, rows//ny]])
	pt2 = np.float32([[0, 0], [cols, 0], [0, rows]])
	A = cv2.getAffineTransform(pt1, pt2)
	Aff = cv2.warpAffine(img, A, (cols, rows))
	return Aff

def Data_augmentation(img, num):
	for i in range(num):
	
		nx = ri(4, 8)
		ny = ri(4, 8)
		ang = 10 * ri(0, 36)
		mg = 0.5 * ri(1, 3)

		temp = Affine(img, nx, ny)
		temp = rotation(temp, ang, mg)
		temp = translation(temp, nx ,ny)
		temp = cv2.blur(temp, (3,3))

		dest = 'image' + f'{i+1}' + '.jpg'
		cv2.imwrite(dest, temp)


import cv2
import numpy as np
from random import randint as ri 

sample = cv2.imread('Sample.png')

Data_augmentation(sample, 10)