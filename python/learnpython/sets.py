print(set("My name is Justin and Justin is my name".split()))

a = set(["Justin", "Jeff", "Connor"])
print(a)
b = set(["Jeff", "Jill"])
print(b)

#shows up in both lists
a.intersection(b)
b.intersection(a)


# only appear once
a.symmetric_difference(b)
b.symmetric_difference(a)

#only 
a.difference(b)
b.difference(a)


