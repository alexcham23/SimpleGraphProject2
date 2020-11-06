import webbrowser
def pageweb():
    from lista import error
    from lista import evalue
    from lista import tipo
    aux=""
    mensaje2=""
    f = open('Reporte.html','w')
    mensaje ="""<html>
        <head><style>
        table {
        width:0;
        }
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        }
        th, td {
        padding: 15px;
        text-align: left;
        }
        #t01 tr:nth-child(even) {
        background-color: #eee;
        }
        #t01 tr:nth-child(odd) {
        background-color: #fff;
        }
        #t01 th {
        background-color: black;
        color: white;
        }
        </style>
    </head>
        """

    if not error:
        if tipo==1:
            mensaje1="""<center>
        <div>
            <h2>Grafica<generada</h2><br><br><br>
            <img src="C:/Users/alexcham23/Desktop/projectGraphviz/lista.gv.svg"/>
        </div>
        """
        elif tipo==2:
            mensaje1="""<center>
            <div>
                <h2>Grafica<generada</h2><br><br><br>
                <img src="C:/Users/alexcham23/Desktop/projectGraphviz/matriz.gv.svg"/>
            </div>
            """
        elif tipo==3:
            mensaje1="""<center>
            <div>
                <h2>Grafica<generada</h2><br><br><br>
                <img src="C:/Users/alexcham23/Desktop/projectGraphviz/tabla.gv.svg"/>
            </div>
            """        
        mensaje2="""<div>
        <h2>TABLA DE TOKENS</h2><br><br>
        <table id="t01">
        <tr>
            <th>No.</th>
            <th>Fila</th>
            <th>Columna</th>
            <th>Lexema</th>
            <th>Token</th>
        </tr>
        """
        X=0
        for i in range(len(evalue)):
            aux+="<tr>\n"
            aux+="<td>"+str(X)+"</td>\n"
            X+=1
            for j in range(4):
                aux+="<td>"+str(evalue[i][j])+"</td>\n"
            aux+="</tr>\n"
        aux+="""
        </table>
        </div>        
        """
        mensaje2+=aux
        aux=""
        mesaje3="""   
        </center>
        </html>"""
    
        unir=mensaje+mensaje1+mensaje2+mesaje3
        f.write(unir)
        f.close()
    else:
 
        mensaje2+="""<center><div>
             <h2>TABLA DE ERROR</h2><br><br>
            <table id="t01">
            <tr>
            <th>No.</th>
            <th>Fila</th>
            <th>Columna</th>
            <th>Caracter</th>
            <th>Descripcion</th>
            </tr>
            """
        X=0
        for i in range(len(error)):
            aux+="<tr>\n"
            aux+="<td>"+str(X)+"</td>\n"
            X+=1
            for j in range(4):
                aux+="<td>"+str(error[i][j])+"</td>\n"
            aux+="</tr>\n"
        aux+="""
        </table>
        </div>        
        """
        mensaje2+=aux
        aux=""     
        mesaje3="""   
        </center>
        </html>"""
     
        unir=mensaje+mensaje2+mesaje3
        f.write(unir)
        f.close()   


    #Cambia la ruta para indicar la localización del archivo
    #nombreArchivo = 'file:///Users/username/Desktop/programming-historian/' + 'holamundo.html'
    #webbrowser.open_new_tab(nombreArchivo)
    d=webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
    d.open_new_tab('file:///E:/[LFA]2S_2020/Proyecto2/Reporte.html')
