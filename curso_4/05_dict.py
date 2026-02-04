
""" dict = {}
for i in range(1, 5):
    dict[i] = i * 2

print(dict)

dict= {i:i*2 for i in range(1,5)}


dict_2 = {i: i * 2 for i in range(1, 5)}
print(dict_2)  """

'''
import random

countries = ['col', 'mex', 'bol', 'pe']
population = {}

for country in countries:
    population[country] = random.randint(1, 100)
print(population)

population_2 = {
    country: random.randint(1, 100)
    for country in countries
}
print(population_2)
'''

names = ['nico', 'zule', 'santi']
ages = [12, 56,98]

""" users = {
    name: age
    for (name, age) in zip(names, ages)
}
print(users) """

