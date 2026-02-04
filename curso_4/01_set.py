
set_countries = {"col", "mex", "bol", "bol"}
set_numbers = {1, 2, 2, 443, 23}
set_types = {1, "hola", False, 12.12}

print(set_countries)
print(set_numbers)
print(set_types)

print(type(set_countries))


set_from_string = set("hola")
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))

numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
list_numbers = list(set_numbers)
print(set_numbers)
print(list_numbers)