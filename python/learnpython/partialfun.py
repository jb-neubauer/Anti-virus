from functools import partial

#*returns 8*
def multiply(x, y):
	return x * y

#create function that multiplies by two 
dbl = partial(multiply, 2)
print(dbl(4))

#create function that multiplies by two
tri= partial(multiply, 3)
print(tri(4))


def func(u, v, w, x):
	return u*4 + v*3 + w*2 + x
p = partial(func, 5, 6, 7)
print(p(8))
