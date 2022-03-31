#!/usr/bin/env python3

import cv2
import numpy as np

import alphabet


import argparse


parser=argparse.ArgumentParser(description="adds text to images")
parser.add_argument("text",help="add video file to rotate",type=str)

args=parser.parse_args()


sentence=args.text

for word in sentence:

    i=alphabet.letters_list.index(f"{word}")
    #print(i)
    new_word=alphabet.letters[i]


    each_word=alphabet.words(new_word)
    
    each_W=np.array(each_word,dtype=np.uint8)
    #print(each_W) #each word 7x7 place in 360x720
    
    #cv2.imshow('white', each_W)


r,c = 360, 720


#making screen 360x720
screen=[[0 for col in range(c)] for rows in range(r)] 

for i in range(r):
    for j in range(c):
        screen[i][j]=[255,255,255]

screen_array=np.array(screen,dtype=np.uint8)
cv2.imshow('white', screen_array)



cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

