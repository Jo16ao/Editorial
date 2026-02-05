class Libro:
    def __init__(self, titulo, isbn, año_publicacion=None, precio=None, paginas=None, id_editorial=None, id_categoria=None, autores=[]):#funcion de llamada
        self.titulo = titulo
        self.isbn = isbn
        self.año_publicacion = año_publicacion
        self.precio = precio
        self.paginas = paginas
        self.id_editorial = id_editorial
        self.id_categoria = id_categoria
        self.autores = autores  # Lista de IDs de autores

        