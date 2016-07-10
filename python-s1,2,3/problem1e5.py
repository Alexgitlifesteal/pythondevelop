G = 6.67*10**-11
M = 5.97*10**24
R = 6371000
T = float(raw_input("Enter desired value for T in seconds: "));
h = ((G*M*T**2)/(4*(3.141592)**2))**1/3.-R
print ("The altitude required is",h, "meters")