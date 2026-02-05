
"""
Script para crear la base de datos 'editorial_db' desde Python.
Ejecuta este script primero para asegurarte de que la base de datos exista.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.database import create_connection
from mysql.connector import Error

def create_database(connection, query):
    """
    Ejecuta una consulta SQL para crear una base de datos.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("✅ Base de datos creada exitosamente")
    except Error as e:
        print(f"❌ El error '{e}' ocurrió")

if __name__ == "__main__":
    # Conéctate al servidor MySQL sin especificar una base de datos
    connection = create_connection(
        host_name="localhost",
        user_name="root",
        user_password="123456"  # ¡Cambia esto por tu contraseña real!
    )
    # Define la consulta para crear la base de datos
    create_database_query = "CREATE DATABASE IF NOT EXISTS editorial_db"
    # Ejecuta la creación
    if connection is not None:
        create_database(connection, create_database_query)
        connection.close()
        print("🔌 Conexión cerrada")
