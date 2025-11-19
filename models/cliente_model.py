from database import db


class Cliente(db.Model):
    __tablename__ = 'clientes'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    #Relacion con ventas
    ventas = db.relationship('Venta', back_populates='cliente')

    # Constructor para inicializar el objeto directamente
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
    # Guardar en la BD
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtener todos los usuarios
    @staticmethod
    def get_all():
        return Cliente.query.all()
    
    # Obtener usuario por ID
    @staticmethod
    def get_by_id(id):
        return Cliente.query.get(id)
    
    # Actualizar datos
    def update(self, nombre=None, email=None, telefono=None):
        if nombre and email and telefono:
            self.nombre = nombre
            self.email = email
            self.telefono = telefono
        db.session.commit()
    
    # Eliminar usuario
    def delete(self):
        db.session.delete(self)
        db.session.commit()
