phonebook = {
	"Justin" : 5183898893,
	"Ana" : 5186981253,
	"Hanna" : 5188958099,
	"Leanne" : 5182818111
}
print(phonebook)

for name, number in phonebook.items():
	print("Phone number of %s is %d" % (name, number))

del phonebook["Hanna"]
print(phonebook)

phonebook["Mike"] = 5189515151
del phonebook["Ana"]

if "Mike" in phonebook:
	print("Mike is in the phonebook.")
if "Ana" not in phonebook:
	print("Ana has been removed.")

