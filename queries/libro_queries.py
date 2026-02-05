
"""
Módulo con consultas CRUD para la tabla de libros.
"""
from config.database import create_connection
from mysql.connector import Error

def execute_read_query(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)  # Devuelve dicts para facilidad
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"❌ El error '{e}' ocurrió")
        return None

def execute_write_query(connection, query, params):
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        connection.commit()
        print("✅ Operación exitosa")
    except Error as e:
        print(f"❌ El error '{e}' ocurrió")

def get_all_libros():
    connection = create_connection("localhost", "root", "123456", "editorial_db")
    query = "SELECT * FROM libros"
    return execute_read_query(connection, query)

def get_libros_by_titulo(titulo):
    connection = create_connection("localhost", "root", "123456", "editorial_db")
    query = "SELECT * FROM libros WHERE titulo LIKE %s"
    params = (f"%{titulo}%",)
    return execute_read_query(connection, query, params)

def update_libro_precio(id_libro, nuevo_precio):
    """Actualiza el precio de un libro específico."""
    connection = create_connection("localhost", "root", "123456", "editorial_db")
    query = "UPDATE libros SET precio = %s WHERE id_libro = %s"
    params = (nuevo_precio, id_libro)
    execute_write_query(connection, query, params)

def delete_libro(id_libro):
    """Elimina un libro de la base de datos."""
    connection = create_connection("localhost", "root", "123456", "editorial_db")
    query = "DELETE FROM libros WHERE id_libro = %s"
    params = (id_libro,)
    execute_write_query(connection, query, params)

def get_libro_details_with_join(id_libro):
    """
    Obtiene los detalles completos de un libro usando JOINs.
    """
    connection = create_connection("localhost", "root", "123456", "editorial_db")
    query = """
    SELECT l.titulo, l.isbn, l.año_publicacion, l.precio, e.nombre AS editorial, c.nombre AS categoria,
           GROUP_CONCAT(CONCAT(a.nombre, ' ', a.apellido) SEPARATOR ', ') AS autores
    FROM libros l
    LEFT JOIN editoriales e ON l.id_editorial = e.id_editorial
    LEFT JOIN categorias c ON l.id_categoria = c.id_categoria
    LEFT JOIN libro_autor la ON l.id_libro = la.id_libro
    LEFT JOIN autores a ON la.id_autor = a.id_autor
    WHERE l.id_libro = %s
    GROUP BY l.id_libro
    """
    params = (id_libro,)
    return execute_read_query(connection, query, params)