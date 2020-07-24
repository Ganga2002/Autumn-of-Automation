def detect_circle(img):

	ret, thresh = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY)
	contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area > 200 and area <700:

			#Approximation to get a regular shape of the ball
			epsilon = 0.01*cv2.arcLength(cnt,True)
			approx = cv2.approxPolyDP(cnt,epsilon,True)
			if len(approx) > 5:
				x,y,w,h = cv2.boundingRect(approx)
				cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
				cv2.imshow(img)
				cv2.waitKey(1)

import numpy as np
import cv2
import math

cap = cv2.VideoCapture('Messi.mp4')

while True:
	ret2, vid = cap.read()
	vid_gray = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
	detect_circle(vid_gray)
	key = cv2.waitKey(1)
	if key == ord('c'):
		break
