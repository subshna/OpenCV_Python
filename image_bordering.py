import cv2 as cv
import numpy as np

img = cv.imread('face3.jpg')

replicate = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_REFLECT101)
constant = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=[255, 0, 0])

cv.imshow('Replicate', replicate)
cv.imshow('Reflect', reflect)
cv.imshow('Reflect101', reflect101)
cv.imshow('Constant', constant)
cv.waitKey(0)
cv.destroyAllWindows()