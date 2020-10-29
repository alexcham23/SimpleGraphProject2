def formG(dato):
    figura=""
    if dato.lower()=="circulo":
        figura="circle"
    elif dato.lower()=="rectangulo":
        figura="box"
    elif dato.lower()=="triangulo":
            figura="triangle"     
    elif dato.lower()=="punto":
            figura="point"  
    elif dato.lower()=="hexagono":
            figura="hexagon" 
    elif dato.lower()=="diamante":
            figura="diamond"     
    return figura