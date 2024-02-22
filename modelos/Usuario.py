from modelos import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    idUsuario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    apPat = db.Column(db.String(200))
    apMat = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(64))
    email = db.Column(db.String(500), nullable=True)
    profilePicture = db.Column(db.LargeBinary)
    superUser = db.Column(db.Boolean, nullable=True)


    def __init__(self, nombre, apPat, apMat=None,
                 password=None, email=None,
                 profile_picture=None, super_user=False):

        self.nombre = nombre
        self.apPat = apPat  
        self.apMat = apMat
        self.password = password
        self.email = email
        self.profilePicture = profile_picture
        self.superUser = super_user

    def __str__(self):
        return(
            f'ID Usuario: {self.idUsuario}\n'
            f'Nombre: {self.nombre}\n'
            f'Apellido Paterno: {self.apPat}\n'
            f'Apellido Materno: {self.apMat}\n'
            f'Contraseña: {self.password}\n'
            f'Email: {self.email}\n'
            f'Super User: {self.superUser}\n'
            )
        




