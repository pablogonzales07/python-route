import random

countries = ['col', 'mex', 'bol', 'pe']

population_2 = {
    country: random.randint(1, 100)
    for country in countries
}
print(population_2)

result = {
    country: population 
    for (country, population) in population_2.items()
    if population >20
}

print(result)


text = 'Hola soy Pablo'

unique = {
    c: text.count(c)
    for c in text
    if c.lower() in ('aeiou')
}

print(unique)

