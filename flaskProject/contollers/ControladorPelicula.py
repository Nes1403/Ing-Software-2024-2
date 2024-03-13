from flask import Blueprint, render_template, flash, redirect, url_for, request
from modelos import db
from modelos.Usuario import Usuario
from modelos.Rentar import Rentar
from modelos.Pelicula import Pelicula

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/', methods =['GET', 'POST'])
def menu_peliculas():
    return render_template('pelicula/menu_peliculas.html')


@pelicula_blueprint.route('/ver', methods=['GET'])
def ver_peliculas():
    peliculas = Pelicula.query.all()
    return render_template('pelicula/ver_peliculas.html', peliculas=peliculas)

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_pelicula():
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form.get('duracion')
        inventario = request.form['inventario']

        duracion = int(duracion) if duracion else None

        
        nueva_pelicula = Pelicula(nombre=nombre, genero=genero, duracion = duracion, inventario=inventario)
        
        try:
            db.session.add(nueva_pelicula)
            db.session.commit()
            flash('Pelicula agregado correctamente', 'success')
            return redirect(url_for('pelicula.ver_peliculas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al agregar Pelicula: {str(e)}', 'danger')

    return render_template('pelicula/agregar_pelicula.html')



@pelicula_blueprint.route('/pedir_id/<string:accion>', methods=['GET', 'POST'])
def pedir_id(accion):
    if request.method == 'POST':
        id_pelicula = request.form.get('id_pelicula')

        pelicula = Pelicula.query.get(id_pelicula)

        if pelicula:
            if accion == 'editar':
                return redirect(url_for('pelicula.editar_pelicula', id_pelicula=id_pelicula))
            elif accion == 'eliminar':
                return redirect(url_for('pelicula.eliminar_pelicula', id_pelicula=id_pelicula))
        else:
            flash(f'No se encontró una pelicula con el ID {id_pelicula}', 'danger')

    return render_template('pelicula/pedir_id.html', accion=accion)

@pelicula_blueprint.route('/editar/<int:id_pelicula>', methods=['GET', 'POST'])
def editar_pelicula(id_pelicula):

    pelicula = Pelicula.query.get_or_404(id_pelicula)

    if request.method == 'POST':
        pelicula.nombre = request.form['nombre']
        pelicula.genero = request.form['genero']

        pelicula.inventario = request.form['inventario']

        duracion = request.form.get('duracion')

        pelicula.duracion = int(duracion) if duracion else None

        try:
            db.session.commit()
            flash('Pelicula editada correctamente', 'success')
            return redirect(url_for('pelicula.ver_peliculas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al editar pelicula: {str(e)}, verifique el id de la pelicula', 'danger')

    return render_template('pelicula/editar_pelicula.html', id_pelicula=id_pelicula)

@pelicula_blueprint.route('/eliminar/<int:id_pelicula>', methods=['POST', 'GET'])
def eliminar_pelicula(id_pelicula):
    pelicula = Pelicula.query.get_or_404(id_pelicula)

    rentas_asociadas = Rentar.query.filter_by(idPelicula=id_pelicula).all()
    for renta in rentas_asociadas:
        db.session.delete(renta)

    try:
        db.session.delete(pelicula)
        db.session.commit()
        flash('Pelicula eliminado correctamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar Pelicula: {str(e)}, verifique el id de la pelicula', 'danger')

    return redirect(url_for('pelicula.ver_peliculas'))
