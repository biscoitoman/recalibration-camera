import cv2 as cv

cam = cv.VideoCapture(0)

import time
import matplotlib.pyplot as plt

frames = []
for i in range(0,10):
	time.sleep(3)
	ret, frame = cam.read()
	plt.imshow(frame, cmap='gray')
	plt.show()
	frames.append(frame)
	cv.imwrite('tabuleiro_' + str(i) + '.jpg', frame)