from negocio_rules import app
from capa_datos import data
from flask import request, jsonify

#Regla de negocio
def evaluar_cantidad(silla,cantidad):
    s = data.consultar_silla(silla)
    if(s.stock>=cantidad):
        return True
    return False


@app.route("/registrar_venta", methods=['POST', 'GET'])
def registrar_venta():
    cantidad = request.args.get("cantidad")
    silla = request.args.get("silla")
    if(evaluar_cantidad(silla,cantidad)):
        data.registrar_venta(request.args.get("fecha"),cantidad,silla,request.args.get("conferencia"))
        return "Operación realizada con éxito"
    return "No hay suficiente cantidad de sillas en el inventario"

@app.route("/obtener_sillas", methods=['POST', 'GET'])
def obtener_sillas():
    sillas = data.obtener_sillas()
    result_json = []
    for silla in sillas:
        cu = {
            "id": silla.id,
            "tipo": silla.tipo,
            "precio": silla.precio,
        }
        result_json.append(cu)
    return jsonify(sillas=result_json)


@app.route("/obtener_conferencias", methods=['POST', 'GET'])
def obtener_conferencias():
    conferencias = data.obtener_conferencias()
    result_json = []
    for conferencia in conferencias:
        cu = {
            "id": conferencia.id,
            "tipo": conferencia.nombre,
            "precio": conferencia.precio,
        }
        result_json.append(cu)
    return jsonify(conferencias=result_json)


'''
@app.route("/add_conferencia", methods=['POST', 'GET'])
def add_conferencia():
    data.add_conferencia(request.args.get("nombre"),request.args.get("descripcion"),request.args.get("fecha"),
                         request.args.get("precio"))
    return

@app.route("/add_evento", methods=['POST', 'GET'])
def add_evento():
    data.add_evento(request.args.get("nombre"),request.args.get("tipo"))
    return

@app.route("/add_silla", methods=['POST', 'GET'])
def add_silla():
    data.add_silla(request.args.get("tipo"))
    return
'''