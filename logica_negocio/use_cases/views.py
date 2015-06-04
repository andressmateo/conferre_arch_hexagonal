from negocio_rules import app
from use_cases import casos_uso
from flask import request, jsonify

#Cada uno de los puertos que se conectan con las interfaces de cada capa.

@app.route("/registrar_venta", methods=['POST', 'GET'])
def registrar_venta():
    cantidad = request.args.get("cantidad")
    silla = request.args.get("silla")
    conferencia = request.args.get("conferencia")
    fecha = request.args.get("fecha")
    return casos_uso.registrar_venta(silla,cantidad,conferencia,fecha)

@app.route("/obtener_sillas", methods=['POST', 'GET'])
def obtener_sillas():
    return jsonify(sillas=casos_uso.obtener_sillas())

@app.route("/obtener_conferencias", methods=['POST', 'GET'])
def obtener_conferencias():
    return jsonify(conferencias=casos_uso.obtener_conferencias())