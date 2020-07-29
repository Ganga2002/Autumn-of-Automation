import cv2

video = cv2.VideoCapture(0)

while True:
	check, frame = video.read()
	cv2.imshow('Live Feed', frame)

	key = cv2.waitKey(1)
	if key == ord('c'):
		break

video.release()
cv2.destroyAllWindows