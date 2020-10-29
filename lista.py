from Graficar import Grafico
error=[]
evalue=[]
listaestados=[]
name=""
namedefect=""
Colordefect=""
figuradefect=""
tipolist=""
ruta=""
graph1=""
graph2=""
def limpiarlistas():
    global evalue, ruta, error
    evalue.clear()
    error.clear()
    ruta=""
def llamar():
    global name,namedefect,Colordefect, tipolist,figuradefect
    from analizadolista import nombre,nombredefect,colordefect,tipofigura,tipolista
    name=nombre
    namedefect=nombredefect
    Colordefect=colordefect
    figuradefect=tipofigura
    tipolist= tipolista
    
    for dato in range(len(listaestados)):
        if listaestados[dato][0]=="#" and listaestados[dato][1]=="#":
            listaestados[dato][0]=namedefect
            listaestados[dato][1]=Colordefect
        elif listaestados[dato][0]!="#" and listaestados[dato][1]=="#":
            listaestados[dato][1]=Colordefect
        elif listaestados[dato][0]=="#" and listaestados[dato][1]!="#":
            listaestados[dato][0]=namedefect
            
def listaerror(fila,columna,caracter,descripcion):
    global listaerror
    lista=[str(fila),str(columna),str(caracter),str(descripcion)]
    error.append(lista)
def listavalue(fila,columna,lexema,token):
    global listavalue
    lista2=[str(fila),str(columna),str(lexema),str(token)] 
    evalue.append(lista2) 
def estados(encabezado,color):
    global listaestados    
    listaestados.append([encabezado,color])
    
# desde aque crearemos lo metodos que me permitan crear el archivo que me servira para graficar
def graficarlist():
    from colorstart import colorfill
    from figurasG import formG
    global name,namedefect,Colordefect,figuradefect,tipolist
    graph1='digraph finite_state_machine {\n\trankdir=LR;\n\tsize=\"8,5\"\n\tlabel="\n'+str(name)+'";\n\tlabelloc="c";\n\tlabelfontsize=200;'
    auxiliar=""
    graph3=""
    graph2=""	
    #datos de estados 
    for dato in range(len(listaestados)):
      graph2+="\n\t"+str(listaestados[dato][0])+" [shape="+formG(figuradefect)+",fillcolor=\""+str(colorfill(listaestados[dato][1]))+"\",style=filled,label=\""+str(listaestados[dato][0])+"\"];"
            
    if tipolist.lower()=="verdadero":
        for dato in range(len(listaestados)):
            if dato==0:
                auxiliar=listaestados[dato][0]
            else:
                graph3+="\n\t"+auxiliar+"->"+listaestados[dato][0]
                auxiliar=listaestados[dato][0]
    
        for item in reversed(range(len(listaestados))):
            if item==len(listaestados)-1:
               auxiliar=listaestados[item][0] 
            else:
                graph3+="\n\t"+auxiliar+"->"+listaestados[item][0]
                auxiliar=listaestados[item][0]
    elif tipolist.lower()=="falso":
        for dato in range(len(listaestados)):
            if dato==0:
                auxiliar=listaestados[dato][0]
            else:
                graph3+="\n\t"+auxiliar+"->"+listaestados[dato][0]
                auxiliar=listaestados[dato][0]
    
    unir=graph1+graph2+graph3+"\n}"
    Grafico(unir,"lista")