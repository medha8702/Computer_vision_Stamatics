import cv2 as cv
import numpy as np
import sys

# Reading the image
img = cv.imread(sys.argv[1])

img.shape
width = img.shape[1]
height = img.shape[0]

temp_img = np.array(img, copy = True)
final_img = np.array(img, copy = True)



# Getting coordinates fot the left part
temp_img = np.array(img, copy = True)
temp_img[:, (width//4 -1 - 10) : (width//4 +1 - 10)] = np.array([0, 0, 0])
#cv.imshow(temp_img)
left_top_right_x = width//4 - 10

temp_img = np.array(img, copy = True)
temp_img[(height//2 - 1 - 10) : (height//2 + 1 - 10), :] = np.array([0, 0, 0])
#cv.imshow(temp_img)
left_top_bottom_y = height//2 - 10



# Getting coordinates for left bottom part
temp_img = np.array(img, copy = True)
temp_img[(height - 1 - 10) : (height-9), :] = np.array([0, 0, 0])
#cv.imshow(temp_img)
left_bottom_bottom_y = height - 12


# Pasting the lower part to top left
temp = np.array(img[(left_top_bottom_y):left_bottom_bottom_y+1, 0:left_top_right_x], copy = True)
temp_height = temp.shape[0]
temp_width = temp.shape[1]

for i in range(0, temp_height):
  for j in range(0, temp_width):
    final_img[i, j+1] = temp[temp_height-i-1,j]
#cv.imshow(final_img)



# Pasting the top left part to its correct position and interchanging it's blue and green channels
temp = np.array(img[0:left_top_bottom_y, 0:left_top_right_x], copy = True)
temp2 = np.array(img[0:left_top_bottom_y, 0:left_top_right_x], copy = True)
temp[:, :, 1] = temp2[:, :, 0]
temp[:, :, 0] = temp2[:, :, 1]

final_img[(left_bottom_bottom_y - left_top_bottom_y-10):left_bottom_bottom_y-10, 2:left_top_right_x+2] = temp
#cv.imshow(final_img)



# Getting coordinates for bottom middle part
temp_img = np.array(img, copy = True)
temp_img[:, (width//2 -1 - 28) : (width//2 +1-28)] = np.array([0, 0, 0])
#cv.imshow(temp_img)
bottom_middle_left_x = (width//2 - 28)

temp_img = np.array(img, copy = True)
temp_img[:, (4*width//5) : (4*width//5 +1)] = np.array([0, 0, 0])
#cv.imshow(temp_img)
bottom_middle_right_x = 4*width//5

temp_img = np.array(img, copy = True)
temp_img[(7*height//8 + 2):(7*height//8 + 3), :] = np.array([0, 0, 0])
#cv.imshow(temp_img)
bottom_middle_top_y = 7*height//8 + 2



# Vertically flipping the bottom middle part
temp = np.array(img[bottom_middle_top_y:(height-1), bottom_middle_left_x: bottom_middle_right_x], copy = True)

temp_width = temp.shape[1]
temp_height = temp.shape[0]

for i in range(0, temp_height):
  for j in range(0, temp_width):
    final_img[bottom_middle_top_y+i, bottom_middle_left_x+j] = temp[temp_height-1-i ,j]



# Getting coordinates for right part
temp_img = np.array(img, copy = True)
temp_img[(height//3 + 10):(height//3 + 11), :] = np.array([0, 0, 0])
#cv.imshow(temp_img)
yellow_top_y = height//3 + 10

temp_img = np.array(img, copy = True)
temp_img[(3*height//4 + 15):(3*height//4 + 16), :] = np.array([0, 0, 0])
#cv.imshow(temp_img)
yellow_bottom_y = 3*height//4 + 15

temp_img = np.array(img, copy = True)
temp_img[:, (2*width//3 - 16):(2*width//3-15)] = np.array([0, 0, 0])
#cv.imshow(temp_img)
yellow_left_x = 2*width//3 - 16

temp_img = np.array(img, copy = True)
temp_img[:, (7*width//8 + 2):(7*width//8 + 3)] = np.array([0, 0, 0])
#cv.imshow(temp_img)
yellow_right_x = 7*width//8 + 3

temp = np.array(img[yellow_top_y: yellow_bottom_y, yellow_left_x: yellow_right_x], copy = True)

temp_width = temp.shape[1]
temp_height = temp.shape[0]

for i in range(0, temp_height):
  for j in range(0, temp_width):
    final_img[(yellow_top_y + i), (yellow_left_x + j)] = temp[i,(temp_width - 1 - j)]

cv.imwrite('Final_image.jpg', final_img)
cv.imshow('Final Image',final_img)
cv.waitKey(0)