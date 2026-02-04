
texto = "Trabajando con este texto"

#slice
slicing = texto[0:10]
print(slicing)
slicing = texto[:10]
print(slicing)
slicing = texto[10:]
print(slicing)
slicing = texto[:-2]
print(slicing)
slicing = texto[10:-2]
print(slicing)

#replace
replace = texto.replace("texto", "texto modificado")
print(replace)

#split
split = texto.split(" ")
print(split)