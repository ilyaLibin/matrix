from plotting import plot
from image import *
from math import e, pi
import time

I = color2gray(file2image('img01.png'))

r = len(I)
c = len(I[0])

M = [x + y*1j for x in range(c) for y in range(r) if I[r-y-1][x] < 120]

#plot([z - (c/2 + (r/2)*1j) for z in M], max(r, c), 1)
#plot([e**(t*2*pi*1j/20) for t in range(20)])

plot([e**(2*pi*1j/3)* z for z in M], r, 1)
time.sleep(4)