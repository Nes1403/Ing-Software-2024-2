from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from flask import Flask
from sqlalchemy import and_, or_
from modelos import db
from modelos.Usuario import Usuario
from modelos.Pelicula import Pelicula
from modelos.Rentar import Rentar
from datetime import datetime


#mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
#<dialecto>+<driver>://<usuario>:<passwd>@localhost:3306/<db>
#mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)


def menu():
    print("Menú:")
    print("1. Ver registros de una tabla")
    print("2. Filtrar registros por ID")
    print("3. Actualizar nopmbre de usuarios o peliculas, o actualizar fecha de renta")
    print("4. Eliminar registro(s)")


def ver_registros(tabla):
    registros = tabla.query.all()
    for registro in registros:
        print(registro)


def filtrar_por_id(tabla, id):
    try:
        if tabla == Usuario:
            registro = tabla.query.filter_by(idUsuario=id).first()
        elif tabla == Pelicula:
            registro = tabla.query.filter_by(idPelicula=id).first()
        elif tabla == Rentar:
            registro = tabla.query.filter_by(idRentar=id).first()
        else:
            print("Tabla no válida.")
            return
        if registro:
            print(registro)
        else:
            print(f"No hay registros con el ID: {id}")
    except Exception as e:
        print(f"Error al filtrar por ID: {e}")



def actualizar_fecha_renta(id_renta, nueva_fecha):
    try:
        nueva_fecha_date = datetime.strptime(nueva_fecha, "%Y-%m-%d").date()
    except ValueError:
        print("Error: Formato de fecha incorrecto. Utiliza el formato YYYY-MM-DD.")
        return

    renta = Rentar.query.get(id_renta)
    if renta:
        renta.fecha_renta = nueva_fecha_date
        db.session.commit()
        print(f"Fecha de renta actualizada para la renta con ID {id_renta}.")
    else:
        print(f"No se encontró una renta con ID {id_renta}.")

def actualizar_nombre(tabla, id_registro, nombre):
    registro = db.session.query(tabla).get(id_registro)
    if registro:
        registro.nombre = nombre
        db.session.commit()
        print(f"Nombre actualizado para el registro con ID {id_registro}.")
    else:
        print(f"No se encontró un registro con ID {id_registro}.")






def eliminar_registro(tabla, id):
    try:
        if id:
            if tabla == Usuario:
                Rentar.query.filter_by(idUsuario=id).delete()
            elif tabla == Pelicula:
                Rentar.query.filter_by(idPelicula=id).delete()
            registro = tabla.query.get(id)
            
            if registro:
                db.session.delete(registro)
                db.session.commit()
                print(f"Registro con ID {id} eliminado.")
            else:
                print(f"No hay registros con el ID: {id}")
        else:
            confirmacion = input("¿Está seguro de que desea eliminar todos los registros? (s/n): ")
            if confirmacion.lower() == 's':
                Rentar.query.delete()
                tabla.query.delete()
                db.session.commit()
                print("Todos los registros eliminados.")
            else:
                print("Operación de eliminación cancelada.")
    except Exception as e:
        print(f"Error al eliminar registro: {e}")


if __name__ == '__main__':
    with app.app_context():
        while True:
            menu()
            opcion = input("Ingrese el número de la opción deseada (0 para salir): ")

            if opcion == '0':
                break

            if opcion == '1':
                tabla = input("Ingrese el nombre de la tabla (usuarios, peliculas, rentas): ")
                if tabla == 'usuarios':
                    ver_registros(Usuario)
                elif tabla == 'peliculas':
                    ver_registros(Pelicula)
                elif tabla == 'rentas':
                    ver_registros(Rentar)
                else:
                    print("Tabla no válida.")

            elif opcion == '2':
                tabla = input("Ingrese el nombre de la tabla (usuarios, peliculas, rentas): ")
                try:
                    if tabla == 'usuarios':
                        id = int(input("Ingrese el ID a filtrar: "))
                        filtrar_por_id(Usuario, id)
                    elif tabla == 'peliculas':
                        id = int(input("Ingrese el ID a filtrar: "))
                        filtrar_por_id(Pelicula, id)
                    elif tabla == 'rentas':
                        id = int(input("Ingrese el ID a filtrar: "))
                        filtrar_por_id(Rentar, id)
                    else:
                        print("Tabla no válida.")
                except ValueError:
                    print("Error: Por favor, ingrese un número entero válido.")
                    
            elif opcion == '3':
                tabla = input("Ingrese el nombre de la tabla (usuarios, peliculas, rentas): ")
                try:
                    if tabla == 'usuarios':
                        id_registro = int(input("Ingrese el ID del usuario a actualizar: "))
                        nombre = input("Ingrese el nuevo nombre del usuario: ")
                        actualizar_nombre(Usuario, id_registro, nombre)
                    elif tabla == 'peliculas':
                        id_registro = int(input("Ingrese el ID de la pelicula a actualizar: "))
                        nombre = input("Ingrese el nuevo nombre de la pelicula: ")
                        actualizar_nombre(Pelicula, id_registro, nombre)
                    elif tabla == 'rentas':
                        id_renta = int(input("Ingrese el ID de la renta a actualizar: "))
                        nueva_fecha = input("Ingrese la nueva fecha de renta (YYYY-MM-DD): ")
                        actualizar_fecha_renta(id_renta, nueva_fecha)
                    else:
                        print("Tabla no válida.")
                except ValueError:
                    print("Error: Por favor, ingrese un número entero válido.")
                

            elif opcion == '4':
                try:
                    tabla = input("Ingrese el nombre de la tabla (usuarios, peliculas, rentas): ")
                    id = input("Ingrese el ID a eliminar (deje en blanco para eliminar todos los registros): ")
                    if id == '':
                        id_borrar = None
                    else:
                        id_borrar = int(id)
                    if tabla == 'usuarios':
                        eliminar_registro(Usuario, id_borrar)
                    elif tabla == 'peliculas':
                        eliminar_registro(Pelicula, id_borrar)
                    elif tabla == 'rentas':
                        eliminar_registro(Rentar, id_borrar)
                except ValueError:
                    print("Error: Por favor, ingrese un número entero válido.")

            else:
                print("Opción no válida.")

