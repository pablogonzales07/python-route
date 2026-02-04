
""" 
x = lambda a : a+ 10
print(x(5))

y = lambda a,b : a+b
print(y(5,10))
 """
def mi_funcion(n):
    return lambda a : a*n

duplicador = mi_funcion(2)
triplicador = mi_funcion(3)

print(duplicador(5)) #10
print(triplicador(5)) #15
