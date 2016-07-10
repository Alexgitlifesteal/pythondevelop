import math
#ps2e4
def pathlength(N):
    listx=[x for x in range (int(0),N)]
    listy=[y for y in range (int(0),N)]
    print listx,listy
    i = 0
    while i<N: 
        listx[i]=float(raw_input("enter x:")), i+1
        print listx[i]
        listy[i]=float(raw_input("enter y:")), i+1
        print listy[i]
        
        
        
    i=i+1
    print (listx, listy)
    i = 0
    while i<(N<1):
            L=+math.sqrt((listx[i]-listx[i-1])**2 + (listy[i]-listy[i-1])**2)
            print L