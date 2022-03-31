#!/usr/bin/env python3

import cv2
import numpy as np

import alphabet

#from alphabet import *


import argparse


parser=argparse.ArgumentParser(description="adds text to images")
parser.add_argument("text",help="add video file to rotate",type=str)

args=parser.parse_args()


sentence=args.text

for word in sentence:

    i=alphabet.letters_list.index(f"{word}")
    print(i)
    new_word=alphabet.letters[i]


    each_word=alphabet.words(new_word)
    
    each_W=np.array(each_word,dtype=np.uint8)
    
    #cv2.imshow('white', each_W)


#from alphabet import alpha

r,c = 360, 720


#numpy array
white = np.full((r,c,3), 255, dtype=np.uint8)
 
#show image
#cv2.imshow('white', white)

#print(alphabet.a) # matrix

#letter_a=np.array((alphabet.a,3),255,dtype=np.uint8)

 

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

