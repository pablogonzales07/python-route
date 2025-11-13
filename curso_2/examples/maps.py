numbers = [1, 2, 3, 4, 5]
cuadrados:list[int] = []

for num in numbers:
    cuadrados.append(num**2)

print(numbers)
print(cuadrados)

def cuadrado(num:int) ->int:
    return num ** 2


cuadrados_map = list(map(cuadrado, numbers))
print(cuadrados_map)