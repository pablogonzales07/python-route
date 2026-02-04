
edad = 17

if edad >= 18:
    print("Podés entrar al boliche")
elif edad >= 16:
    print("Podés entrar con autorización")
else:
    print("No podés entrar")

edad = 20
tiene_dni = True

if edad >= 18:
    if tiene_dni:
        print("Podés votar")
    else:
        print("Necesitás DNI para votar")
else:
    print("Sos menor de edad")

nota = 8

if nota >= 6 and nota <= 10:
    print("Aprobado")
else:
    print("Desaprobado")

edad = 20

if edad >= 18:
    pass  #después voy a poner el 
          #código acá
else:
    print("Es menor de edad")