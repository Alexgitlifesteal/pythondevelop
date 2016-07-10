#change directory to PH2150
from pylab import scatter,xlabel,ylabel,xlim,ylim,show
from numpy import loadtxt
import numpy as np
#crating an array of the stars txt file
HRdiagram = loadtxt("stardata.txt",float)
temperaturex = HRdiagram[:,0]
magnitudey = HRdiagram[:,1]

array1 = np.array([[temperaturex], [magnitudey]], float)

print array1
#creating an HR diagram using the data from the stars txt file
HRdiagram = loadtxt("stardata.txt",float)
x = HRdiagram[:,0]
y = HRdiagram[:,1]

scatter(x,y)
xlabel("Temperature, K")
ylabel("Magnitude")
xlim(0,13000)
ylim(-5,20)
show()
