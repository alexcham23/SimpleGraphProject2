from tkinter import messagebox as ms
import tkinter as tk
from Token import tokens
from lista import listavalue
from lista import listaerror,estados,llamar,graficarlist
nombredefect=""
colordefect=""
tipolista=""
tipofigura=""
nombre=""
fila=0
i=0
cadena=""
errorcount=0
columna=0
estado=0
auxiliar=""
auxinodo=""
auxinodocount=0
banderalista=False
banderanodo=False
banderanodos=False
banderadefecto=False
banderallave=False
def analizador(texto):
    global fila,i,cadena,errorcount,fila,columna,estado
    errorcount=0
    i=0
    fila=1
    columna=0
    estado=0
    cadena=texto+'λ'
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
                return errorcount
            else:
                root=tk.Tk()
                root.withdraw()                
                ms.showerror(title="error",message="EL analizador a terminado de leer el Archivo con "+str(errorcount)+" errores")
                root.destroy()  
                llamar()  
                graficarlist()
                print("EL analizador a terminado de leer el Archivo con "+str(errorcount)+" errores")
                return errorcount
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
def S0(concatenada):
    global fila,columna,i,errorcount,estado,auxiliar,banderalista,banderanodo,banderanodos,banderadefecto,banderallave
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
        while i and banderacomentario==False:
            if cadena[i]=="\n":
                fila+=1
                estado=0
                columna=0
                banderacomentario=True
            i+=1    
    elif banderalista== True:
        estado=2
    elif banderanodo==True:
        estado=3
    elif banderanodos==True:
        estado=4
    elif banderadefecto==True:
        estado=16   
def S1(concatenada):
    global i,fila,columna,errorcount,estado,auxiliar,banderalista,banderanodo,banderanodos,banderadefecto
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        columna+=1
        estado=1
        i+=1
    elif '(' in concatenada:
        estado=0
        i+=1
        columna+=1
        if auxiliar.lower()== "lista":
            banderalista=True
            listavalue(fila,columna,auxiliar,tokens(auxiliar))
            auxiliar=""
        elif auxiliar.lower()=="nodo":
            banderanodo= True
            listavalue(fila,columna,auxiliar,tokens(auxiliar)) #aqui graabamos la listatoken
            auxiliar=""
        elif auxiliar.lower()=="nodos":
            banderanodos=True
            listavalue(fila,columna,auxiliar,tokens(auxiliar))#aqui graabamos la listatoken
            auxiliar=""
        elif auxiliar.lower()=="defecto":
            banderadefecto=True
            listavalue(fila,columna,auxiliar,tokens(auxiliar)) #aqui graabamos la listatoken
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
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=1
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=1 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror     
        columna+=1
        estado+=1
def S2(concatenada):
    global i, fila,columna, errorcount,auxiliar,banderallave,estado,banderalista
    if "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=5
    elif concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=7
    elif "{" in concatenada:
        banderalista=False
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
        estado=2
def S3(concatenada):
    global i, fila,columna, errorcount,auxiliar,estado
    if "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=8
    elif concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=10
    elif "#" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=22
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
        columna+=1
def S4(concatenada):
    global i, fila,columna, errorcount,auxiliar,estado
    if concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=11
    elif "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=12
    elif concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=15
    elif "#" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=23
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=4
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=4
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=4
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=4                     
def S5(concatenada):
    global fila,columna,i,errorcount,auxiliar,estado
    if "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=5
    elif "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=6;
    else:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=5;
def S6(concatenada):
    global fila,columna,i,errorcount,auxiliar,estado,nombre
    if "," in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#aqui guardamos auxi en listatoken
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
        estado=6
        columna+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror    
def S7(concatenada):
    global i,columna,fila,auxiliar,errorcount,estado,tipofigura,tipolista
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=7
    elif ")"in concatenada: #verdadero o falso
        
        columna+=1
        if auxiliar.lower()=="verdadero":
            listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken
            tipolista=auxiliar
            auxiliar=""
            estado=2
        elif auxiliar.lower() =="falso":
            listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken
            tipolista=auxiliar
            auxiliar=""
            estado=2
        else:
            errorcount+=1
            listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror
            auxiliar=""
            estado=2
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken el signo
        i+=1
    elif "," in concatenada:
        estado=2
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken
        auxiliar=auxiliar.replace("'","")
        tipofigura=auxiliar
        auxiliar=""
        listavalue(fila,columna,concatenada,tokens(concatenada))
        i+=1
        columna+=1
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
        estado=7 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror
        i+=1
        columna+=1
        estado=7 
def S8(concatenada): 
    global fila,columna,i,errorcount,auxiliar,estado
    if "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=8
    elif "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=9;
    else:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=8;
def S9(concatenada):
    global i,columna,fila,auxiliar,errorcount,estado,auxinodo
    if ")"in concatenada:
        i+=1
        columna+=1
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken
        listavalue(fila,columna,concatenada,tokens(concatenada))
        auxiliar=auxiliar.replace("'","")
        auxinodo=auxiliar
        auxiliar=""
        estado=3
        # falta guardar signo
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
        i+=1
        columna+=1 
        estado=9   
def S10(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderanodo,auxinodo
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        estado=10
        columna+=1
    elif concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        estado=20
        columna+=1     
    elif ";" in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        estados(auxinodo,auxiliar)
        auxinodo=""
        auxiliar=""
        columna+=1
        i+=1
        banderanodo=False
        estado=0       
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
def S11(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,auxinodocount
    if concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=11
    elif "," in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        auxinodocount=int(auxiliar)
        auxiliar=""
        columna+=1
        i+=1
        estado=4
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=11
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=11
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=11 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui grabamos la listatokenerror 
        i+=1
        columna+=1
        estado=11                        
def S12(concatenada): 
    global fila,columna,i,errorcount,auxiliar,estado
    if "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=12
    elif "'" in concatenada:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=14;
    else:
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=12  
def S13(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,colordefect
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        estado=13
        columna+=1
    elif concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        estado=21
        columna+=1       
    elif ";" in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        colordefect=auxiliar
        auxiliar=""
        columna+=1
        i+=1
        banderanodo=False
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
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=15    
def S14(concatenada):
    global i,columna,fila,auxiliar,errorcount,estado,auxinodo
    if ")"in concatenada:
        auxinodo=auxiliar
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(auxiliar))#guardamos la listatoken el simbolo
        auxiliar=""
        i+=1
        columna+=1
        estado=4
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
    global i,fila,columna,errorcount,auxiliar,estado,auxinodo,auxinodocount
    if concatenada.islower() or concatenada.isupper():
        auxiliar+=concatenada
        i+=1
        estado=15
        columna+=1
    elif concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        estado=21
        columna+=1   
    elif ";" in concatenada:
        
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        auxinodo=auxinodo.replace("'","" )
        x=0
        while x<auxinodocount:
            estados(auxinodo+str(x+1),auxiliar)
            x+=1
        auxinodo=""
        auxiliar=""
        columna+=1
        i+=1
        banderanodo=False
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
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=15        
def S16(concatenada):
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
        estado=13
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
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=16                     
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
    global i,columna,fila,auxiliar,errorcount,estado,nombredefect
    if ")"in concatenada:

        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos la listatoken el simbolo
        auxiliar=auxiliar.replace("'","")
        nombredefect=auxiliar
        auxiliar=""
        i+=1
        columna+=1
        estado=16
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
def S19(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderadefecto,colordefect
    if ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        colordefect=auxiliar;
        auxiliar=""
        columna+=1
        i+=1
        banderadefecto=False
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
def S20(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderanodo,auxinodo
    if ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        estados(auxinodo,auxiliar)
        auxinodo=""
        auxiliar=""
        columna+=1
        i+=1
        banderanodo=False
        estado=0
    elif "\n" in concatenada:
        i+=1
        fila+=1
        columna=0
        estado=20
    elif "\t" in concatenada:
        i+=1
        columna+=8;
        estado=20
    elif " " in concatenada:
        i+=1
        columna+=1;
        estado=20 
    else:
        errorcount+=1
        listaerror(fila,columna,concatenada,"Desconocido")#aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=20            
def S21(concatenada):
    global i,fila,columna,errorcount,auxiliar,estado,banderanodos,auxinodocount,auxinodo
    if ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        auxinodo=auxinodo.replace("'","" )
        x=0
        while x<auxinodocount:
            estados(auxinodo+str(x+1),auxiliar)
            x+=1
        auxinodo=""
        auxiliar=""
        columna+=1
        i+=1
        banderanodos=False
        estado=0
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
    global i,fila,columna,errorcount,auxiliar,estado,banderanodo,auxinodo
    if ")" in concatenada:
        auxinodo=auxiliar
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        auxiliar=""
        columna+=1
        i+=1
        estado=3   
    elif ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        estados(auxinodo,auxiliar)
        auxinodo=""
        auxiliar=""
        columna+=1
        i+=1
        banderanodo=False
        estado=0
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
    global i,fila,columna,errorcount,auxiliar,estado,banderanodos,auxinodo,auxinodocount
    if ")" in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        auxiliar=""
        columna+=1
        i+=1
        estado=4   
    elif ";"  in concatenada:
        listavalue(fila,columna,auxiliar,tokens(auxiliar))#guardamos en listatoken auxiliar
        listavalue(fila,columna,concatenada,tokens(concatenada))#guardamos en listatoken signo
        auxinodo=auxinodo.replace("'","" )
        x=0
        while x<auxinodocount:
            estados(auxinodo+str(x+1),auxiliar)
            x+=1
        auxinodo=""
        auxiliar=""
        columna+=1
        i+=1
        banderanodos=False
        estado=0
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