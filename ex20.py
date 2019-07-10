from sys import argv

script, input_file = argv

#the function below takes the file as an input
#and then prints the entire file
def print_all(f):
    print f.read()
#the function below takes the file as an input and the seek function
#moves the read header to the first line
def rewind(f):
    f.seek(0)
#the function below takes the line number as input and prints the line 
#number as well as the content in that line
def print_a_line(line_count, f):
    print line_count, f.readline()

#accepting the input file from the user and storing it in current_file
current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

