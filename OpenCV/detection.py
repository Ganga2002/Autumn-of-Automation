import cv2
import numpy as np
import math

img = cv2.imread('Test.png')
sketch = cv2.imread('Test.png')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 225, 255, cv2.THRESH_BINARY_INV)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow('identified', thresh)
cv2.waitKey(0)

for cnt in contours:
	area = cv2.contourArea(cnt)
	if area > 400:
		M = cv2.moments(cnt)
		cx, cy = int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])
		approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
		sketch = cv2.drawContours(sketch, approx, -1, (255,0,0), 1)

		if len(approx)==3:
			print(f'Triangle, centroid {cx, cy}')
		
		elif len(approx)==4:
			x, y, w, h = cv2.boundingRect(approx)
			aspect_ratio = float(w)/h
			extent       = float(area)/(w*h)
			if aspect_ratio < 0.9 or aspect_ratio > 1.1:
				if extent < 0.9:
					print(f'Rhombus, centre {cx, cy}')
				elif extent > 0.9 and extent < 1.1:
					print(f'Rectangle, centre {cx, cy}')
			elif aspect_ratio > 0.9 and aspect_ratio < 1.1:
				print(f'square, centre {cx, cy}')
		
		elif len(approx) > 12:
			(x, y), radius = cv2.minEnclosingCircle(approx)
			x, y, radius = int(x), int(y), int(radius)
			bcircle_area = math.pi * radius * radius
			ratio = area / bcircle_area
			if ratio < 0.9:
				print(f'oval, centre {cx, cy}')
			elif ratio > 0.9 and ratio < 1.1:
				print(f'Circle, centre {cx, cy}')






