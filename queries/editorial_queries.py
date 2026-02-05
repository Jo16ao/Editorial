
"""
Consultas para la tabla de editoriales.
"""
from config.database import create_connection

def get_all_editoriales():
    connection = create_connection("localhost", "root", "123456", "editorial_db")
    query = "SELECT * FROM editoriales"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(query)
    return cursor.fetchall()