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
def listavalue(lexema,fila,columna,token):
    global listavalue
    lista2=[str(lexema),str(fila),str(columna),str(token)] 
    evalue.append(lista2) 