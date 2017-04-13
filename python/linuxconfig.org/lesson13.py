new_dictionary = {}
distro_install_command = {'Debian': 'apt-get', 
			'Ubuntu': 'apt-get', 
			'Fedora': 'dnf', 
			'CentOS': 'yum', 
			'OpenSUSE': 'zypper', 
			'Arch': 'pacman', 
			'Gentoo': 'emerge'
}
print(distro_install_command['Gentoo'])

test_dict = {}
test_dict[3] = "Boat"
test_dict['Green'] = 42
test_dict['a list'] = [2,4,6,8,10]
other_dict = {'a': 1, 'b': 2, 'c': 3}
test_dict['a dict'] = other_dict
print(test_dict)
print(test_dict['a dict'])
print(test_dict['a list'][1])
test_dict = {}
test_dict[3] = "Boat"
test_dict['Green'] = 42
test_dict['a list'] = [2, 4, 6, 8, 10]
other_dict = {'a': 1, 'b': 2, 'c': 3}
test_dict['a dict'] = other_dict
print(test_dict)
print(test_dict['a dict'])
print(test_dict['a list'][1])

del distro_install_command['Ubuntu']
print(distro_install_command)
