x = 2
print(x == 2) #prints true
print(x == 3) #prints false
print(x < 3) #prints true

#boolean
name = "Justin"
age = 34
if name == "Justin" and age == 34:
	print("Your name is Justin and your age is 34")

if name == "Justin" or name == "Jim":
	print("Your name is either Justin or Jim")

#in operator

if name in ["Justin", "Jim"]:
	print ("Your name is either Justin or Jim")

x = 2
if x == 2:
	print("x equals two")
else:
	print("x does not equal two")


#is operator
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y) #prints true
print(x is y) #prints false

#not operator
print(not False) #prints true
print((not False) == (False)) #prints false


#exercise

number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
	print("1")

if first_array:
	print("2")

if len(second_array) == 2:
	print("3")

if len(first_array) + len(second_array) == 5:
	print("4")

if first_array and first_array[0] == 1:
	print("5")

if not second_number:
	print("6")
