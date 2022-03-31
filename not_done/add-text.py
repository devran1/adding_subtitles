#!/usr/bin/env python3

import cv2
import numpy as np

import alphabet


import argparse


parser=argparse.ArgumentParser(description="adds text to images")
parser.add_argument("text",help="add video file to rotate",type=str)

args=parser.parse_args()


sentence=args.text

def word_picture(sentence):

    for word in sentence:

        i=alphabet.letters_list.index(f"{word}")
        #print(i)
        new_word=alphabet.letters[i]


        each_word=alphabet.words(new_word)
        
        each_W=np.array(each_word,dtype=np.uint8)
        #print(each_W) #each word 7x7 place in 360x720
        
        #cv2.imshow('white', each_W)
    return each_W #return means bring it outside

eW = word_picture(sentence) # brings outside with assigned name

#print(eW[0][0])

r,c = 360, 720


#making screen 360x720
screen=[[0 for col in range(c)] for rows in range(r)] 

for i in range(r):
    for j in range(c):
        screen[i][j]=[255,255,255]

#screen_array=np.array(screen,dtype=np.uint8) #need to stay as last
#cv2.imshow('white', screen_array)

#where to put the text row 251-258 and 2 col (almost like 100 letters can fit)
#make the word smaller pixelly and will fit more 
#how to add
#add a letter like "a"   


for i in range(7):
    for j in range(7):
        screen[251+i][2+j] = eW[i][j] 
            #pass


screen[251][2]=eW[0][0]

"""
[255,,][,,][,,][][][][]
[255,,][,,][,,]
"""

screen_array=np.array(screen,dtype=np.uint8)
cv2.imshow('white', screen_array)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

