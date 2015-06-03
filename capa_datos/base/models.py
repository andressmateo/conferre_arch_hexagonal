from base import db

class Conferencia(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    nombre = db.Column(db.String(200), unique=True)
    descripcion = db.Column(db.Text)
    fecha = db.Column(db.Text)
    precio = db.Column(db.Integer)
    sillas = db.relationship('Silla', backref=db.backref('conferecias', lazy='dynamic'))

    def __init__(self, nombre, descripcion, fecha, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.fecha = fecha
        self.precio = precio


class  Venta (db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    fecha = db.Column(db.Text)
    cantidad = db.Column(db.Integer)
    silla = db.relationship('Silla', backref=db.backref('ventas', lazy='dynamic'))
    conferencia = db.relationship('Conferencia', backref=db.backref('ventas', lazy='dynamic'))

    def __init__(self, fecha, cantidad, silla, conferencia):
        self.fecha = fecha
        self.cantidad = cantidad
        self.silla = silla
        self.conferencia = conferencia

class Silla (db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    tipo = db.Column(db.Text)
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)

    def __init__(self, tipo, precio):
        self.tipo = tipo
        self.precio = precio


