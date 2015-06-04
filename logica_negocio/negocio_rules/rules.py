from datos import interfase

def evaluar_cantidad(silla,cantidad):
    s = data.consultar_silla(silla)
    if(s.stock>=cantidad):
        return True
    return False