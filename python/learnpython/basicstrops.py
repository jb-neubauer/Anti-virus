#basic string operations
astring = "Hello world!"
astring2 = 'Hello world!'

print("single quotes are ' '")

print(len(astring))

#prints out the first occurrence of "o"
print(astring.index("o"))

#prints out the number of occurrences of "l"
print(astring.count("l"))

#prints out all letters between index 3 and ends at index 6
print(astring[3:7])

#prints out everyother letter between index 3 and 6
print(astring[3:7:2])

#prints the string in revers order
print(astring[::-1])

#prints the string in uppercase
print(astring.upper())

#prints the string in lowercase
print(astring.lower())

#checks to see if string starts with
print(astring.startswith("Hello"))

#checks to see if string ends with
print(astring.endswith("kdfjah"))

#splits the string 
affewwords = astring.split(" ")
print(affewwords)

#exercise
s = "Hey there, how long should string be?"
print("Length of s = %d" %len(s))

print("The first occurrance of g should be %d" % s.index("g"))

print("e occurrs %d times" % s.count("e"))

print("The first seven letters are '%s'" % s[:7])

print("The next three letters are '%s'" % s[7:10])

print("The eleventh letter is '%s'" % s[10])

print("The characters with odd indexes are '%s'" % s[1::2])

print("The last five characters are '%s'" % s[-5])

print("This string in uppercase: %s" % s.upper())

print("this string in lowercase: %s" % s.lower())

print("This string in title: %s" %s.title())

print("This string is now split: %s" % s.split(" "))
