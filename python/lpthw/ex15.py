#lines 1, 3 get the file name
from sys import argv

script, filename = argv

#opens the file
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again: "
file_again = raw_input("-> ")

txt_again = open(file_again)

print txt_again.read()
