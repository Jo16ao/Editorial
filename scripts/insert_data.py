"""
Script para insertar datos de ejemplo en la base de datos.
SIN LIMPIAR DATOS EXISTENTES - Solo añade datos nuevos
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.database import create_connection
from mysql.connector import Error

def execute_query_ignore(connection, query, values=None):
    """Ejecuta INSERT IGNORE para evitar errores de duplicados"""
    cursor = connection.cursor()
    try:
        
        if "INSERT INTO" in query.upper() and "INSERT IGNORE" not in query.upper():
            query = query.replace("INSERT INTO", "INSERT IGNORE INTO")
        
        if values:
            cursor.executemany(query, values)
        else:
            cursor.execute(query)
        
        connection.commit()
        print(f"✅ {cursor.rowcount} registros insertados/actualizados exitosamente")
    except Error as e:
        print(f"❌ Error: {e}")
        connection.rollback()

if __name__ == "__main__":
    connection = create_connection(
        host_name="localhost",
        user_name="root",
        user_password="123456",
        db_name="editorial_db"
    )
    
    if connection is not None:
        print("📝 Insertando datos de ejemplo (sin borrar existentes)...")
        print("ℹ️  Los duplicados serán ignorados automáticamente\n")
        
        # INSERTAR EDITORIALES (20 editoriales)
        insert_editoriales = """
        INSERT IGNORE INTO editoriales (nombre, direccion, telefono, email, fecha_fundacion)
        VALUES (%s, %s, %s, %s, %s)
        """
        editoriales_data = [
            ("Penguin Random House", "1745 Broadway, New York, USA", "+1 212-782-9000", "info@penguinrandomhouse.com", "1925-01-01"),
            ("HarperCollins", "195 Broadway, New York, USA", "+1 212-207-7000", "consumerservices@harpercollins.com", "1817-01-01"),
            ("Editorial Planeta", "Av. Diagonal 662-664, Barcelona, España", "+34 93 366 03 00", "info@planeta.es", "1949-01-01"),
            ("Santillana", "Av. de los Artesanos 6, Tres Cantos, Madrid", "+34 91 744 90 00", "informacion@santillana.es", "1960-01-01"),
            ("McGraw-Hill Education", "1325 Avenue of the Americas, NY, USA", "+1 212-904-2000", "customer.service@mheducation.com", "1888-01-01"),
            ("Pearson Education", "80 Strand, London, UK", "+44 20 7010 2000", "enquiries@pearson.com", "1844-01-01"),
            ("Oxford University Press", "Great Clarendon St, Oxford, UK", "+44 1865 556767", "enquiry@oup.com", "1586-01-01"),
            ("Cambridge University Press", "University Printing House, Cambridge, UK", "+44 1223 358331", "information@cambridge.org", "1534-01-01"),
            ("Editorial Alfaguara", "Torrelaguna 60, Madrid, España", "+34 91 744 90 60", "alfaguara@santillana.es", "1964-01-01"),
            ("Anaya", "Calle Juan I. Luca de Tena 15, Madrid", "+34 91 393 88 00", "atencioncliente@anaya.es", "1959-01-01"),
            ("Editorial Seix Barral", "Av. Diagonal 662-664, Barcelona", "+34 93 366 03 00", "seixbarral@planeta.es", "1911-01-01"),
            ("DeBolsillo", "Av. Diagonal 662-664, Barcelona", "+34 93 366 03 00", "debolsillo@planeta.es", "2001-01-01"),
            ("Simon & Schuster", "1230 Avenue of the Americas, NY, USA", "+1 212-698-7000", "consumer@simonandschuster.com", "1924-01-01"),
            ("Hachette Livre", "58 Rue Jean Bleuzen, Vanves, Francia", "+33 1 43 92 30 00", "contact@hachette-livre.fr", "1826-01-01"),
            ("Editorial Anagrama", "Pedró de la Creu 58, Barcelona", "+34 93 322 81 51", "anagrama@anagrama-ed.es", "1969-01-01"),
            ("Tusquets Editores", "Av. Diagonal 662-664, Barcelona", "+34 93 366 03 00", "tusquets@planeta.es", "1969-01-01"),
            ("Editorial Acantilado", "Carrer de les Camèlies 47, Barcelona", "+34 93 417 78 67", "acantilado@acantilado.es", "1999-01-01"),
            ("Cátedra", "Calle Juan I. Luca de Tena 15, Madrid", "+34 91 393 88 00", "catedra@anaya.es", "1973-01-01"),
            ("Alianza Editorial", "Calle Juan I. Luca de Tena 15, Madrid", "+34 91 393 88 00", "alianza@anaya.es", "1966-01-01"),
            ("RBA Libros", "Av. Diagonal 662-664, Barcelona", "+34 93 366 03 00", "info@rbalibros.com", "1981-01-01")
        ]
        execute_query_ignore(connection, insert_editoriales, editoriales_data)
        
        # INSERTAR CATEGORÍAS (15 categorías)
        insert_categorias = """
        INSERT IGNORE INTO categorias (nombre, descripcion)
        VALUES (%s, %s)
        """
        categorias_data = [
            ("Novela", "Ficción narrativa extensa"),
            ("Ensayo", "Textos de análisis y opinión"),
            ("Poesía", "Obras en verso y expresión lírica"),
            ("Teatro", "Obras dramáticas para representación"),
            ("Ciencia Ficción", "Ficción basada en ciencia y tecnología futura"),
            ("Fantasía", "Mundo imaginario con elementos mágicos"),
            ("Misterio", "Historias de detectives y suspenso"),
            ("Romance", "Historias de amor y relaciones"),
            ("Histórica", "Ficción ambientada en épocas pasadas"),
            ("Biografía", "Relato de la vida de una persona"),
            ("Infantil", "Literatura para niños"),
            ("Juvenil", "Literatura para adolescentes"),
            ("Científica", "Libros de divulgación científica"),
            ("Filosofía", "Estudio de problemas fundamentales"),
            ("Autoayuda", "Libros para desarrollo personal")
        ]
        execute_query_ignore(connection, insert_categorias, categorias_data)
        
        # INSERTAR AUTORES (25 autores )
        insert_autores = """
        INSERT IGNORE INTO autores (nombre, apellido, nacionalidad, fecha_nacimiento, biografia)
        VALUES (%s, %s, %s, %s, %s)
        """
        autores_data = [
            ("Gabriel", "García Márquez", "Colombia", "1927-03-06", "Premio Nobel de Literatura 1982, máximo exponente del realismo mágico"),
            ("Jane", "Austen", "Reino Unido", "1775-12-16", "Autora de novelas románticas clásicas de la literatura inglesa"),
            ("Mario", "Vargas Llosa", "Perú", "1936-03-28", "Premio Nobel de Literatura 2010, novelista y ensayista"),
            ("Isabel", "Allende", "Chile", "1942-08-02", "Escritora chilena conocida por 'La casa de los espíritus'"),
            ("Julio", "Cortázar", "Argentina", "1914-08-26", "Escritor e intelectual argentino, autor de 'Rayuela'"),
            ("Jorge Luis", "Borges", "Argentina", "1899-08-24", "Escritor de cuentos, ensayos y poesía, figura clave de la literatura"),
            ("Ernest", "Hemingway", "Estados Unidos", "1899-07-21", "Premio Nobel 1954, periodista y escritor del estilo iceberg"),
            ("George", "Orwell", "Reino Unido", "1903-06-25", "Escritor y periodista británico, autor de '1984' y 'Rebelión en la granja'"),
            ("J.K.", "Rowling", "Reino Unido", "1965-07-31", "Autora de la serie Harry Potter, una de las más vendidas de la historia"),
            ("Stephen", "King", "Estados Unidos", "1947-09-21", "Escritor de novelas de terror, suspenso y ciencia ficción"),
            ("Miguel de", "Cervantes", "España", "1547-09-29", "Autor de 'El ingenioso hidalgo Don Quijote de la Mancha'"),
            ("Federico García", "Lorca", "España", "1898-06-05", "Poeta y dramaturgo español, figura de la Generación del 27"),
            ("Pablo", "Neruda", "Chile", "1904-07-12", "Poeta chileno, Premio Nobel de Literatura 1971"),
            ("William", "Shakespeare", "Reino Unido", "1564-04-26", "Dramaturgo, poeta y actor inglés, considerado el escritor más importante"),
            ("Agatha", "Christie", "Reino Unido", "1890-09-15", "Escritora de novelas de misterio, la más vendida de todos los tiempos"),
            ("Fiodor", "Dostoievski", "Rusia", "1821-11-11", "Escritor ruso, autor de 'Crimen y castigo' y 'Los hermanos Karamazov'"),
            ("Leo", "Tolstoi", "Rusia", "1828-09-09", "Novelista ruso, autor de 'Guerra y paz' y 'Anna Karénina'"),
            ("Franz", "Kafka", "República Checa", "1883-07-03", "Escritor checo en lengua alemana, autor de 'La metamorfosis'"),
            ("Gabriela", "Mistral", "Chile", "1889-04-07", "Poetisa chilena, primera latinoamericana en ganar el Nobel de Literatura"),
            ("Carlos", "Ruiz Zafón", "España", "1964-09-25", "Escritor español conocido por 'La sombra del viento'"),
            ("Arturo", "Pérez-Reverte", "España", "1951-11-25", "Escritor y periodista español, autor de 'El capitán Alatriste'"),
            ("Ken", "Follett", "Reino Unido", "1949-06-05", "Escritor británico de novelas históricas y de suspense"),
            ("Dan", "Brown", "Estados Unidos", "1964-06-22", "Escritor estadounidense conocido por 'El código Da Vinci'"),
            ("Paulo", "Coelho", "Brasil", "1947-08-24", "Novelista brasileño, autor de 'El alquimista'"),
            ("Haruki", "Murakami", "Japón", "1949-01-12", "Escritor japonés, autor de 'Tokio blues' y 'Kafka en la orilla'"),
            ("Umberto", "Eco", "Italia", "1932-01-05", "Semiólogo y novelista italiano, autor de 'El nombre de la rosa'")
        ]
        execute_query_ignore(connection, insert_autores, autores_data)
        
        # INSERTAR LIBROS (30 libros)
        insert_libros = """
        INSERT IGNORE INTO libros (titulo, isbn, año_publicacion, precio, paginas, id_editorial, id_categoria)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        libros_data = [
            ("Cien Años de Soledad", "978-0307474728", 1967, 24.99, 417, 1, 1),
            ("Orgullo y Prejuicio", "978-0141439518", 1813, 12.50, 279, 2, 1),
            ("La ciudad y los perros", "978-8420471839", 1963, 18.95, 320, 3, 1),
            ("La casa de los espíritus", "978-9507315855", 1982, 21.99, 448, 4, 1),
            ("Rayuela", "978-8432216420", 1963, 22.50, 736, 5, 1),
            ("Ficciones", "978-8420674284", 1944, 15.99, 192, 6, 2),
            ("El viejo y el mar", "978-0684801223", 1952, 11.25, 127, 7, 1),
            ("1984", "978-0451524935", 1949, 9.99, 328, 8, 5),
            ("Harry Potter y la piedra filosofal", "978-8478884459", 1997, 19.95, 256, 9, 6),
            ("It", "978-1501142970", 1986, 25.50, 1138, 10, 7),
            ("Don Quijote de la Mancha", "978-8467034053", 1605, 29.99, 1056, 11, 1),
            ("Bodas de sangre", "978-8437604944", 1933, 8.99, 112, 12, 4),
            ("Veinte poemas de amor", "978-9507316531", 1924, 10.50, 96, 13, 3),
            ("Hamlet", "978-0140707342", 1603, 7.99, 148, 14, 4),
            ("Asesinato en el Orient Express", "978-0007119318", 1934, 14.75, 256, 15, 7),
            ("Crimen y castigo", "978-8420674208", 1866, 18.25, 592, 16, 1),
            ("Guerra y paz", "978-8420674215", 1869, 32.99, 1392, 17, 9),
            ("La metamorfosis", "978-8420674192", 1915, 6.99, 64, 18, 1),
            ("Desolación", "978-9561117466", 1922, 9.50, 128, 19, 3),
            ("La sombra del viento", "978-8408093108", 2001, 22.99, 576, 20, 1),
            ("El capitán Alatriste", "978-8420467993", 1996, 16.75, 256, 1, 9),
            ("Los pilares de la Tierra", "978-0451166890", 1989, 28.50, 973, 2, 9),
            ("El código Da Vinci", "978-0307474278", 2003, 19.99, 592, 3, 7),
            ("El alquimista", "978-0061122415", 1988, 13.25, 208, 4, 15),
            ("Tokio blues", "978-8483835173", 1987, 18.99, 400, 5, 1),
            ("Cien sonetos de amor", "978-9507317729", 1959, 11.99, 120, 13, 3),
            ("Rebelión en la granja", "978-0451526342", 1945, 8.50, 112, 8, 2),
            ("Anna Karénina", "978-8420674222", 1877, 26.75, 864, 17, 1),
            ("El nombre de la rosa", "978-8420460949", 1980, 20.50, 592, 1, 7),
            ("El amor en los tiempos del cólera", "978-0307389732", 1985, 17.99, 348, 1, 8)
        ]
        execute_query_ignore(connection, insert_libros, libros_data)
        
        # INSERTAR RELACIONES LIBRO-AUTOR
        insert_libro_autor = """
        INSERT IGNORE INTO libro_autor (id_libro, id_autor)
        VALUES (%s, %s)
        """
        libro_autor_data = [
            (1, 1),   # Cien Años - García Márquez
            (2, 2),   # Orgullo y Prejuicio - Austen
            (3, 3),   # La ciudad y los perros - Vargas Llosa
            (4, 4),   # La casa de los espíritus - Allende
            (5, 5),   # Rayuela - Cortázar
            (6, 6),   # Ficciones - Borges
            (7, 7),   # El viejo y el mar - Hemingway
            (8, 8),   # 1984 - Orwell
            (9, 9),   # Harry Potter - Rowling
            (10, 10), # It - King
            (11, 11), # Don Quijote - Cervantes
            (12, 12), # Bodas de sangre - Lorca
            (13, 13), # Veinte poemas - Neruda
            (14, 14), # Hamlet - Shakespeare
            (15, 15), # Orient Express - Christie
            (16, 16), # Crimen y castigo - Dostoievski
            (17, 17), # Guerra y paz - Tolstoi
            (18, 18), # La metamorfosis - Kafka
            (19, 19), # Desolación - Mistral
            (20, 20), # La sombra del viento - Ruiz Zafón
            (21, 21), # Capitán Alatriste - Pérez-Reverte
            (22, 22), # Pilares de la Tierra - Follett
            (23, 23), # Código Da Vinci - Brown
            (24, 24), # El alquimista - Coelho
            (25, 25), # Tokio blues - Murakami
            (26, 13), # Cien sonetos - Neruda
            (27, 8),  # Rebelión en la granja - Orwell
            (28, 17), # Anna Karénina - Tolstoi
            (29, 26), # El nombre de la rosa - Eco
            (30, 1)   # El amor en tiempos del cólera - García Márquez
        ]
        execute_query_ignore(connection, insert_libro_autor, libro_autor_data)
        
        print("\n" + "=" * 50)
        print("🎉 ¡Inserción de datos completada!")
        print("=" * 50)
     
        connection.close()
        print("🔌 Conexión cerrada")