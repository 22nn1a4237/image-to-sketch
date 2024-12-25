# Python program to Convert Image into sketch

"""
# import all the required modules
import numpy as np
import imageio
import scipy.ndimage
import cv2


# take image input and assign variable to it
img = "image.jpg"


# function to convert image into sketch
def rgb2gray(rgb):
	# 2 dimensional array to convert image to sketch
	return np.dot(rgb[..., :3], [0.2989, 0.5870, .1140])


def dodge(front, back):

	# if image is greater than 255 (which is not possible) it will convert it to 255
	final_sketch = front*255/(255-back)
	final_sketch[final_sketch > 255] = 255
	final_sketch[back == 255] = 255

	# to convert any suitable existing column to categorical type we will use aspect function
	# and uint8 is for 8-bit signed integer
	return final_sketch.astype('uint8')


ss = imageio.imread(img)
gray = rgb2gray(ss)

i = 255-gray


# to convert into a blur image
blur = scipy.ndimage.filters.gaussian_filter(i, sigma=13)


# calling the function
r = dodge(blur, gray)


cv2.imwrite('4.png', r)
print("welcome")"""












import cv2
image = cv2.imread('image.jpg') # loads an image from the specified file
# convert an image from one color space to another
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img) # helps in masking of the image
# sharp edges in images are smoothed while minimizing too much blurring
blur = cv2.GaussianBlur(invert, (21, 21), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite("sketch.png", sketch) # converted image is saved as mentioned name

