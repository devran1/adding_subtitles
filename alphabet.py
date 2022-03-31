#!/usr/bin/env python3

import cv2
import numpy as np


"""
def alpha(letter):
    return letter
"""
#letters=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,R,Q,S,T,U,V,W,X,Y,Z]

#letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

#7x5
a=[
[0,0,0,0,0],
[0,1,1,1,0],
[0,0,0,1,0],
[0,1,1,1,0],
[0,1,0,1,0],
[0,1,1,1,0],   
[0,0,0,0,0]    
]

#make a an image every data must be a color
#letters=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,R,Q,S,T,U,V,W,X,Y,Z]

letters=[a]
"""
for _ in letters:
 
    if _[0][0]==0:
        _[0][0]=np.full((1,1,3), 255, dtype=np.uint8)
        #print("yes")
    print(_)
"""

for _ in letters:
    for i in range(7):
        for j in range(5):
            if _[i][j] ==0:
                #print("yes")
                #_[i][j]=np.full((1,1,3), 255)
                _[i][j]=[255,255,255]
            
            else:    
            #if _[i][j] ==1:
                _[i][j]=[0,0, 0,]

              
#print(a)
a =np.array(a,dtype=np.uint8)

cv2.imshow('white', a)
#    print(np.full((1,1,3), 255, dtype=np.uint8))



#if 0 make black (0,0,0)

#if 1 make white (255,255,255)


b=[
[0,0,0,0,0],
[0,1,0,0,0],
[0,1,0,0,0],
[0,1,1,1,0],
[0,1,0,1,0],
[0,1,1,1,0],
[0,0,0,0,0]
]




"""

c=[]

d=
e=
f=
g=
h=
i=
j=
k=
l=
m
n
o
p
q
r
s
t
u
v
w
x
y
z





A
B
C
D
E
F
G
H
I
J
K
L
M
N
O
P
Q
R
S
T
U
V
W
X
Y
Z

"""



cv2.waitKey(0) # waits until a key is pressed
cv2.destroyAllWindows() # destroys the window showing image

