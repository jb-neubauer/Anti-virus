linux_distros = ['Debian', 'Ubuntu', 'Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
print(linux_distros[0])
print(linux_distros[3])
print(linux_distros[-2])
debian_distros = linux_distros[:2]
print(debian_distros)
rh_distros = linux_distros[2:4]
print(rh_distros)
rh_distros = linux_distros[-5:-3]
print(rh_distros)
linux_distros.insert(2, "Mint")
print(linux_distros)
linux_distros.remove("Mint")
print(linux_distros)
distros = ['Fedora', 'CentOS', 'OpenSUSE', 'Arch', 'Gentoo']
deb_distros = ['Debian', 'Ubuntu', 'Mint']
distros.extend(deb_distros)
print(distros)
print(len(linux_distros))
print(linux_distros[len(linux_distros) -1])
