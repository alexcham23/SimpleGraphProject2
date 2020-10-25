tipo=""
def token(dato):
    global tipo
    if dato.lower()=="lista":
        tipo="Tk_lista"
    elif dato.isdigit():
        tipo="Tk_Numero"
    elif "," in dato:
        tipo="Tk_coma"
    elif "(" in dato:
        tipo="Tk_Apertura_Parentesis"
    elif ")" in dato:
        tipo="Tk_Cierre_Parentesis" 
    elif "{" in dato:
        tipo="Tk_Apertura_Llave"
    elif "}" in dato:
        tipo="Tk_Cierre_Llave" 
    elif ";" in dato:
        tipo="Tk_Punto&coma"
    elif tipo.lower()=="circulo" or tipo.lower()=="rectangulo" or tipo.lower()=="triangulo" or tipo.lower()=="punto" or tipo.lower()=="hexagono" or tipo.lower()=="diamante":
        tipo="Tk_Forma"
    elif "'" in dato:
        tipo="Tk_Cadena"
    elif dato.lower()=="nodo":
        tipo="Tk_nodo"
    elif dato.lower()=="nodos":
        tipo="Tk_nodos"
    elif dato.lower()=="defecto":
        tipo="Tk_defecto"
    return tipo   