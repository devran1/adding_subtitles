#!/usr/bin/env python3

import cv2
import numpy as np


"""
def alpha(letter):
    return letter
"""


#9x9




a=[
[0,0,0,0,0,0,0,0,0],    
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,1,1,0,0],
[0,0,0,1,1,1,1,0,0],
[0,0,1,1,0,1,1,0,0],   
[0,0,0,1,1,1,0,0,0],   
[0,0,0,0,0,0,0,0,0]
]

#make a an image every data must be a color


b=[
[0,0,0,0,0,0,0,0,0],   
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,1,1,1,1,0,0],
[0,0,1,1,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,1,1,1,1,0,0],
[0,0,0,0,0,0,0,0,0]
]






c=[
[0,0,0,0,0,0,0,0,0],    
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0],    
[0,0,0,0,0,0,0,0,0]
]

d=[
[0,0,0,0,0,0,0,0,0],      
[0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,0,0,0,0]  

]

e=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,1,1,1,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]


f=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,1,1,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0]    
]



g=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,1,1,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]

h=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,1,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],  
[0,0,0,0,0,0,0,0,0]    
]




i=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]

j=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]


k=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,1,0,0,0],
[0,0,0,1,1,0,0,0,0],
[0,0,0,1,1,0,0,0,0],
[0,0,0,1,0,1,0,0,0],  
[0,0,0,0,0,0,0,0,0]    
]


l=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0],  
[0,0,0,0,0,0,0,0,0]    
]


m=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,1,1,0,1,1,0,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],  
[0,0,0,0,0,0,0,0,0]    
]


n=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]
o=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,0,1,1,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]


p=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,1,1,0,0,0],
[0,0,0,1,0,0,1,0,0],
[0,0,0,1,0,0,1,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]


q=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]
    

r=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]



s=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,1,1,1,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]






t=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,1,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]



u=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,0,1,1,1,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




v=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,1,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  

]

w=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,0,1,1,0,1,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]


x=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,0,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




y=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,1,1,1,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]


z=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,1,1,1,1,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,1,1,1,1,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]



A=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],  
[0,0,0,0,0,0,0,0,0]    
]




B=[
[0,0,0,0,0,0,0,0,0],  
[0,1,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




C=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,1,1,1,1,0],
[0,0,1,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,0,1,1,1,1,1,0],    
[0,0,0,0,0,0,0,0,0]  
]




D=[
[0,0,0,0,0,0,0,0,0],  
[0,1,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




E=[
[0,0,0,0,0,0,0,0,0],  
[0,1,1,1,1,1,1,1,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,0],    
[0,0,0,0,0,0,0,0,0]  
]




F=[
[0,0,0,0,0,0,0,0,0],  
[0,1,1,1,1,1,1,1,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




G=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




H=[
[0,0,0,0,0,0,0,0,0],  
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],    
[0,0,0,0,0,0,0,0,0]  
]





I=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,1,1,1,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




J=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,1,0,0,1,0,0,0,0],
[0,0,1,1,0,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




K=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,1,0,0,0,0],
[0,0,1,1,0,0,0,0,0],
[0,0,1,0,1,0,0,0,0],
[0,0,1,0,0,1,0,0,0],
[0,0,1,0,0,0,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




L=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,1,1,1,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




M=[
[0,0,0,0,0,0,0,0,0],  
[0,1,0,0,0,0,0,1,0],
[0,1,1,0,0,0,1,1,0],
[0,1,0,1,0,1,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],    
[0,0,0,0,0,0,0,0,0]  
]




N=[
[0,0,0,0,0,0,0,0,0],  
[0,1,0,0,0,0,0,1,0],
[0,1,1,0,0,0,0,1,0],
[0,1,0,1,0,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,0,1,0,1,0],
[0,1,0,0,0,0,1,1,0],
[0,1,0,0,0,0,0,1,0],    
[0,0,0,0,0,0,0,0,0]  
]




O=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




P=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,1,1,1,1,0,0],
[0,0,1,0,0,0,0,1,0],
[0,0,1,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




Q=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,1,0,1,0],
[0,1,0,0,0,0,1,1,0],
[0,0,1,1,1,1,1,1,0],    
[0,0,0,0,0,0,0,0,0]  
]




R=[
[0,0,0,0,0,0,0,0,0],  
[0,1,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],    
[0,0,0,0,0,0,0,0,0]  
]




S=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,0,0],
[0,0,1,1,1,1,1,0,0],
[0,0,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




T=[
[0,0,0,0,0,0,0,0,0],  
[0,1,1,1,1,1,1,1,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




U=[
[0,0,0,0,0,0,0,0,0],  
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




V=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,0,1,1,1,0,0,0],
[0,0,0,0,1,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




W=[
[0,0,0,0,0,0,0,0,0],  
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,1,0,0,1,0,0,1,0],
[0,0,1,1,0,1,1,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




X=[
[0,0,0,0,0,0,0,0,0],  
[0,1,0,0,0,0,0,1,0],
[0,0,1,0,0,0,1,0,0],
[0,0,0,1,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,1,0,0,0],
[0,0,1,0,0,0,1,0,0],
[0,1,0,0,0,0,0,1,0],    
[0,0,0,0,0,0,0,0,0]  
]




Y=[
[0,0,0,0,0,0,0,0,0],  
[0,1,0,0,0,0,0,1,0],
[0,0,1,0,0,0,1,0,0],
[0,0,0,1,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],    
[0,0,0,0,0,0,0,0,0]  
]




Z=[
[0,0,0,0,0,0,0,0,0],  
[0,1,1,1,1,1,1,1,0],
[0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,0],    
[0,0,0,0,0,0,0,0,0]  
]

zero=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,1,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],   
[0,0,0,1,1,1,0,0,0],  
[0,0,0,0,0,0,0,0,0]    
]


one=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,1,0,0,0,0],
[0,0,0,1,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0],   
[0,0,0,1,1,1,0,0,0],  
[0,0,0,0,0,0,0,0,0]    
]


two=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,1,1,1,0,0],
[0,0,1,0,0,0,0,1,0],
[0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0,0],   
[0,0,1,1,1,1,1,1,0],  
[0,0,0,0,0,0,0,0,0]    
]

three=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0,0],
[0,0,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],   
[0,0,1,1,1,1,1,0,0],  
[0,0,0,0,0,0,0,0,0]    
]

four=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,1,1,0,0],
[0,0,0,0,1,0,1,0,0],
[0,0,0,1,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],
[0,1,1,1,1,1,1,1,0],
[0,0,0,0,0,0,1,0,0],   
[0,0,0,0,0,0,1,0,0],  
[0,0,0,0,0,0,0,0,0]    
]

five=[
[0,0,0,0,0,0,0,0,0],  
[0,1,1,1,1,1,1,1,0],
[0,1,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0],
[0,1,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],   
[0,0,1,1,1,1,1,0,0],  
[0,0,0,0,0,0,0,0,0]    
]

six=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,1,1,1,0,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,0,0,0],
[0,0,1,1,1,1,0,0,0],
[0,0,1,0,0,0,1,0,0],
[0,0,1,0,0,0,1,0,0],   
[0,0,0,1,1,1,0,0,0],  
[0,0,0,0,0,0,0,0,0]    
]

seven=[
[0,0,0,0,0,0,0,0,0],  
[0,1,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,1,0,0],
[0,0,0,0,0,1,0,0,0],
[0,0,0,0,1,0,0,0,0],
[0,0,0,1,0,0,0,0,0],   
[0,0,1,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0]    
]

eight=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,0,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],   
[0,0,1,1,1,1,1,0,0],  
[0,0,0,0,0,0,0,0,0]    
]


nine=[
[0,0,0,0,0,0,0,0,0],  
[0,0,1,1,1,1,1,0,0],
[0,1,0,0,0,0,0,1,0],
[0,1,0,0,0,0,0,1,0],
[0,0,1,1,1,1,1,1,0],
[0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,1,0],   
[0,0,1,1,1,1,1,0,0],  
[0,0,0,0,0,0,0,0,0]    
]

empty=[
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0],   
[0,0,0,0,0,0,0,0,0],  
[0,0,0,0,0,0,0,0,0]    
]


def word_coloring(word):

    for i in range(9):
        for j in range(9):
            if word[i][j] ==0:
                word[i][j]=[255,255,255]
            if word[i][j] ==1: 
                word[i][j]=[0,0, 0]
    return word




letters_list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]

letters=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,zero,one,two,three,four,five,six,seven,eight,nine]

#print(len(letters_list),len(letters))


