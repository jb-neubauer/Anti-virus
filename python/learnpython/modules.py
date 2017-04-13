#finds all finctions in "re" with find in it and sorts them alpabetically
import re

find_members = []
for member in dir(re):
	if "find" in member:
		find_members.append(member)

print(sorted(find_members))
