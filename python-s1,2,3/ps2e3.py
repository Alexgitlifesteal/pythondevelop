import math
def area(vertices):
    x1,y1 = vertices[0]
    x2,y2 = vertices[1]
    x3,y3 = vertices[2]
    
x1 = int(raw_input("Enter x1 value: "))
y1 = int(raw_input("Enter y1 value: "))
x2 = int(raw_input("Enter x2 value: "))
y2 = int(raw_input("Enter y2 value: "))
x3 = int(raw_input("Enter x3 value: "))
y3 = int(raw_input("Enter y3 value: "))

A = 0.5*((x2*y3) - (x3*y2) - (x1*y3) + (x3*y1) + (x1*y2) - (x2*y1))
print A
