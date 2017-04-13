distro_install_command = {'Debian': 'apt-get',
			'Ubuntu': 'apt-get',
			'Fedora': 'dnf',
			'CentOS': 'yum',
			'OpenSUSE': 'zypper',
			'Arch': 'pacman',
			'Gentoo': 'emerge'
}
distro_install_list = distro_install_command.items()
print(distro_install_list)
print(distro_install_list[3][1])

distro_names = distro_install_command.keys()

for distro in distro_names:
	print(distro)

distro_commands = distro_install_command.values()
for command in distro_commands:
	print(command)


book_info = { 'title': 'Learning Python',
			'pages': 342,
			'pub_date': 'November 2016',
			'chapters': 14,
}
print("The book is called %(title)s, and it was released on %(pub_date)s.  It is %(pages)d pages long with %(chapters)d chapters." % book_info)

for distro in distro_install_command:
	print(distro)
for distro in distro_install_command:
	print("the distro is %s, and it uses the command %s." % (distro, distro_install_command[distro]))

for distro, command in distro_install_command.items():
	print("the distro is %s, and it uses the command %s." % (distro, command))
