
""" palabra = "Python"
 """
#Nombre que represente una unidad.
    #Es nbuena practica que la palabra sea facil de intuir su contenido
#El bucle recorre elemento por elemento
#Podemos romper el bucle con break
#Tambien podemos saltear iteracion con continue
#Podemos usar el else

""" palabra = "Python"
for letra in palabra:
    print(letra) """

""" print("-------------------------------")

adjetivos = ["Rica", "Saludable"]
frutas = ["Manzana", "Naranja", "Kiwi"]

for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo) """
#Tenemos dos estructuras una interna y otra externa
#Hace una vuelta del bucle externo incluyendo todas las vueltas deel bucle interno


""" for fruta in frutas:
    if fruta=="Naranja":
        continue
    print(fruta)
else:
    print("Ya finalizo el bucle") """

""" print("-------------------------------")
 """
#Range comienza en 0 y finaliza sin incluir numero ingresado
""" for i in range(10):
    print(i) """

""" for i in range(3,5):
    print(i) """

""" for i in range(0, 10,2):
    print(i) """


#Si no sabemos la intruccion de una estructura
#Podemos usar pass

""" for i in range(10):
    pass """

adjetivos = ["Rica", "Saludable"]
frutas = ["Manzana", "Naranja", "Kiwi"]

for fruta in frutas:
    for adjetivo in adjetivos:
        print(fruta, adjetivo)