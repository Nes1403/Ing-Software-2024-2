from flask import Blueprint, render_template, flash, redirect, url_for, request
from modelos import db
from modelos.Usuario import Usuario
from modelos.Rentar import Rentar
from modelos.Pelicula import Pelicula
from datetime import datetime

renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/', methods =['GET', 'POST'])
def menu_rentas():
    return render_template('renta/menu_rentas.html')


@renta_blueprint.route('/ver', methods=['GET'])
def ver_rentas():
    rentas = Rentar.query.all()
    return render_template('renta/ver_rentas.html', rentas=rentas)

@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_renta():
    if request.method == 'POST':
        idUsuario = request.form['idUsuario']
        idPelicula = request.form['idPelicula']
        fecha = request.form['fecha']
        diasRenta = request.form['diasRenta']

        fecha_actual = datetime.now().strftime('%Y-%m-%d')
        if fecha > fecha_actual:
            flash('La fecha de renta no puede ser futura', 'danger')
            return render_template('renta/agregar_renta.html')
        
        usuario_existente = Usuario.query.get(idUsuario)
        if usuario_existente is None:
            flash('El ID de usuario proporcionado no existe', 'danger')
            return render_template('renta/agregar_renta.html')


        pelicula_existente = Pelicula.query.get(idPelicula)
        if pelicula_existente is None:
            flash('El ID de película proporcionado no existe', 'danger')
            return render_template('renta/agregar_renta.html')
        
        
        nueva_renta = Rentar(idUsuario = idUsuario, idPelicula=idPelicula, fecha_renta=fecha, dias_de_renta= diasRenta, estatus=False)


        try:
            db.session.add(nueva_renta)
            db.session.commit()
            flash('Renta agregado correctamente', 'success')
            return redirect(url_for('renta.ver_rentas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al agregar Renta: {str(e)}', 'danger')

    return render_template('renta/agregar_renta.html')



@renta_blueprint.route('/pedir_id/<string:accion>', methods=['GET', 'POST'])
def pedir_id(accion):
    if request.method == 'POST':
        id_renta = request.form.get('id_renta')

        renta = Rentar.query.get(id_renta)

        if renta:
            if accion == 'editar':
                return redirect(url_for('renta.editar_renta', id_renta=id_renta))
            elif accion == 'eliminar':
                return redirect(url_for('renta.eliminar_renta', id_renta=id_renta))
        else:
            flash(f'No se encontró una renta con el ID {id_renta}', 'danger')

    return render_template('renta/pedir_id.html', accion=accion)

@renta_blueprint.route('/editar/<int:id_renta>', methods=['GET', 'POST'])
def editar_renta(id_renta):

    renta = Rentar.query.get_or_404(id_renta)

    if request.method == 'POST':
        renta.estatus = request.form['estatus'] == 'True'

        try:
            db.session.commit()
            flash('Renta editada correctamente', 'success')
            return redirect(url_for('renta.ver_rentas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al editar Renta: {str(e)}, verifique el id de la renta', 'danger')

    return render_template('renta/editar_renta.html', id_renta=id_renta)

@renta_blueprint.route('/eliminar/<int:id_renta>', methods=['POST', 'GET'])
def eliminar_renta(id_renta):
    renta = Rentar.query.get_or_404(id_renta)
    try:
        db.session.delete(renta)
        db.session.commit()
        flash('Renta eliminado correctamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar Renta: {str(e)}, verifique el id de la pelicula', 'danger')

    return redirect(url_for('renta.ver_rentas'))
