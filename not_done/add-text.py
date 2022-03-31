#!/usr/bin/env python3

import cv2
import numpy as np

import alphabet


import argparse


parser=argparse.ArgumentParser(description="adds text to images")
parser.add_argument("text",help="add video file to rotate",type=str)

args=parser.parse_args()


sentence=args.text

r,c = 360, 720


#making screen 360x720
screen=[[0 for col in range(c)] for rows in range(r)] 

for i in range(r):
    for j in range(c):
        screen[i][j]=[255,255,255]

#pics=[]
#print(len(sentence))
def word_picture(sentence):
    pics=[]
    for word in sentence:
        
        i=alphabet.letters_list.index(f"{word}")
        print(i,word)
        new_word=alphabet.letters[i]
        each_word=alphabet.words(new_word)
        each_W=np.array(each_word,dtype=np.uint8)
        pics += [each_W]
        #print(each_W) #each word 7x7 place in 360x720
    #351+7*k 2+7*k len of k 7
    #adding word
        
                #cv2.imshow('white', each_W)
        #print(names)     
    #print(len(pics))    
    
    """
    #for a in pics:
    
    for a in range(len(pics)):
        
        for b in pics[a]:
            for i in range(7):
                #print(b[i])
                pass
    """                
      
        
       
                #print(a[i][j]) 
        
        



    """
    for i in range(7):
            for j in range(7):
                for k in range(len(sentence)):
                    screen[351+i][2 +7*k +j] = each_W[i][j]      
    """
    return pics #each_W  #screen #return means bring it outside


eW = word_picture(sentence) # brings outside with assigned name
print(len(eW))
print(eW)
#screen_=word_picture(sentence)
#print(eW[0][0])   
#wlist=word_picture(sentence)

for k in range(len(eW)):
    #print(k)
    for i in range(7):
        for j in range(7):    
            screen[351+i][2 +7*k +j] = eW[k][i][j]  
            pass

#screen_array=np.array(screen,dtype=np.uint8) #need to stay as last
#cv2.imshow('white', screen_array)

#where to put the text row 251-258 and 2 col (almost like 100 letters can fit)
#make the word smaller pixelly and will fit more 
#how to add
#add a letter like "a"   


            #pass


#new thing is add all the letters return all the letters
#return letters recursively #
#add letters recursively #?


#screen[251][2]=eW[0][0]

"""
[255,,][,,][,,][][][][]
[255,,][,,][,,]
"""




screen_array=np.array(screen,dtype=np.uint8)
cv2.imshow('white', screen_array)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
