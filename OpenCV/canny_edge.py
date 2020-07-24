import cv2
import numpy as np 
from matplotlib import pyplot as plt

video = cv2.VideoCapture(0)

while True:
	ret, frame = video.read()
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	frame = cv2.GaussianBlur(frame, (3, 3), 0)

	edges = cv2.Canny(frame, 50, 75)
	thres, edge = cv2.threshold(edges, 127, 255, cv2.THRESH_BINARY_INV)
	cv2.imshow('Edges', edge)

	key = cv2.waitKey(1)
	if key == ord('c'):
		break



