from typing import Protocol

from exceptions import LibroNoDisponible


class LibroProtocol(Protocol):
    def prestar(self) -> str:
        """Metodo necesario para cualquier clase que quiera prestar un libro"""
        ...

    def devolver(self) -> str:
        """Metodo necesario para devolver un libro"""
        ...

    def calcular_duracion(self) -> str:
        """Metodo necesario para calcular la duracion de un prestamo"""
        ...


class Libro:
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__veces_prestado = 0

    @classmethod
    def crear_no_disponible(cls, titulo, autor, isbn):
        return cls(titulo, autor, isbn, disponible=False)

    def __str__(self):
        return f"Mi libro: {self.titulo} -- {self.autor} -- {'Esta disponible' if self.disponible else 'No esta diponible'} -- {self.isbn}"

    def prestar(self):
        if not self.disponible:
            raise LibroNoDisponible(f"Libro de titulo: {self.titulo} no disponible")

        if self.disponible:
            self.disponible = False
            self.__veces_prestado += 1
            return f"{self.titulo} pestado exitosamente"

    def devolver(self):
        self.disponible = True

        return f"{self.titulo} devuelto y disponible nuevamente"

    @property
    def esPopular(self):
        return self.__veces_prestado > 5

    @property
    def veces_prestado(self):
        return self.__veces_prestado

    @veces_prestado.setter
    def veces_prestado(self, veces_prestado):
        if veces_prestado >0:
            self.__veces_prestado = veces_prestado
    
        raise ValueError("El valor de veces_prestado debe ser mayor a 0")

    @property
    def descripcion_completa(self):
        return f"{self.titulo} por {self.autor} (ISBN_ {self.isbn})"

class LibroFisico(Libro):
    def __init__(self, titulo, autor, isbn, disponible=True):
        super().__init__(titulo, autor, isbn, disponible)

    def calcular_duracion(self):
        return "7 dias"


class LibroElectronico(Libro):
    def __init__(self, titulo, autor, isbn, disponible=True):
        super().__init__(titulo, autor, isbn, disponible)

    def calcular_duracion(self):
        return "14 dias"
