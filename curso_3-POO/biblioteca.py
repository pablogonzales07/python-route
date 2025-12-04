from exceptions import BibliotecaError, LibroNoDisponible, UsuarioNoEncontradoError
from libros import LibroElectronico, LibroFisico


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    @property
    def libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

    def buscar_usuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(
            f"Cedula {cedula} no coincidente a ningun usuario del sistema"
        )

    def buscar_libro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower() and libro.disponible:
                return libro

        raise LibroNoDisponible(f"Libro {titulo} no disponbile o inexistente")

    def agregar_libro(self, tipo_libro, titulo, autor, isbn):
        if tipo_libro.lower() == "fisico":
            nuevo_libro = LibroFisico(titulo, autor, isbn)
            self.libros.append(nuevo_libro)
            return f"Libro {titulo} agregado correctamente"
        elif tipo_libro.lower() == "electronico":
            nuevo_libro = LibroElectronico(titulo, autor, isbn)
            self.libros.append(nuevo_libro)
            return f"Libro {titulo} agregado correctamente"
        else:
            return BibliotecaError("Tipo de libro incorrecto")
        
    @staticmethod
    def validar_isbn(isbn):
        return len(isbn) >=10
