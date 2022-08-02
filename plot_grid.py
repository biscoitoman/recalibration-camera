import cv2 as cv
import matplotlib.pyplot as plt
  
# Reading an image in default mode
img_orig = cv.imread('tabuleiro_0.jpg')
img_calibrada = cv.imread('calibresulttabuleiro_0.jpg.png') 
  
# Window name in which image is displayed
window_name = 'Image'
 
# Start coordinate, here (0, 0)
# represents the top left corner of image
start_point = (0, 0)
 
# End coordinate, here (250, 250)
# represents the bottom right corner of image
end_point = (313, 173)
 
# Green color in BGR
color = (0, 255, 0)
 
# Line thickness of 9 px
thickness = 4
 
# Using cv2.line() method
# Draw a diagonal green line with thickness of 9 px
image = cv.line(img_orig, start_point, end_point, color, thickness)
 
start_x = start_point[0]
start_y = start_point[1]
end_x = start_point[0]
end_y = end_point[1]
cv.line(img_calibrada, (start_x, start_y), (end_x, end_y), (255, 0, 0), 1, thickness)

# Displaying the image
cv.imshow(window_name, image)
plt.imshow(image)
plt.show()