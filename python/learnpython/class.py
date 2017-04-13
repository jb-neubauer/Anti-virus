#accessing object variables
class MyClass:
	variable = "blah"

	def function(self):
		print("This is a message inside the class.")

myobjectx = MyClass()
myobjectx.variable
print(myobjectx.variable)

class MyClass:
	variable = "blah"
	
	def function(self):
		print("This is a message inside the class.")

myobjectx = MyClass()
myobjecty = MyClass()

myobjecty.varuable = "yackity"
print(myobjectx.variable)
print(myobjecty.variable)

class MyClass:
	variable = "blah"

	def function(self):
		print("This is a message inside the class")

myobjectx = MyClass()

myobjectx.function()

class Vehicle:
	name = ""
	kind = "car"
	color = ""
	value = 100.00
	def description(self):
		desc_str = "%s is a %s %s worth $%.2f." %(self.name, self.color, self.kind, self.value)
		return desc_str

car1 = Vehicle()
car1.name = "Camaro"
car1.color = "Silver"
car1.kind = "Super Sport"
car1.value = 58000.00

car2 = Vehicle()
car2.name = "X30"
car2.color = "Silver"
car2.kind = "luxery"
car2.value = 52000.00

print(car1.description())
print(car2.description())

