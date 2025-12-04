class BibliotecaError(Exception):
    pass

class TituloInvalidoError(BibliotecaError):
    pass

class UsuarioNoEncontradoError(BibliotecaError):
    """Usuario no encontrado en el sistema"""
    pass

class LibroInvalido(BibliotecaError):
    """Tipo de libro invalido"""
    pass

class LibroNoDisponible(BibliotecaError):
    """Libro no disponible para prestamo"""
    pass