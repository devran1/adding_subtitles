#!/usr/bin/env python3

import cv2
import numpy as np
import argparse

import alphabet

parser=argparse.ArgumentParser(description="adds text to images")
parser.add_argument("text",help="write for making subtitles",type=str)

args=parser.parse_args()
sentence=args.text

r,c = 360, 720


#making screen 360x720
screen=[[0 for col in range(c)] for rows in range(r)] 
for i in range(r):
    for j in range(c):
        screen[i][j]=[255,255,255]

            

def word_picture(sentence):
    pics=[]
    for word in sentence:     
        if word.isspace():
            new_word=alphabet.empty
            each_word=alphabet.word_coloring(new_word)
            each_W=np.array(each_word,dtype=np.uint8)
            pics += [each_W]
                
        else:   

            i=alphabet.letters_list.index(f"{word}")
            new_word=alphabet.letters[i]
            each_word=alphabet.word_coloring(new_word)
            each_W=np.array(each_word,dtype=np.uint8)
            pics += [each_W]
    return pics 


eW = word_picture(sentence) 

for k in range(len(eW)):
    for i in range(9):
        for j in range(9):    
            screen[351+i][2 +9*k +j] = eW[k][i][j]  
            pass


screen_array=np.array(screen,dtype=np.uint8)
cv2.imshow('white', screen_array)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
