from sys import argv

# This prompts for values to be added using raw_input
script, first, second, third = argv, raw_input("Enter first value: "), raw_input("Enter second value: "), raw_input("Enter third value: " )


print "This script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

