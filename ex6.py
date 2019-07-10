#creating a string x with formatting method %d
x = "There are %d types of people." % 10
#creating further strings 
binary = "binary"
do_not = "don't"
#creating a second string with string formatting method
y = "Those who know %s and those who %s" %(binary, do_not)
#printing the first two strings
print x
print y
#using two printing methods below to highlight the difference between %r & %s
print "I said %r." %x
print "I also said : `%s`." % y
#further highlighting the usage of %r
hilarious = False
joke_evaluation = "Isnt't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side"
#concatenating two strings using '+'
print w + e