import json
import pickle
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))

def add_employee(salaries_json, name, salary):
	salaries = json.loads(salaries_json)
	salaries[name] = salary

	return json.dumps(salaries)

salaries = '{"Justin" : 820, "Ana" : 870 }'
new_salaries = add_employee(salaries, "Me", 1020)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Justin"])
print(decoded_salaries["Ana"])
print(decoded_salaries["Me"])
