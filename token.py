tipo=""
def tokens(dato):
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
    elif "circulo" in dato.lower() or "rectangulo" in dato.lower() or "triangulo" in dato.lower() or "punto" in dato.lower() or "hexagono" in dato.lower() or "diamante" in dato.lower():
        tipo="Tk_Forma"
    elif "'" in dato:
        tipo="Tk_Cadena"
    elif dato.lower()=="nodo":
        tipo="Tk_nodo"
    elif dato.lower()=="nodos":
        tipo="Tk_nodos"
    elif dato.lower()=="defecto":
        tipo="Tk_defecto"
    elif dato.lower()=="verdadero":
        tipo="Tk_listaDobleEnlazada"
    elif dato.lower()=="falso":
        tipo="Tk_listaSimple"
    return tipo   