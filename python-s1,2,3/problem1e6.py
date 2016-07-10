#PS1 ex6
fo = open("firstlaw.txt", "wb")
fo.write("In all cases in which work is produced by the agency of heat,a quantity of heat\nis consumed which is proportional to the work done; and conversely,by the\nexpenditure of an equal quantity of work an equal quantity of heat is produced.")
fo = open("firstlaw.txt", "r+")
str = fo.read()
print str [22:26]
print str
fo.close