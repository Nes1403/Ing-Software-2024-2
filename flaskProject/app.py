from modelos import db
from flask import Flask, render_template
from contollers.PrimerControlador import mi_primer_blueprint
from contollers.ControllerAlumno import alumno_blueprint
from contollers.ControladorUsuario import usuario_blueprint
from contollers.ControladorPelicula import pelicula_blueprint
from contollers.ControladorRentar import renta_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_software'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)
app.register_blueprint(renta_blueprint)
app.register_blueprint(usuario_blueprint, url_prefix='/usuario')
app.register_blueprint(pelicula_blueprint)

@app.route('/')
def hello_world():  # put application's code here
    return render_template('menu.html')

if __name__ == '__main__':
    app.run()
