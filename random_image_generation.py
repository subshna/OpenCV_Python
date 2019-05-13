import numpy as np
import cv2 as cv
import os

# make an array of 120,000 random bytes
randombyte = bytearray(os.urandom(120000))

flatnumpyarray = np.array(randombyte)
print (flatnumpyarray)

# convert the array to make a 400x300 size grayscale image
grayscale = flatnumpyarray.reshape(300, 400)
cv.imwrite('Random_GrayScale.png', grayscale)

# convert the array to amke a 400x100 size BRG image
bgrimage = flatnumpyarray.reshape(100, 400, 3)
cv.imwrite('Random_BGRScale.png', bgrimage)