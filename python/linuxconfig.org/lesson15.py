def print_hello():
	print("Hello World!")

print_hello()

new_list = [[2, 4, 6], [3, 6, 9], [4, 8, 12]]
for list in new_list:
	for x in list:
		print(x)
		print_hello()

def square(x):
	return x ** 2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
for number in numbers:
	print(square(number))


def multiply_numbers(x, y):
	return x * y
print(multiply_numbers(5, 4))


