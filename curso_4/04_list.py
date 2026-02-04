""" # Estructura con for tradicional
numbers = []
for element in range(1, 11):
    numbers.append(element * 2)


print(numbers)

# Estructura utilizando list comprehensions
numbers_2 = [element * 2 for element in range(1, 11)]

print(numbers_2)
 """


even_numbers = []
for number in range(1, 11):
    if number % 2 ==0:
        even_numbers.append(number * 2)
print(even_numbers)

even_numbers2 = [
    number * 2 
    for number in range(1, 11)
    if number % 2 == 0
]
print(even_numbers2)

