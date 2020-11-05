from tkinter import messagebox as ms
import tkinter as tk
from Token import tokens
from lista import listavalue
from lista import listaerror,estados,llamar2,graficartabla,limpiarlistas
numero=1
matriz=[]
auxlista=[]
auxfilacount=0
auxcolcount=0
nombredefect=""
colordefect=""
tipolista=""
tipofigura=""
nombre=""
fila=0
i=0
tamanofila=0
cadena=""
errorcount=0
columna=0
estado=0
filamatriz= 0
columnamatriz=0
auxiliar=""
auxinodo=""
auxinodocount=0
banderamatriz=False
banderafila=False
banderanodo=False
banderadefecto=False
banderafila=False
banderallave=False
def analizadorTabla(texto):
    global fila,i,cadena,errorcount,fila,columna,estado,matriz,filamatriz,columnamatriz,auxfilacount,auxcolcount
    errorcount=0
    i=0
    fila=1
    columna=0
    estado=0
    errorcount=0
    filamatriz= 0
    columnamatriz=0
    limpiarlistas()
    auxfilacount=0
    auxcolcount=0
    tamanofila=0
    auxlista.clear()
    matriz.clear()
    cadena=texto+'\nλ'
    bandera=False
    while i< len(cadena) and bandera==False:
        #columna+=1
        #fila+=1
        concatenada= cadena[i]
        print(concatenada)
        if 'λ' in concatenada:
            bandera=True
            if errorcount>0:
                root=tk.Tk()
                root.withdraw()
                ms.showerror(title="error",message="EL analizador a terminado de leer el Archivo con "+str(errorcount)+" errores encontrados")
                root.destroy()
                print("EL analizador a terminado de leer el Archivo con "+str(errorcount)+" errores encontrados")
                llamar2()  
                graficartabla()
            else:
                root=tk.Tk()
                root.withdraw()                
                ms.showerror(title="error",message="EL analizador a terminado de leer el Archivo con "+str(errorcount)+" errores")
                root.destroy()  
                llamar2()  
                graficartabla()
                print("EL analizador a terminado de leer el Archivo con "+str(errorcount)+" errores")
                #return errorcount
        else:    
            switch(concatenada)
        #i+=1
def switch(concatenada):
    global estado
    if estado == 0:
        S0(concatenada)
    elif  estado==1:
        S1(concatenada)
    elif estado==2:       
        S2(concatenada)
    elif estado==3:
        S3(concatenada)
    elif estado==4:
        S4(concatenada)
    elif estado==5:
        S5(concatenada)
    elif estado==6:
        S6(concatenada)
    elif estado==7:
        S7(concatenada)
    elif estado==8:
        S8(concatenada)
    elif estado==9:
        S9(concatenada)
    elif estado==10:
        S10(concatenada)    
    elif estado==11:
        S11(concatenada)
    elif estado==12:
        S12(concatenada)
    elif estado==13:
        S13(concatenada)
    elif estado==14:
        S14(concatenada)    
    elif estado==15:
        S15(concatenada)
    elif estado==16:
        S16(concatenada)
    elif estado==17:
        S17(concatenada)
    elif estado==18:
        S18(concatenada)
    elif estado==19:
        S19(concatenada)
    elif estado==20:
        S20(concatenada)
    elif estado==21:
        S21(concatenada)
    elif estado==22:
        S22(concatenada)
    elif estado==23:
        S23(concatenada)
    elif estado==24:
        S24(concatenada)
def S0(concatenada):
    global fila,columna,i,errorcount,estado,auxiliar,banderamatriz,banderanodo,banderafila,banderadefecto,banderallave
    if "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=0
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=0
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=0
    elif concatenada.islower() or concatenada.isupper():
         auxiliar+=concatenada
         i+=1
         estado=1
         columna+=1 
    elif "}" in concatenada and banderallave== True:
        banderallave=False
        listavalue(fila,columna,concatenada,tokens(concatenada))
        i+=1
        columna+=1  
        estado=0    
    elif cadena[i]=="/" and cadena[i+1]=="/":
        banderacomentario=False
        if i==0:
            while i <len(cadena) and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=0
                    columna=0
                    banderacomentario=True
                i+=1
        else:
            while i and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=0
                    columna=0
                    banderacomentario=True
                i+=1 
    elif banderamatriz== True:
        estado=2
    elif banderafila==True:
        estado=8
    elif banderanodo==True:
        estado=9
    elif banderadefecto==True:
        estado=10   
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror     
        columna+=1
        i+=1
        estado=0   
def S1(concatenada):
    global i,fila,columna,errorcount,estado,auxiliar,banderamatriz,banderanodo,banderafila,banderadefecto
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        columna+=1
        estado=1
        i+=1
    elif '(' in concatenada:
        estado=0
        i+=1
        columna+=1
        if "tabla" in auxiliar.lower():
            banderamatriz=True
            if auxiliar.lower()=="tabla":
                listavalue(fila,columna,auxiliar,tokens(auxiliar))
            else:
                listaerror(fila,columna,auxiliar,"palabra desconocida")#aqui graabamos la listatokenerror
                errorcount+=1
            auxiliar=""
        elif "encabezados" in auxiliar.lower():
            banderanodo= True
            if auxiliar.lower()=="encabezados":
                listavalue(fila,columna,auxiliar,tokens(auxiliar))
            else:
                listaerror(fila,columna,auxiliar,"palabra desconocida")#aqui graabamos la listatokenerror
                errorcount+=1
            auxiliar=""
        elif "fila" in auxiliar.lower():
            banderafila=True
            if auxiliar.lower()=="fila":
                listavalue(fila,columna,auxiliar,tokens(auxiliar))
            else:
                listaerror(fila,columna,auxiliar,"palabra desconocida")#aqui graabamos la listatokenerror
                errorcount+=1
            auxiliar=""
        elif "defecto" in auxiliar.lower():
            banderadefecto=True
            if auxiliar.lower()=="defecto":
                listavalue(fila,columna,auxiliar,tokens(auxiliar))
            else:
                listaerror(fila,columna,auxiliar,"palabra desconocida")#aqui graabamos la listatokenerror
                errorcount+=1
            auxiliar=""
        else:
            errorcount+=1
            listaerror(fila,columna,auxiliar,"palabra desconocida")#aqui graabamos la listatokenerror
            auxiliar=""
        listavalue(fila,columna,concatenada,tokens(concatenada))
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=1
    elif cadena[i]=="/" and cadena[i+1]=="/":
        banderacomentario=False
        if i==0:
            while i <len(cadena) and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=0
                    columna=0
                    banderacomentario=True
                i+=1
        else:
            while i and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=0
                    columna=0
                    banderacomentario=True
                i+=1 
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=1
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=1
    elif cadena[i]=="/" and cadena[i+1]=="/":
        banderacomentario=False
        if i==0:
            while i <len(cadena) and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=1
                    columna=0
                    banderacomentario=True
                i+=1
        else:
            while i and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=1
                    columna=0
                    banderacomentario=True
                i+=1 
    else:
        if not auxiliar:
            errorcount+=1
            listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror     
            columna+=1
            estado=1
            i+=1
        else:
            errorcount+=2
            listaerror(fila,columna,auxiliar,"Desconocido")#aqui graabamos la listatokenerror  
            listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror  
            auxiliar=""   
            columna+=1
            estado=0
            i+=1
def S2(concatenada):
    global i, fila,columna, errorcount,auxiliar,banderallave,estado,banderamatriz,filamatriz,columnamatriz
    if "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=4
    elif concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=6
    elif concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=3
    elif "{" in concatenada:
        banderamatriz=False
        banderallave=True
        i+=1
        columna+=1
        estado=0
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=2
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=2
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=2 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"desconocido")#aqui graabamos la listatokenerror
        columna+=1
        i+=1
        estado=2
def S3(concatenada):
    global i, fila,columna, errorcount,auxiliar,estado,banderafila,filamatriz,columnamatriz,tamanofila
    if concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=3
    elif  concatenada==",":
        listavalue(fila,columna,auxiliar,tokens(auxiliar))
        listavalue(fila,columna,concatenada,tokens(concatenada))
        i+=1
        columna+=1
       # if banderafila==False:
        tamanofila=auxiliar
          #  banderafila=True
        #elif banderafila==True:
            #columnamatriz=auxiliar
           # banderafila=False
            #for x in range(int(filamatriz)):
        #matriz.append(["#"]*int(tamanofila+1))
        auxiliar=""
        estado=2
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=3
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=3
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=3 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror
        estado=3
        i+=1
        columna+=1
def S4(concatenada):
    global fila,columna,i,errorcount,auxiliar,estado
    if "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=4
    elif "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=5;
    else:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=4;
def S5(concatenada):
    global fila,columna,i,errorcount,auxiliar,estado,nombre
    if ")" in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar[0]))#aqui guardamos auxi en listatoken
        listavalue(fila,columna,concatenada,tokens(concatenada))#aqui guardamos signo en listatoken
        auxiliar=auxiliar.replace("'","")
        nombre=auxiliar
        auxiliar=""
        i+=1
        columna+=1
        estado=2;
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=5
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=5
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=5 
    else:
        errorcount+=1
        estado=5
        i+=1
        columna+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror     
def S6(concatenada):
    global i,columna,fila,auxiliar,errorcount,estado,tipofigura,auxfilacount,auxcolcount
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=6
    elif ")"in concatenada: #verdadero o falso
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken el signo
        auxlista.append([auxfilacount,auxcolcount,auxiliar])
        auxiliar=""
        estado=8
        auxcolcount+=1
        columna+=1
        i+=1
    elif "," in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken
        auxlista.append([auxfilacount,auxcolcount,auxiliar])
        estado=8
        auxcolcount+=1
        auxiliar=""
        listavalue(fila,columna,concatenada,tokens(concatenada))
        i+=1
        columna+=1
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=6
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=6
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=6 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror
        i+=1
        columna+=1
        i+=1
        estado=6 
def S8(concatenada):
    global i, fila,columna, errorcount,auxiliar,estado
    if "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=11
    elif concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=13
    elif concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=6
    elif "#" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=15
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=8
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=8
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=8
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=8
def S11(concatenada):
    global fila,columna,i,errorcount,auxiliar,estado
    if "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=11
    elif "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=12
    else:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=11
def S12(concatenada):
    global i,columna,fila,auxiliar,errorcount,estado,auxinodo,auxfilacount,auxcolcount,auxlista
    if ")"in concatenada:
        i+=1
        columna+=1
        listavalue(fila,columna,auxiliar,tokens(auxiliar[0]))#guardamos en listatoken
        listavalue(fila,columna,concatenada,tokens(concatenada))
        auxiliar=auxiliar.replace("'","")
        auxlista.append([auxfilacount,auxcolcount,auxiliar])
        auxcolcount+=1
        #auxinodo=auxiliar
        auxiliar=""
        estado=8
        # falta guardar signo
    elif "," in concatenada:
        i+=1
        columna+=1
        listavalue(fila,columna,auxiliar,tokens(auxiliar[0]))#guardamos en listatoken
        listavalue(fila,columna,concatenada,tokens(concatenada))
        auxiliar=auxiliar.replace("'","")
        auxlista.append([auxfilacount,auxcolcount,auxiliar])
        #matriz[auxfilacount][auxcolcount]=auxiliar
        auxcolcount+=1
        #auxinodo=auxiliar
        auxiliar=""
        estado=8
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=12
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=12
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=12
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1 
        estado=12  
def S13(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderafila,auxinodo,auxfilacount,auxcolcount,auxlista,tamanofila
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        estado=13
        columna+=1
    elif concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        estado=14
        columna+=1     
    elif ";" in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        matriz.append(["#"]*int(tamanofila))
        for li in range(len(auxlista)):
            matriz[auxlista[li][0]][auxlista[li][1]]=[auxlista[li][2],auxiliar]
            #estados(li,auxiliar)
        if (int(tamanofila)-len(auxlista))>0:
            x=0
            while x < (int(tamanofila)-len(auxlista)):
                matriz[auxfilacount][auxcolcount]=["#",auxiliar] 
                x+=1
                auxcolcount+=1  
        auxlista.clear()
        auxfilacount+=1
        auxcolcount=0
        auxiliar=""
        columna+=1
        i+=1
        banderafila=False
        estado=0       
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=13
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=13
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=13 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=13
def S14(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderafila,auxinodo,auxcolcount,auxfilacount,auxlista,matriz
    if ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        matriz.append(["#"]*int(tamanofila))
        for li in range(len(auxlista)):
            matriz[auxlista[li][0]][auxlista[li][1]]=[auxlista[li][2],auxiliar]
            #estados(li,auxiliar)
        if (int(tamanofila)-len(auxlista))>0:
            x=0
            while x < (int(tamanofila)-len(auxlista)):
                matriz[auxfilacount][auxcolcount]=["#",auxiliar] 
                x+=1
                auxcolcount+=1 
        auxlista.clear()
        auxfilacount+=1
        auxcolcount=0
        auxiliar=""
        columna+=1
        i+=1
        banderafila=False
        estado=0
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=14
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=14
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=14
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=14
def S15(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderafila,auxinodo,auxfilacount,auxcolcount,auxlista,tamanofila
    if ")" in concatenada:
        auxinodo=auxiliar
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        auxlista.append([auxfilacount,auxcolcount,auxiliar])
        auxcolcount+=1        
        auxiliar=""
        columna+=1
        i+=1
        estado=8   
    elif "," in concatenada:
        auxinodo=auxiliar
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        auxlista.append([auxfilacount,auxcolcount,auxiliar])
        auxcolcount+=1           
        auxiliar=""
        columna+=1
        i+=1
        estado=8 
    elif ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        matriz.append(["#"]*int(tamanofila))
        for li in range(len(auxlista)):
            matriz[auxlista[li][0]][auxlista[li][1]]=[auxlista[li][2],auxiliar]
            #estados(li,auxiliar)
        if (int(tamanofila)-len(auxlista))>0:
            x=0
            while x < (int(tamanofila)-len(auxlista)):
                matriz[auxfilacount][auxcolcount]=["#",auxiliar] 
                x+=1
                auxcolcount+=1          
        auxlista.clear()
        auxfilacount+=1
        auxcolcount=0
        auxiliar=""
        columna+=1
        i+=1
        banderafila=False
        estado=0
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=15
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=15
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=15 
    elif cadena[i]=="/" and cadena[i+1]=="/":
        banderacomentario=False
        if i==0:
            while i <len(cadena) and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=15
                    columna=0
                    banderacomentario=True
                i+=1
        else:
            while i and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=15
                    columna=0
                    banderacomentario=True
                i+=1 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=15   
def S9(concatenada):
    global i, fila,columna, errorcount,auxiliar,estado
    if "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=17
    elif concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=7
    elif concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=16
    elif "#" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=19
    elif cadena[i]=="/" and cadena[i+1]=="/":
        banderacomentario=False
        if i==0:
            while i <len(cadena) and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=9
                    columna=0
                    banderacomentario=True
                i+=1
        else:
            while i and banderacomentario==False:
                if cadena[i]=="\n":
                    fila+=1
                    estado=9
                    columna=0
                    banderacomentario=True
                i+=1 
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=9
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=9
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=9
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror
        estado=9
        columna+=1    
def S7(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderanodo,auxinodo,auxcolcount,auxfilacount,auxlista,matriz
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        estado=7
        columna+=1
    elif concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        estado=24
        columna+=1     
    elif ";" in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        #matriz[int(filamatriz)-1][int(columnamatriz)-1]=[auxinodo,auxiliar] 
        #estados(auxinodo,auxiliar)# aqui debo de aregralar esto
        matriz.insert(0,["#"]*int(tamanofila))
        for li in range(len(auxlista)):
            matriz[auxlista[li][0]][auxlista[li][1]]=[auxlista[li][2],auxiliar]
        if (int(tamanofila)-len(auxlista))>0:
            x=0
            while x < (int(tamanofila)-len(auxlista)):
                matriz[auxfilacount][auxcolcount]=["#",auxiliar] 
                x+=1
                auxcolcount+=1      
        #auxinodo=""
        auxlista.clear()
        auxfilacount+=1
        auxcolcount=0
        auxiliar=""
        columna+=1
        i+=1
        banderanodo=False
        estado=0       
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=7
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=7
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=10 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=7        
def S24(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderanodo,auxinodo,auxlista,auxcolcount,auxfilacount,numero,filamatriz,columnamatriz,tamanofila
    if ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        #matriz[int(filamatriz)-1][int(columnamatriz)-1]=[auxinodo,auxiliar]    
        matriz.insert(0,["#"]*int(tamanofila))
        for li in range(len(auxlista)):
            matriz[auxlista[li][0]][auxlista[li][1]]=[auxlista[li][2],auxiliar]
        if (int(tamanofila)-len(auxlista))>0:
            x=0
            while x < (int(tamanofila)-len(auxlista)):
                matriz[auxfilacount][auxcolcount]=["#",auxiliar] 
                x+=1
                auxcolcount+=1 
        #auxinodo=""
        auxlista.clear()
        auxcolcount=0
        auxfilacount+=1
        auxiliar=""
        columna+=1
        i+=1
        banderanodo=False
        estado=0
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=24
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=24
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=24
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=24  
def S17(concatenada):
    global fila,columna,i,errorcount,auxiliar,estado
    if "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=17
    elif "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=18
    else:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=17
def S18(concatenada):
    global i,columna,fila,auxiliar,errorcount,estado,auxinodo,columnamatriz,filamatriz,auxfilacount,matriz,auxlista,auxcolcount
    if ")"in concatenada:
        i+=1
        columna+=1
        listavalue(fila,columna,auxiliar,tokens(auxiliar[0]))#guardamos en listatoken
        listavalue(fila,columna,concatenada,tokens(concatenada))
        auxiliar=auxiliar.replace("'","")   
        auxlista.append([0,auxcolcount,auxiliar])
        auxcolcount+=1
        #auxinodo=auxiliar
        auxiliar=""
        estado=9
        # falta guardar signo
    elif "," in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar[0]))#guardamos en listatoken
        listavalue(fila,columna,concatenada,tokens(concatenada))
        auxiliar=auxiliar.replace("'","")   
        auxlista.append([0,auxcolcount,auxiliar])      
        auxiliar=""
        i+=1
        auxcolcount+=1
        columna+=1
        estado=9
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=18
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=18
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=18
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1 
        estado=18
def S16(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,auxinodocount,banderafila,auxcolcount,auxfilacount,filamatriz,columnamatriz
    if concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=16
    elif "," in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        #auxinodocount=int(auxiliar)
        if banderafila==False:
            filamatriz=auxiliar
            banderafila=True
        elif banderafila==True:
            columnamatriz=auxiliar
            banderafila=False
        auxiliar=""
        columna+=1
        i+=1
        estado=9
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=16
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=16
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=16
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui grabamos la listatokenerror 
        i+=1
        columna+=1
        estado=16             
def S19(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderafila,auxinodo,filamatriz,columnamatriz,matriz
    if ")" in concatenada:
        auxinodo=auxiliar
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        auxinodo=auxiliar
        auxiliar=""
        columna+=1
        i+=1
        estado=9   
    #elif "," in concatenada:
        #auxinodo=auxiliar
        #listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        #listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        #auxiliar=""
        #columna+=1
        #i+=1
        #estado=9 
    elif ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        matriz[int(filamatriz)-1][int(columnamatriz)-1]=[auxinodo,auxiliar] 
        #estados(auxinodo,auxiliar)
        auxinodo=""
        auxiliar=""
        columna+=1
        i+=1
        banderafila=False
        estado=0
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=19
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=19
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=19 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=19  
def S10(concatenada):
    global i, fila,columna, errorcount,auxiliar,estado
    if "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=20
    elif concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=22
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=10
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=10
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=10
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=10 
def S20(concatenada):
    global fila,columna,i,errorcount,auxiliar,estado
    if "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=20
    elif "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=21
    else:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=20 
def S21(concatenada):
    global i,columna,fila,auxiliar,errorcount,estado,nombredefect
    if ")"in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar[0]))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos la listatoken el simbolo
        auxiliar=auxiliar.replace("'","")
        nombredefect=auxiliar
        auxiliar=""
        i+=1
        columna+=1
        estado=10
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=21
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=21
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=21
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1 
        estado=21    
def S22(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,colordefect,banderadefecto
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        estado=22
        columna+=1
    elif concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        estado=23
        columna+=1       
    elif ";" in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        colordefect=auxiliar
        auxiliar=""
        columna+=1
        i+=1
        banderadefecto=False
        estado=0 
        for x in range(len(matriz)):
            for y in range(len(matriz[0])):
                if len(matriz[x][y])>1:
                    if matriz[x][y][0]=="#"and matriz[x][y][1]!="#":
                        matriz[x][y][0]=nombredefect
                    elif matriz[x][y][0]!="#"and matriz[x][y][1]=="#":
                        matriz[x][y][1]=colordefect
                    elif matriz[x][y][0]=="#"and matriz[x][y][1]=="#":  
                        matriz[x][y][0]=nombredefect
                        matriz[x][y][1]=colordefect
                        #print(len(matriz[x][y]))
                elif len(matriz[x][y])==1:
                    matriz[x][y]=[nombredefect,colordefect]  
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=22
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=22
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=22 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=22
def S23(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderadefecto,colordefect,matriz,nombredefect
    if ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        colordefect=auxiliar;
        auxiliar=""
        columna+=1
        i+=1
        banderadefecto=False
        estado=0
        for x in range(len(matriz)):
            for y in range(len(matriz[0])):
                if len(matriz[x][y])>1:
                    if matriz[x][y][0]=="#"and matriz[x][y][1]!="#":
                        matriz[x][y][0]=nombredefect
                    elif matriz[x][y][0]!="#"and matriz[x][y][1]=="#":
                        matriz[x][y][1]=colordefect
                    elif matriz[x][y][0]=="#"and matriz[x][y][1]=="#":  
                        matriz[x][y][0]=nombredefect
                        matriz[x][y][1]=colordefect
                        #print(len(matriz[x][y]))
                elif len(matriz[x][y])==1:
                    matriz[x][y]=[nombredefect,colordefect]
                    
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=23
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=23
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=23 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=23      