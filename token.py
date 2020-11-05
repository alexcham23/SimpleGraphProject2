tipo=""
def tokens(dato):
    global tipo
    if dato.lower()=="lista":
        tipo="Tk_lista"
    elif dato.lower()=="matriz":
        tipo="Tk_matriz"
    elif dato.lower()=="fila":
        tipo="Tk_fila"   
    elif dato.lower()=="#":
        tipo="Tk_Numeral" 
    elif dato.lower()=="encabezados":
        tipo="Tk_encabezado"     
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
    elif dato.lower()=="azul" or dato.lower()=="azul2" or dato.lower()=="azul3":
        tipo="Tk_color"
    elif dato.lower()=="rojo" or dato.lower()=="rojo2" or dato.lower()=="rojo3": 
        tipo="Tk_color"
    elif dato.lower()=="amarillo" or dato.lower()=="amarillo2" or dato.lower()=="amarillo3":
        tipo="Tk_color"
    elif dato.lower()=="anaranjado" or dato.lower()=="anaranjado2" or dato.lower()=="anaranjado3":
        tipo="Tk_color"
    elif dato.lower()=="cafe" or dato.lower()=="cafe2" or dato.lower()=="cafe3":
        tipo="Tk_color"
    elif dato.lower()=="gris" or dato.lower()=="gris2" or dato.lower()=="gris3":
        tipo="Tk_color"
    elif dato.lower()=="morado" or dato.lower()=="morado2" or dato.lower()=="morado3":
        tipo="Tk_color"
    elif dato.lower()=="gris" or dato.lower()=="gris2" or dato.lower()=="gris3":
        tipo="Tk_color"
    elif dato.lower()=="verde" or dato.lower()=="verde2" or dato.lower()=="verde3" or dato.lower()=="blanco":
        tipo="Tk_color"        
    else:
        tipo="Desconocido"  
    return tipo   