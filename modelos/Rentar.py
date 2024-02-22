from modelos import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Rentar(db.Model):
    __tablename__ = 'rentar'
    idRentar = db.Column(db.Integer, primary_key=True)
    idUsuario = db.Column(db.Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = db.Column(db.Integer, ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    dias_de_renta = db.Column(db.Integer, default=5)
    estatus = db.Column(db.Boolean, default=False)

    usuario = relationship('Usuario', backref='rentas')
    pelicula = relationship('Pelicula', backref='rentas')


    def __init__(self, idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=False):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus


    def __str__(self):
        return f'ID Renta: {self.idRentar}\nID Usuario: {self.idUsuario}\nID Película: {self.idPelicula}\n' \
            f'Fecha de Renta: {self.fecha_renta}\nDías de Renta: {self.dias_de_renta}\nEstatus: {self.estatus}\n'
    
