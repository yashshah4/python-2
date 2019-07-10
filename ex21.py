#defining a function that accepts two numbers and adds them to return the sum
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a+b
#defining a function that accepts two numbers and subtracts them to return the difference
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a-b
#defining a function that accepts two numbers and multiplies them to return the product   
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a*b
#defining a function that accepts two numbers and divides them to return the result
def  divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a/b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


print "Here is the puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"