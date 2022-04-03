#!/usr/bin/env python3

import cv2
import numpy as np
import argparse

import alphabet

parser=argparse.ArgumentParser(description="adds text to images")
#about picture
parser.add_argument("picture", help="picture which needs the subtitles", type=str)
parser.add_argument("size", help=  "percentage of the image, default 40",type=int ,nargs='?',const=1,default=40)

#about text
parser.add_argument("x",help="x position for text, default 351",type=int,nargs='?',const=1,default=351)
parser.add_argument("y", help= "y position for text, default 2",type=int,nargs='?',const=1,default=2)
parser.add_argument("text",help="write for making subtitles",type=str)

args=parser.parse_args()
sentence=args.text

r,c = 360, 720

#position (how to default value  nargs='?',const=1,default=351), later(size of the text)<-----
#how to add to videos, later from videos extract subtitles


#making screen 360x720

pic=args.picture


# resize image


screen=cv2.imread(f"{pic}")

scale_percent = args.size #40

width = int(screen.shape[1] * scale_percent / 100)
height = int(screen.shape[0] * scale_percent / 100)
dim = (width, height)
  

screen = cv2.resize(screen, dim)

"""
#just for white picture

screen=[[0 for col in range(c)] for rows in range(r)] 
for i in range(r):
    for j in range(c):
        screen[i][j]=[255,255,255]
"""
            

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
            screen[args.x +i][ args.y +9*k +j] = eW[k][i][j]  
            pass

#arg.x=351 args.y=2

screen_array=np.array(screen,dtype=np.uint8)
cv2.imshow('white', screen_array)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
