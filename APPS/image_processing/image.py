'''
the smallgray.png is a gray scale image, made of pixels
3x5 pixels in size (15 pixels) and each pixel has a value.
Programs uses numbers to store images then the computer display converts these
numbers to colors.

python stores and uses arrays of numbers to displays images

the smallgray.png image could be represented by:

list_of_lists = [[123,12,123,12,33],[234,22,123,445,11],[a,b,c,d,e]]   3x5 in size

here numpy comes in handy

Numpy is a base library for all other libs such as pandas and OpenCV which is an image processing library
for ex: pandas df are based on numpy arrays and OpenCV objects are based on numpy arrays
'''

import numpy as np

n = np.arange(27) # create an array (1 dimensional, looks like a list)
n.reshape(3,9)    # transform it to a 2D array
n.reshape(3,3,3)  # transform it to a 3D array
m=np.asarray([[123,135,63,634,12],[],[]])  # create an array from a list, or a list of lists

# lets jump to image processing

import cv2   #pip install opencv-python

# read an image
img = cv2.imread("smallgray.png",0)    # 2nd argument 0=read in grayscale 1=read in BGR (blue,green,red)  !NOT RGB as in other software
print(img)   # shows an array with a dimenson of 3 by 5
img = cv2.imread("smallgray.png",1)    # read it as color picture
print(img)   # will show 3 arrays that represent the intensity of each color BGR for eash pixel

# create an image
cv2.imwrite("newsmallgray.png",img)   # you pass in the array with the values you want to create a new image

# slicing a numpy array
img = cv2.imread("smallgray.png",0)
img[0:2]      # this is index for rows - gives first 2 arrays
img[0:2,2:4]  # (second element) this is index for columns
img[2,4]      # get one element (x,y) coordonates

# iteration
for i in img:
    print(i)    # this iterates through the rows

for i in  img.T:
    print(i)    # if you want to iterate through the columns, you have to access the transposed form of the array

for i in img.flat:
    print(i)    # to access the values 1 by 1

# stacking arrays
img_h = np.hstack(img,img)    # horizontal stacking -> this gives error -> we can use a tuple to pass it to the method
img_h = np.hstack((img,img))
img_v = np.vstack((img,img))  # vertical stacking

# when stacking arrays, remember that they have to have the same dimension

# splitting arrays

lst = np.hsplit(img_v,5)     # horizontal split (need to be careful when you split it. If size is 5h 7v, you cannot split 5/3 -> error)
lst = np.vsplit(img_v,2)     # vertical split (same attention)
