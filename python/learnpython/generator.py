import random

def lottery():
# returns 6 numbers 1-72
	for i in range(6):
		yield random.randint(1, 72)

	# returns a 7th number between 1 and 40
		yield random.randint(1, 40)

for random_number in lottery():
	print("And the next number is .... %d!" %(random_number))

#switches the values of a and b
a=1
b=2
a, b = b, a
print(a, b)



# fibonacci sequence first 100 values
def fib():
	a, b = 1, 1
	while 1:
		yield a
		a, b = b, a +b

import types
if type(fib()) == types.GeneratorType:
	print("Good, the fib function is a generator.")

	counter = 0
	for n in fib():
		print(n)
		counter += 1
		if counter == 100:
			break

