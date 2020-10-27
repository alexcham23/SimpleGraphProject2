error=[]
evalue=[]
ruta=""
def limpiarlistas():
    global evalue, ruta, error
    evalue.clear()
    error.clear()
    ruta=""
def listaerror(fila,columna,caracter,descripcion):
    global listaerror
    lista=[str(fila),str(columna),str(caracter),str(descripcion)]
    error.append(lista)
def listavalue(fila,columna,lexema,token):
    global listavalue
    lista2=[str(fila),str(columna),str(lexema),str(token)] 
    evalue.append(lista2) 