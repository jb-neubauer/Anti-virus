for x in range(1, 11):
	print(x * 2)

times_two = []
for x in range(1, 11):
	times_two.append(x * 2)
	print(x * 2)

print(times_two)

linux_distros = ['Debian', 'Ubuntu', 'Mint', 'Fedora', 'CentOS', 'OpenSUSE', 'SlackWare', 'Arch', 'Gentoo']

distros_cap = []
for distro in linux_distros:
	print(distro.upper())
	distros_cap.append(distro.upper())

print(linux_distros)
print(distros_cap)

number_sets = [[2,4,6], [3,6,9], [4,8,12]]
square_sets = []
for number_set in number_sets:
	square_sets.append([])
	for number in number_set:
		print("The original number is %d, and the result is %d." % (number, number ** 2))
		square_sets[number_sets.index(number_set)].append(number **2)
print(square_sets)
