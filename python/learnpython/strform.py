#string formatting

#prints out "Hello Justin!!!"
name = "Justin"
print("Hello, %s!!!" % name)

# prints out "Justin is 34 years old."
name = "Justin"
age = 34
print("%s is %d years old." %(name, age))

# this prints out a list:[1,2,3]
mylist = [1, 2, 3]
print("A list: %s" % mylist)

# exercise
data = ("Justin", "Neubauer", 53.44)
format_string = "Hello %s %s. Your balance is $%s."
print(format_string % data)
