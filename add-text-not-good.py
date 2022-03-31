#!/usr/bin/env python3
import numpy as np
from PIL import Image

r,c=360,720
row=np.zeros([r,1,3],dtype=int) # 720 times (0 0 0)
col=np.zeros([1,c,3],dtype=int)

matris=row*col
matris=matris + 255
#print(matris.shape)

img = Image.fromarray(matris, 'RGB')
img.show()

#print(row)
#print(col)
#print(matris)

