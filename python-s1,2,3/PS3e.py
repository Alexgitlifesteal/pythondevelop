from numpy import *
import random
PS3a = array([[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0]], float)
PS3b = arange(1,17).reshape((4,4))
PS3c = [random.random() for PS3c in range(0,16)]
PS3c = array(PS3c).reshape((4,4))
PS3e = PS3a + PS3b + PS3c
print PS3e # returns new array
print PS3e.item((2,3))#returns object at 4 across and row 3