from Graficar import Grafico
error=[]
evalue=[]
listaestados=[]
tipo=0
name=""
namedefect=""
Colordefect=""
figuradefect=""
tipolist=""
ruta=""
#graph1=""
#graph2=""
def limpiarlistas():
    global evalue, ruta, error, listaestados, Colordefect,name,namedefect,figuradefect,tipolist
    evalue.clear()
    error.clear()
    listaestados.clear()
    ruta=""
    Colordefect=""
    name=""
    namedefect=""
    figuradefect=""
    tipolist=""
def llamar():
    global name,namedefect,Colordefect, tipolist,figuradefect,tipo
    from analizadolista import nombre,nombredefect,colordefect,tipofigura,tipolista
    name=nombre
    namedefect=nombredefect
    Colordefect=colordefect
    figuradefect=tipofigura
    tipolist= tipolista
    tipo=1
    for dato in range(len(listaestados)):
        if listaestados[dato][0]=="#" and listaestados[dato][1]=="#":
            listaestados[dato][0]=namedefect
            listaestados[dato][1]=Colordefect
        elif listaestados[dato][0]!="#" and listaestados[dato][1]=="#":
            listaestados[dato][1]=Colordefect
        elif listaestados[dato][0]=="#" and listaestados[dato][1]!="#":
            listaestados[dato][0]=namedefect
def llamar2():
    global name,namedefect,Colordefect, tipolist,figuradefect,tipo
    from analizadormatriz import nombre,nombredefect,colordefect,tipofigura,tipolista
    name=nombre
    namedefect=nombredefect
    Colordefect=colordefect
    figuradefect=tipofigura
    tipolist= tipolista  
    tipo=2  
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
def graficarmatriz():
    from colorstart import colorfill
    from figurasG import formG
    from analizadormatriz import matriz
    global name,namedefect,Colordefect,figuradefect,tipolist
    graph1='digraph finite_state_machine {\n\tsize=\"8,5\"\n\tlabel="'+str(name)+'";\n\tlabelloc="c";\n\tlabelfontsize=200;'
    auxiliar=""
    aux2=""
    graph3=""
    graph2=""    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]=="#":
                graph2+="\n\t"+str(i)+str(j)+" [shape="+formG(figuradefect)+",fillcolor=\""+str(colorfill(Colordefect))+"\",style=filled,label=\""+str(namedefect)+"\",group="+str(j)+"];" 
            else:
                bandera=False
                x=0
                while x < len(listaestados) and bandera==False :
                    if matriz[i][j] == listaestados[x][0]:
                        if listaestados[x][0]=="$":
                            graph2+="\n\t"+str(i)+str(j)+" [shape="+formG(figuradefect)+",fillcolor=\""+str(colorfill(listaestados[x][1]))+"\",style=filled,label=\""+str(namedefect)+"\",group="+str(j)+"];"
                        elif listaestados[x][1]=="#":
                            graph2+="\n\t"+str(i)+str(j)+" [shape="+formG(figuradefect)+",fillcolor=\""+str(colorfill(Colordefect))+"\",style=filled,label=\""+str(listaestados[x][0])+"\",group="+str(j)+"];"
                        elif listaestados[x][0]=="$" and listaestados[x][1]=="#":
                            graph2+="\n\t"+str(i)+str(j)+" [shape="+formG(figuradefect)+",fillcolor=\""+str(colorfill(Colordefect))+"\",style=filled,label=\""+str(namedefect)+"\",group="+str(j)+"];"                       
                        else:
                            graph2+="\n\t"+str(i)+str(j)+" [shape="+formG(figuradefect)+",fillcolor=\""+str(colorfill(listaestados[x][1]))+"\",style=filled,label=\""+str(listaestados[x][0])+"\",group="+str(j)+"];"
                        bandera=True
                    x+=1
    if tipolist.lower()=="verdadero":
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if j==0:
                    auxiliar=str(i)+str(j)
                    aux2+="\n\t{ rank =same;"+str(i)+str(j)+";"
                else:
                    graph3+="\n\t"+auxiliar+" -> "+str(i)+str(j)
                    graph3+="\n\t"+str(i)+str(j)+" -> "+auxiliar
                    auxiliar=str(i)+str(j)
                    aux2+=str(i)+str(j)+";"
            aux2+="}"
            graph3+=aux2
            aux=""  

        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if j==0:
                    auxiliar=str(j)+str(i)
                    #aux+="\n\t{ rank ="+str(i)+str(j)+";"
                else:
                    graph3+="\n\t"+auxiliar+" -> "+str(j)+str(i)
                    graph3+="\n\t"+str(j)+str(i)+" -> "+auxiliar
                    auxiliar=str(j)+str(i)
                    #aux+=str(i)+str(j)+";"
    elif tipolist.lower()=="falso":
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if j==0:
                    auxiliar=str(i)+str(j)
                    aux2+="\n\t{ rank =same;"+str(i)+str(j)+";"
                else:
                    graph3+="\n\t"+auxiliar+" -> "+str(i)+str(j)
                    #graph3+="\n\t"+str(i)+str(j)+" -> "+auxiliar
                    auxiliar=str(i)+str(j)
                    aux2+=str(i)+str(j)+";"  
            aux2+="}"
            graph3+=aux2
            aux2=""  
        for i in range(len(matriz)):
            for j in range(len(matriz[0])):
                if j==0:
                    auxiliar=str(j)+str(i)
                    #aux+="\n\t{ rank ="+str(i)+str(j)+";"
                else:
                    graph3+="\n\t"+auxiliar+" -> "+str(j)+str(i)
                    #graph3+="\n\t"+str(j)+str(i)+" -> "+auxiliar
                    auxiliar=str(j)+str(i)
                    #aux+=str(i)+str(j)+";"
    
    unir=graph1+graph2+graph3+"\n}"
    Grafico(unir,"matriz")