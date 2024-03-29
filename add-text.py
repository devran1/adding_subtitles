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




#picture name
pic=args.picture

screen=cv2.imread(f"{pic}")

#picture size
scale_percent = args.size #40
width = int(screen.shape[1] * scale_percent / 100)
height = int(screen.shape[0] * scale_percent / 100)
dim = (width, height)
  
#resized image
screen = cv2.resize(screen, dim)

"""
#just for white picture

#that was the screen size
r,c = 360, 720

screen=[[0 for col in range(c)] for rows in range(r)] 
for i in range(r):
    for j in range(c):
        screen[i][j]=[255,255,255]
"""
            
#writing every letter side by side from text

def word_picture(sentence):
    pics=[]
    #if there is white space between words add empty
    for word in sentence:     
        if word.isspace():
            new_word=alphabet.empty
            each_word=alphabet.word_coloring(new_word)
            each_W=np.array(each_word,dtype=np.uint8)
            pics += [each_W]
        
        # letters        
        else:   

            i=alphabet.letters_list.index(f"{word}")
            new_word=alphabet.letters[i]
            each_word=alphabet.word_coloring(new_word)
            each_W=np.array(each_word,dtype=np.uint8)
            pics += [each_W] #adding every letters' matrix value to the list
    return pics 


eW = word_picture(sentence) 

#adding the text to the picture 
for k in range(len(eW)):
    for i in range(9):
        for j in range(9):    
            screen[args.x +i][ args.y +9*k +j] = eW[k][i][j]  
            pass

#positons of the text arg.x=351 args.y=2
#matrix to image
screen_array=np.array(screen,dtype=np.uint8)
cv2.imshow('white', screen_array)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
