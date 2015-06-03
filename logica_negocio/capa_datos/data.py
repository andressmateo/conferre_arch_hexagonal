from base import db

def registrar_venta(fecha,cantidad,tipo_silla, conferencia):
    silla = models.Silla.query.filter_by(models.Silla.tipo==tipo_silla)
    conferencia = models.Conferencia.query.filter_by(models.Conferencia.nombre==conferencia)
    venta = models.Venta(fecha, cantidad, silla, conferencia)
    db.session.add(venta)
    db.session.commit()
    return

def obtener_conferencias():
    conferencias = models.Conferencia.query.all()
    return conferencias

def obtener_sillas():
    sillas = models.sillas.query.all()
    return sillas

def consultar_silla(tipo):
    result = models.Silla.query.filter_by(models.Silla.tipo==tipo)
    return result

'''
def add_conferencia(id,nombre, descripcion, fecha, tipo_silla, precio):
    conferencia = models.Conferencia(nombre, descripcion, fecha, tipo_silla, precio)
    db.session.add(conferencia)
    db.session.commit()
    return  

def add_evento(nombre, tipo):
    evento = models.evento(nombre, tipo)
    db.session.add(evento)
    db.session.commit()
    return 

def add_silla(tipo):
    silla = models.silla(tipo)
    db.session.add(silla)
    db.session.commit()
    return 

def edit_conferencia(id, nombre, descripcion, fecha, tipo_silla, precio):
    models.Conferencia.query.filter_by(id=id).update({models.Conferencia.nombre: nombre,
    models.Conferencia.descripcion: descripcion, models.Conferencia.fecha: fecha,
    models.Conferencia.tipo_silla: tipo_silla, models.Conferencia.precio: precio}, synchronize_session=False)
    db.session.commit()
    return 

'''