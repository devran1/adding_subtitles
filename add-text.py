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

"""
empt=[(s.isspace(),sentence.index(s)) for s in sentence]    
if empt:

    #print(empt)
    point=[i for i in empt if i[0] == True]
    #print(point)
    print(point[1])
    
    #because the length of the letters is 7 multpily index by 7 and put empty in the picture 
    # than the rest will be replaced with +1 index
"""    

#making screen 360x720
screen=[[0 for col in range(c)] for rows in range(r)] 
for i in range(r):
    for j in range(c):
        screen[i][j]=[255,255,255]

#words=[word for word in sentence]
#print(words)


#why that gives black lines #duplicates gives black lines doesn't have to e in the same place
            

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
        #print(i) #new_word, each_W, each_word was black
        #print(pics)
#    print(pics)
            print(new_word)#problem is the function word_coloring
    return pics 

#    print(sentence.index(""))



#empt=[(s.isspace(),sentence.index(s)) for s in sentence]    
#print(empt)

"""
while empt==True:
    new_word=alphabet.empty
    each_word=alphabet.words(new_word)
    each_W=np.array(each_word,dtype=np.uint8)
    pics += [each_W]
"""

"""
    if i.isspace():
#        emp=sentence.index(f"{i}")
#        print(emp)
        print([s.isspace() for s in sentence])
"""

eW = word_picture(sentence) 
#print(eW)

for k in range(len(eW)):
    for i in range(7):
        for j in range(7):    
            screen[351+i][2 +7*k +j] = eW[k][i][j]  
            pass


screen_array=np.array(screen,dtype=np.uint8)
cv2.imshow('white', screen_array)

cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image
