try:
    print(0/0)
    assert 1 != 1, 'Uno no es igual que uno'
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print('Imprime', error)
except Exception as error:
    print(error) 



""" try:
    assert 1 != 1, 'Uno no es igual que uno'
    print(0/0)
except AssertionError as error:
    print('Imprime', error)

try:
    age = 10
    if age < 18:
        raise Exception('No se permiten menores de edad')
except Exception as error:
    print(error)  """