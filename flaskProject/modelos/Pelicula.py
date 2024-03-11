from modelos import db

class Pelicula(db.Model):
    __tablename__ = 'peliculas'
    idPelicula = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200), nullable=False)
    genero = db.Column(db.String(45), nullable=True)
    duracion = db.Column(db.Integer, nullable=True)
    inventario = db.Column(db.Integer, nullable=False, default=1)

    def __init__(self, nombre, genero=None, duracion=None, inventario=1):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f'ID Película: {self.idPelicula}\nNombre: {self.nombre}\nGénero: {self.genero}\nDuración: {self.duracion}\n' \
               f'Inventario: {self.inventario}\n'
