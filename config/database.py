
"""
Módulo de configuración para la conexión a la base de datos.
Centraliza los parámetros de conexión para facilitar el mantenimiento.
"""
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name=None):#creamos coneccion
    """
    Crea una conexión a la base de datos MySQL.
    Parámetros:
    host_name (str): Dirección del servidor (normalmente 'localhost').
    user_name (str): Nombre de usuario de MySQL.
    user_password (str): Contraseña del usuario.
    db_name (str, opcional): Nombre de la base de datos a la que conectar.
    Retorna:
    Connection: Objeto de conexión a la base de datos o None si falla.
    """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("✅ Conexión a MySQL DB exitosa")
    except Error as e:
        print(f"❌ El error '{e}' ocurrió")
    return connection


