from random import random

inCircle = 0
Total=0
Precision=3000 # The higher it is, the more precise the result will be

for i in range(Precision):
    Total+=1
    if (random()**2)+(random()**2)<=1:
        inCircle+=1
print(inCircle/Total*4)