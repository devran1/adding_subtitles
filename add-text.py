#!/usr/bin/env python3

import cv2
import numpy as np

import alphabet

#from alphabet import alpha

r,c = 360, 720


#numpy array
white = np.full((r,c,3), 255, dtype=np.uint8)
 
#show image
cv2.imshow('white', white)
 
#print(alphabet.a) # matrix

#letter_a=np.array((alphabet.a,3),255,dtype=np.uint8)

 

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

