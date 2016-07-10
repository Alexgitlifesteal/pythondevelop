from numpy import *
import random
PS3b = arange(1,17).reshape((4,4))
PS3f = PS3b*PS3b # multiply the array by itself
print PS3f
dotprod = dot(PS3b, PS3b)#dot product of PS3b
print dotprod
difference = subtract(dotprod, PS3f)#calculates difference between the two arrays
print difference