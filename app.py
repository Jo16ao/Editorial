
"""
Módulo principal para la aplicación interactiva de la base de datos editorial.
Contiene el menú interactivo que se enviara al main para ejecutar el programa.
"""
#Importamos funciones específicas del módulo libro_queries.py en la carpeta queries/
from queries.libro_queries import get_all_libros, get_libro_details_with_join, get_libros_by_titulo, update_libro_precio, delete_libro
from queries.autor_queries import get_all_autores
from queries.editorial_queries import get_all_editoriales 
from mysql.connector import Error
#Menu interactivo y funcional 
def show_menu():
    print("\n--- 📚 Menú Interactivo de la Editorial --- 🌟")
    print("1 - 📖 Ver todos los libros")
    print("2 - 👤 Ver todos los autores")
    print("3 - 🏢 Ver todas las editoriales")
    print("4 - 🔍 Buscar libros por título")
    print("5 - 📘 Ver detalles de un libro (con JOIN)")
    print("6 - 💰 Actualizar precio de un libro")
    print("7 - ❌ Eliminar un libro")
    print("8 - 🚪 Salir")
    print("-----------------------------------------")

def handle_choice(choice):
    if choice == 1:
        print("\n📚 Todos los libros en la base de datos:")
        libros = get_all_libros()
        if libros:
            for libro in libros:
                print(f"- {libro['titulo']} (ID: {libro['id_libro']}, Precio: €{libro['precio']})")
        else:
            print("😕 No hay libros disponibles.")
    
    elif choice == 2:
        print("\n👤 Todos los autores en la base de datos:")
        autores = get_all_autores()
        if autores:
            for autor in autores:
                print(f"- {autor['nombre']} {autor['apellido']} (ID: {autor['id_autor']})")
        else:
            print("😕 No hay autores.")
    
    elif choice == 3:
        print("\n🏢 Todas las editoriales en la base de datos:")
        editoriales = get_all_editoriales()
        if editoriales:
            for editorial in editoriales:
                print(f"- {editorial['nombre']} (ID: {editorial['id_editorial']})")
        else:
            print("😕 No hay editoriales .")
    
    elif choice == 4:
        titulo = input("🔍 Ingresa el título (o parte de él) para buscar: ")
        libros = get_libros_by_titulo(titulo)
        if libros:
            print(f"\n📖 Libros encontrados con '{titulo}':")
            for libro in libros:
                print(f"- {libro['titulo']} (ID: {libro['id_libro']})")
        else:
            print("😕 No se encontraron libros.")
    
    elif choice == 5:
        try:
            id_libro = int(input("📘 Ingresa el ID del libro para ver detalles: "))
            detalles = get_libro_details_with_join(id_libro)
            if detalles:
                detalle = detalles[0]  # Asumiendo que devuelve una lista con un dict
                print("\n🔍 Detalles del libro:")
                print(f"Título: {detalle['titulo']}")
                print(f"ISBN: {detalle['isbn']}")
                print(f"Año: {detalle['año_publicacion']}")
                print(f"Precio: ${detalle['precio']}")
                print(f"Editorial: {detalle['editorial']}")
                print(f"Categoría: {detalle['categoria']}")
                print(f"Autores: {detalle['autores']}")
            else:
                print("😕 Libro no encontrado.")
        except ValueError:
            print("❌ ID inválido. Debe ser un número.")
    
    elif choice == 6:
        try:
            id_libro = int(input("💰 Ingresa el ID del libro a actualizar: "))
            nuevo_precio = float(input("Ingresa el nuevo precio: "))
            update_libro_precio(id_libro, nuevo_precio)
            print("🎉 Precio actualizado exitosamente!")
        except ValueError:
            print("❌ Entrada inválida. Usa números para ID y precio.")
    
    elif choice == 7:
        try:
            id_libro = int(input("❌ Ingresa el ID del libro a eliminar: "))
            delete_libro(id_libro)
            print("🎉 Libro eliminado exitosamente!")
        except ValueError:
            print("❌ ID inválido. Debe ser un número.")
    
    elif choice == 8:
        print("👋 ¡Adiós! Gracias por usar la app de la editorial. 🔥⚡")
        return False  # Salir del bucle
    
    else:
        print("❌ Opción inválida. Por favor, elige un número del 1 al 8. 😕")
    
    return True  # Continuar el bucle

def run_app():
    while True:
        show_menu()
        try:
            choice = int(input("Elige una opción: "))
            if not handle_choice(choice):
                break
        except ValueError:
            print("❌ Solo números, por favor. Intenta de nuevo. 🔢")
        except Error as e:
            print(f"❌ Error en la base de datos: {e}. Verifica tu conexión.")