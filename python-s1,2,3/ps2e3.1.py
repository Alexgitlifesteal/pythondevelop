import math
def area(vertices):
    x1,y1 = vertices[0]
    x2,y2 = vertices[1]
    x3,y3 = vertices[2]
   
x1 = 0
y1 = 0
x2 = 1
y2 = 0
x3 = 0
y3 = 2

A = 0.5*((x2*y3) - (x3*y2) - (x1*y3) + (x3*y1) + (x1*y2) - (x2*y1))
#arbitary triangle code
print A 


