height = int(raw_input("Enter the height in meters: "))
print "Thank You"
time = int(raw_input("Enter the time interval in seconds: "))
print "Thank You"
a = 9.81
x = (a * time ** 2) / 2
print " The height of the ball is ", height - x, " meteres from the ground."