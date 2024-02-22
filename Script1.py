import pymysql
from faker import Faker
from datetime import datetime
import secrets
import string
from datetime import datetime, timedelta

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return contrasena


fake = Faker()

def conectar():
    conexion = pymysql.connect(host='localhost',
                               user='lab',
                               password='Developer123!',
                               database='lab_ing_software')
    return conexion


def insertar():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            sql_usuario = "INSERT INTO usuarios (nombre, apPat, apMat, password, email, superUser) VALUES (%s, %s, %s, %s, %s, %s)"
            contrasena_usuario = generar_contrasena()
            values_usuario = (fake.first_name(), fake.last_name(), fake.last_name(), contrasena_usuario, fake.email(), None)
            cursor.execute(sql_usuario, values_usuario)

            generos_validos = ['Acción', 'Comedia', 'Drama', 'Ciencia Ficción', 'Aventura', 'Romance', 'Thriller', 'Animación', 'Fantasía']
            genero_pelicula = fake.random_element(elements=generos_validos)
            sql_pelicula = "INSERT INTO peliculas (nombre, genero, duracion, inventario) VALUES (%s, %s, %s, %s)"
            values_pelicula = (fake.word(), genero_pelicula, fake.random_int(min=60, max=180), fake.random_int(min=1, max=10))
            cursor.execute(sql_pelicula, values_pelicula)

            cursor.execute("SELECT idUsuario FROM usuarios ORDER BY RAND() LIMIT 1")
            id_usuario = cursor.fetchone()[0]

            cursor.execute("SELECT idPelicula FROM peliculas ORDER BY RAND() LIMIT 1")
            id_pelicula = cursor.fetchone()[0]

            fecha_renta = datetime.now()
            sql_renta = "INSERT INTO rentar (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES (%s, %s, %s, %s, %s)"
            values_renta = (id_usuario, id_pelicula, fecha_renta, fake.random_int(min=1, max=10), 0)
            cursor.execute(sql_renta, values_renta)
        
            conexion.commit()

    except pymysql.IntegrityError as integrity_error:
        print(f"Error de integridad: {integrity_error}")
        conexion.rollback()
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        conexion.rollback()

    finally:
        conexion.close()



def filtra_apellidos():
    cadena_filtro = input("Ingrese la cadena para filtrar por apellidos: ")
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE apPat LIKE %s", (f'%{cadena_filtro}',))
            resultados_paterno = cursor.fetchall()

            cursor.execute("SELECT * FROM usuarios WHERE apMat LIKE %s", (f'%{cadena_filtro}',))
            resultados_materno = cursor.fetchall()

            if resultados_paterno or resultados_materno:
                print("Usuarios cuyo apellido paterno termina con la cadena:")
                for usuario_paterno in resultados_paterno:
                    print(usuario_paterno)

                print("\nUsuarios cuyo apellido materno termina con la cadena:")
                for usuario_materno in resultados_materno:
                    print(usuario_materno)
            else:
                print(f"No se encontraron usuarios cuyo apellido paterno o materno termine con '{cadena_filtro}'.")

    except Exception as e:
        print(f"Error al filtrar usuarios por apellido: {e}")

    finally:
        conexion.close()



def cambiar_genero_pelicula():
    nombre_pelicula = input("Ingrese el nombre de la película: ")
    nuevo_genero = input("Ingrese el nuevo género: ")
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("SELECT idPelicula FROM peliculas WHERE nombre = %s", (nombre_pelicula,))
            resultado = cursor.fetchone()
            if resultado:
                id_pelicula = resultado[0]
                cursor.execute("UPDATE peliculas SET genero = %s WHERE idPelicula = %s", (nuevo_genero, id_pelicula))
                conexion.commit()
                print(f"Se ha cambiado el género de la película '{nombre_pelicula}' a '{nuevo_genero}'.")
            else:
                print(f"No se encontró la película '{nombre_pelicula}' en la base de datos.")

    except Exception as e:
        print(f"Error al cambiar el género de la película: {e}")
    finally:
        conexion.close()



def eliminar_rentas_antiguas():
    conexion = conectar()
    try:
        with conexion.cursor() as cursor:
            fecha_limite = datetime.now() - timedelta(days=3)
            cursor.execute("DELETE FROM rentar WHERE fecha_renta <= %s", (fecha_limite,))
            conexion.commit()
            print(f"Se han eliminado las rentas anteriores al {fecha_limite.strftime('%Y-%m-%d')}.")

    except Exception as e:
        print(f"Error al eliminar rentas antiguas: {e}")

    finally:
        conexion.close()


insertar()
