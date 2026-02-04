
texto = "Hi i'm Pablo"
texto2 = "Supuestamente todo esta 'correcto'"

cantidadCaracteres = len(texto2)
print(cantidadCaracteres)

textoMultilinea = """Hola
soy 
un
comentario
multilinea 
"""
print(textoMultilinea)

texto = "Vamos a convertir este texto"

mayuculas = texto.upper()
print(mayuculas)
minusculas = texto.lower()
print(minusculas)

texto2 = "  Manipulando este string  "

palabraIncluida = "este" in texto2
palabraNoIncluida = "este" not in texto2
eliminoEspacios = texto2.strip()

print(palabraIncluida)
print(palabraNoIncluida)
print(eliminoEspacios)