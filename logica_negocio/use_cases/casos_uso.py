from negocio_rules import rules
from datos import interfase

#Casos de uso de la aplicación

def registrar_venta(silla, cantidad, conferencia, fecha):
    if(rules.evaluar_cantidad(silla,cantidad)):
        data.registrar_venta(fecha ,cantidad,silla,conferencia)
        return "Operación realizada con éxito"
    return "No hay suficiente cantidad de sillas en el inventario"

def obtener_sillas ():
    sillas = data.obtener_sillas()
    result_json = []
    for silla in sillas:
        cu = {
            "id": silla.id,
            "tipo": silla.tipo,
            "precio": silla.precio,
        }
        result_json.append(cu)
    return result_json

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
    return result_json


