
"""
Script para crear todas las tablas necesarias en la base de datos editorial_db.
Ejecuta este script después de haber creado la base de datos.
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.database import create_connection
from mysql.connector import Error

def execute_query(connection, query):
    """
    Ejecuta una consulta SQL en la base de datos.
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("✅ Consulta ejecutada exitosamente")
    except Error as e:
        print(f"❌ El error '{e}' ocurrió")

# Definición de las tablas
create_editoriales_table = """
CREATE TABLE IF NOT EXISTS editoriales (
    id_editorial INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    telefono VARCHAR(20),
    email VARCHAR(100),
    fecha_fundacion DATE
);
"""

create_categorias_table = """
CREATE TABLE IF NOT EXISTS categorias (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion TEXT
);
"""

create_autores_table = """
CREATE TABLE IF NOT EXISTS autores (
    id_autor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    nacionalidad VARCHAR(50),
    fecha_nacimiento DATE,
    biografia TEXT
);
"""

create_libros_table = """
CREATE TABLE IF NOT EXISTS libros (
    id_libro INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    isbn VARCHAR(20) UNIQUE,
    año_publicacion INT,
    precio DECIMAL(10, 2),
    paginas INT,
    id_editorial INT,
    id_categoria INT,
    FOREIGN KEY (id_editorial) REFERENCES editoriales(id_editorial),
    FOREIGN KEY (id_categoria) REFERENCES categorias(id_categoria)
);
"""

create_libro_autor_table = """
CREATE TABLE IF NOT EXISTS libro_autor (
    id_libro INT,
    id_autor INT,
    PRIMARY KEY (id_libro, id_autor),
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro) ON DELETE CASCADE,
    FOREIGN KEY (id_autor) REFERENCES autores(id_autor) ON DELETE CASCADE
);
"""

if __name__ == "__main__":
    connection = create_connection(
        host_name="localhost",
        user_name="root",
        user_password="123456",  # ¡Cambia esto!
        db_name="editorial_db"
    )
    if connection is not None:
        print("🔄 Creando tablas...")
        execute_query(connection, create_editoriales_table)
        execute_query(connection, create_categorias_table)
        execute_query(connection, create_autores_table)
        execute_query(connection, create_libros_table)
        execute_query(connection, create_libro_autor_table)
        print("🎉 ¡Todas las tablas fueron creadas exitosamente!")
        connection.close()
        print("🔌 Conexión cerrada")