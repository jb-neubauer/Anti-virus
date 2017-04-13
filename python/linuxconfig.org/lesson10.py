if (5 ** 2 >= 25):
	print("It's true!")
	print("If is great")

if( (5 **2 >= 25) and (4 * 2 < 8) or (35 / 7 > 4) ): 
	print("Booleans make If even more powerful")

if (not (5 ** 2 >= 25)):
	print("biarro")
else:
	print("Check your math")

if  ( ( 5 ** 2 <= 25) and (35 / 7 >4) and (4 ** 2 > 10) and (3 ** 2 < 10) ):
	print("Everything looks good.")
else:
	print("Your math is a little off")

if (5 ** 2 > 25):
	print("It is greater")
elif (5 ** 2 < 25):
	print("It is less")
elif (5 ** 2 == 25):
	print("It is equal")
else:
	print("That makes no sense")

a = 10
b = 15
c = 20
d = 25

if (a > b):
	if (a + b >= d):
		d -= c
	elif (a + b >= c):
		c -= b
	else:
		b -= a
elif (b > c):
	print(b - c)
else:
	print(d)
