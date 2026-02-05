
"""
Consultas para la tabla de autores.
"""
from config.database import create_connection

def get_all_autores():
    connection = create_connection("localhost", "root", "123456", "editorial_db")
    query = "SELECT * FROM autores"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    return cursor.fetchall()

