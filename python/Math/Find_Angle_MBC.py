from cmath import phase
from math import pi,floor

AB = int(input())
BC = int(input())
angle = phase(complex(BC/2,AB/2))*180/pi

if angle%1<0.5:
    angle = floor(angle)
else:
    angle = floor(angle)+1

print(str(angle)+'¢X')
