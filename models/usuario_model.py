from database import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    # Constructor para inicializar el objeto directamente
    def __init__(self, nombre, username, password, rol):
        self.nombre = nombre
        self.username = username
        self.password = self.hash_password(password)  # encripta al crear
        self.rol = rol

    # Verificar contraseña
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password)
    
    def verify_password(self, password):
        return check_password_hash(self.password, password)
    # Guardar en la BD
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtener todos los usuarios
    @staticmethod
    def get_all():
        return Usuario.query.all()
    
    # Obtener usuario por ID
    @staticmethod
    def get_by_id(id):
        return Usuario.query.get(id)
    
    # Actualizar datos
    def update(self, nombre=None, username=None, password=None, rol=None):
        if nombre:
            self.nombre = nombre
        if username:
            self.username = username
        if password:
            self.password = generate_password_hash(password)
        if rol:
            self.rol = rol
        db.session.commit()
    
    # Eliminar usuario
    def delete(self):
        db.session.delete(self)
        db.session.commit()
