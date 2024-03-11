from flask import Blueprint, render_template, flash, redirect, url_for, request
from modelos import db
from modelos.Usuario import Usuario
from modelos.Rentar import Rentar
from modelos.Pelicula import Pelicula

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/', methods =['GET', 'POST'])
def menu_usuarios():
    return render_template('usuario/menu_usuarios.html')


@usuario_blueprint.route('/ver', methods=['GET'])
def ver_usuarios():
    usuarios = Usuario.query.all()
    return render_template('usuario/ver_usuarios.html', usuarios=usuarios)

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        ap_pat = request.form['ap_pat']
        ap_mat = request.form['ap_mat']
        password = request.form['password']
        email = request.form['email']

        nuevo_usuario = Usuario(nombre=nombre, apPat=ap_pat, apMat=ap_mat, password=password, email=email)
        
        try:
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario agregado correctamente', 'success')
            return redirect(url_for('usuario.ver_usuarios'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al agregar usuario: {str(e)}', 'danger')

    return render_template('usuario/agregar_usuario.html')



@usuario_blueprint.route('/pedir_id/<string:accion>', methods=['GET', 'POST'])
def pedir_id(accion):
    if request.method == 'POST':
        id_usuario = request.form.get('id_usuario')

        usuario = Usuario.query.get(id_usuario)

        if usuario:
            if accion == 'editar':
                return redirect(url_for('usuario.editar_usuario', id_usuario=id_usuario))
            elif accion == 'eliminar':
                return redirect(url_for('usuario.eliminar_usuario', id_usuario=id_usuario))
        else:
            flash(f'No se encontró un usuario con el ID {id_usuario}', 'danger')

    return render_template('usuario/pedir_id.html', accion=accion)

@usuario_blueprint.route('/editar/<int:id_usuario>', methods=['GET', 'POST'])
def editar_usuario(id_usuario):

    usuario = Usuario.query.get_or_404(id_usuario)

    if request.method == 'POST':
        usuario.nombre = request.form['nombre']
        usuario.apPat = request.form['ap_pat']
        usuario.apMat = request.form['ap_mat']
        usuario.password = request.form['password']
        usuario.email = request.form['email']

        try:
            db.session.commit()
            flash('Usuario editado correctamente', 'success')
            return redirect(url_for('usuario.ver_usuarios'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al editar usuario: {str(e)}, verifique el id del usuario', 'danger')

    return render_template('usuario/editar_usuario.html', id_usuario=id_usuario)

@usuario_blueprint.route('/eliminar/<int:id_usuario>', methods=['POST', 'GET'])
def eliminar_usuario(id_usuario):
    usuario = Usuario.query.get_or_404(id_usuario)

    rentas_asociadas = Rentar.query.filter_by(idUsuario=id_usuario).all()
    for renta in rentas_asociadas:
        db.session.delete(renta)

    try:
        db.session.delete(usuario)
        db.session.commit()
        flash('Usuario eliminado correctamente', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error al eliminar usuario: {str(e)}, verifique el id del usuario', 'danger')

    return redirect(url_for('usuario.ver_usuarios'))
