from exceptions import LibroNoDisponible, UsuarioNoEncontradoError
from persistencia import Persistencia

persistencia = Persistencia()
biblioteca = persistencia.cargar_datos()

print("Bienvenido a Platzi Biblioteca")

print("Libros disponibles: ")
for libro in biblioteca.libros_disponibles:
    print(libro.descripcion_completa)
print()

try:
    cedula = input("Digite el numero de cedula: ")
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.nombre_completo)
except UsuarioNoEncontradoError as e:
    print(e)

titulo = input("Digite el titulo del libro: ")
try:
    libro = biblioteca.buscar_libro(titulo)
    print(f"El libro que seleccionaste es {libro} y esta disponible para el prestamo")
except LibroNoDisponible as e:
    print(e)

resultado = usuario.solicitar_libro(libro.titulo)
print(f"\n {resultado}")

try:
    resultado_prestar = libro.prestar()
    print(f"\n {resultado_prestar}")
except LibroNoDisponible as e:
    print(e)

persistencia.guardar_datos(biblioteca)

# result = Biblioteca.validar_isbn("1234567899")
# print(f"El isbn es valido: {resultado}")
