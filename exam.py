from datetime import datetime
# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.__nombre = nombre  # Encapsulamiento
        self.__id_usuario = id_usuario
    def buscar_autor(self, autor, catalogo):
        """Busca libros por autor en el catálogo."""
        catalogo.buscar_libros_disponibles(autor)
    def realizar_prestamo(self, libro, catalogo, prestamos):
        """Realiza un préstamo si el libro está disponible."""
        try:
            if libro not in catalogo.lista_libros:
                raise Exception("El libro no pertenece al catálogo.")  # Manejo de errores
            if not libro.estado:
                raise Exception("El libro no está disponible.")  # Manejo de errores
            prestamo = Prestamo(self, libro)  # Uso de encapsulación
            prestamos.registrar_prestamo(prestamo)
            catalogo.actualizar_catalogo(libro)
            print("Préstamo realizado con éxito.")
        except Exception as e:
            print(f"Error al realizar el préstamo: {e}")  # Manejo de errores
# Clase Catalogo
class Catalogo:
    def __init__(self):
        self.lista_libros = []
    def agregar_libro(self, libro):
        """Agrega un libro al catálogo."""
        self.lista_libros.append(libro)
    def buscar_libros_disponibles(self, autor):
        """Lista los libros disponibles de un autor."""
        libros_encontrados = [libro for libro in self.lista_libros if libro.autor == autor and libro.estado]
        if libros_encontrados:
            print("Libros disponibles:")
            for libro in libros_encontrados:
                print(f"- {libro.titulo}")
        else:
            print(f"No hay libros disponibles del autor {autor}.")
    def actualizar_catalogo(self, libro):
        """Actualiza el estado del libro en el catálogo."""
        libro.estado = False
# Clase LibrosDisponibles
class LibrosDisponibles:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = True
# Clase Prestamo
class Prestamo:
    def __init__(self, usuario, libro):
        self.usuario = usuario
        self.libro = libro
        self.fecha_inicio = datetime.now()
        self.fecha_fin = None
    def registrar_prestamo(self):
        """Registra la información del préstamo."""
        self.fecha_fin = datetime.now()
        print(f"Préstamo registrado: {self.libro.titulo} para {self.usuario._Usuario__nombre}.")
# Clase Prestamos (Maneja múltiples préstamos)
class Prestamos:
    def __init__(self):
        self.lista_prestamos = []
    def registrar_prestamo(self, prestamo):
        """Registra un préstamo en la lista."""
        self.lista_prestamos.append(prestamo)
        prestamo.registrar_prestamo()
# Clase UsuarioAdmin Herencia
class UsuarioAdmin(Usuario):
    def __init__(self, nombre, id_usuario, permisos):
        super().__init__(nombre, id_usuario)  # Herencia
        self.__permisos = permisos  # Encapsulación
    def agregar_libro_catalogo(self, libro, catalogo):
        """Permite a un administrador agregar libros al catálogo."""
        catalogo.agregar_libro(libro)
        print(f"Libro '{libro.titulo}' agregado por el administrador {self._Usuario__nombre}.")
# --- Ejemplo de Uso ---
# Crear catálogo y libros
catalogo = Catalogo()
libro1 = LibrosDisponibles("Libro A", "Autor 1")
libro2 = LibrosDisponibles("Libro B", "Autor 1")
catalogo.agregar_libro(libro1)
catalogo.agregar_libro(libro2)
# Crear usuario
usuario = Usuario("Juan Pérez", 1)
# Crear administrador (Herencia)
admin = UsuarioAdmin("Admin Loan", 999, permisos="todos")
# Crear sistema de préstamos
prestamos = Prestamos()
# Buscar libros y realizar préstamo
usuario.buscar_autor("Autor 1", catalogo)
usuario.realizar_prestamo(libro1, catalogo, prestamos)
# Intentar realizar un préstamo con un libro ya prestado
usuario.realizar_prestamo(libro1, catalogo, prestamos)
# Agregar un libro al catálogo como administrador
libro3 = LibrosDisponibles("Libro C", "Autor 2")
admin.agregar_libro_catalogo(libro3, catalogo)