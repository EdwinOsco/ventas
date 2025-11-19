from database import db


class Producto(db.Model):
    __tablename__ = 'productos'
    
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(120), nullable=False)
    precio = db.Column(db.Float(11,2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    #Especificamos la relacion con ventas
    ventas = db.relationship('Venta', back_populates='producto')

    # Constructor para inicializar el objeto directamente
    def __init__(self, descripcion, precio, stock):
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
    # Guardar en la BD
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtener todos los usuarios
    @staticmethod
    def get_all():
        return Producto.query.all()
    
    # Obtener usuario por ID
    @staticmethod
    def get_by_id(id):
        return Producto.query.get(id)
    
    # Actualizar datos
    def update(self, descripcion=None, precio=None, stock=None):
        if descripcion and precio and stock:
            self.descripcion = descripcion
            self.precio = precio
            self.stock = stock
        db.session.commit()
    
    # Eliminar usuario
    def delete(self):
        db.session.delete(self)
        db.session.commit()
