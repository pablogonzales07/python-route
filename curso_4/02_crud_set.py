set_countries = {"col", "mex", "bol"}

size = len(set_countries)
print(size)

print("col" in set_countries)

# add
set_countries.add("pe")
print(set_countries)
# update
set_countries.update(["ar", "br"])
print(set_countries)
# discard
set_countries.discard("col")
print(set_countries)
#remove
set_countries.remove("mex")
print(set_countries)
#pop
set_countries.pop()
#sorted
print(sorted(set_countries)) #Devuelve una LISTA ORDENADA