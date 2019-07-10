#importing the sys module
from sys import argv
#unpacking into two variables
script, filename = argv
#using open() func. to save the file content in txt variable
txt = open(filename)

print "Here's your file %r:" %filename
#printing the contents of the file txt
print txt.read()

txt.close()
