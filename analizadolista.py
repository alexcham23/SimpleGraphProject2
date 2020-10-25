from tkinter import messagebox as ms
import tkinter as tk
fila=0
i=0
cadena=""
errorcount=0
columna=0
estado=0
auxiliar=""
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
                print("EL analizador a terminado de leer el Archivo con "+str(errorcount)+" errores")
                return errorcount
        else:    
            switch(concatenada)
        #i+=1
def switch(concatenada):
    global estado
    if '0' in str(estado):
        S0(concatenada)
    elif '1'in  str(estado):
        S1(concatenada)
    elif '2' in str(estado):       
        S2(concatenada)
    elif '3' in str(estado):
        S3(concatenada)
    elif '4' in str(estado):
        S4(concatenada)
    elif '5' in str(estado):
        S5(concatenada)
    elif '6' in str(estado):
        S6(concatenada)
    elif '7' in str(estado):
        S7(concatenada)
    elif '8' in str(estado):
        S8(concatenada)
    elif '9' in str(estado):
        S9(concatenada)
    elif '10' in str(estado):
        S10(concatenada)    
    elif '11' in str(estado):
        S11(concatenada)
    elif '12' in str(estado):
        S12(concatenada)
    elif '13' in str(estado):
        S13(concatenada)
    elif '14' in str(estado):
        S14(concatenada)    
    elif '15' in str(estado):
        S15(concatenada)
    elif '16' in str(estado):
        S16(concatenada)
    elif '17' in str(estado):
        S17(concatenada)
    elif '18' in str(estado):
        S18(concatenada)
    elif '19' in str(estado):
        S19(concatenada)
    elif '20' in str(estado):
        S20(concatenada)
    elif '21' in str(estado):
        S21(concatenada)
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
    elif banderalista== True:
        estado=2
    elif banderanodo==True:
        estado=3
    elif banderanodos==True:
        estado=4
    elif banderadefecto==True:
        estado=16    
    elif "}" in concatenada and banderallave== True:
        banderallave=False
        #guardar listatoken el 
        i+=1
        columna+=1      
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
            #aqui graabamos la listatoken
            auxiliar=""
        elif auxiliar.lower()=="nodo":
            banderanodo= True
            #aqui graabamos la listatoken
            auxiliar=""
        elif auxiliar.lower()=="nodos":
            banderanodos=True
            #aqui graabamos la listatoken
            auxiliar=""
        elif auxiliar.lower()=="defecto":
            banderadefecto=True
            #aqui graabamos la listatoken
            auxiliar=""
        else:
            errorcount+=1
            #aqui graabamos la listatokenerror
            auxiliar=""
        #aqui graabamos la listatoken el signo
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
        #aqui graabamos la listatokenerror     
def S2(concatenada):
    global i, fila,columna, errorcount,auxiliar,banderallave
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
        estado=7
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
        #aqui graabamos la listatokenerror
def S3(concatenada):
    global i, fila,columna, errorcount,auxiliar
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
        estado=2 
    else:
        errorcount+=1
        #aqui graabamos la listatokenerror
        estado=3
def S4(concatenada):
    global i, fila,columna, errorcount,auxiliar
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=4                     
def S5(concatenada):
    global fila,columna,i,errorcount,auxiliar
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
    global fila,columna,i,errorcount,auxiliar
    if "," in concatenada:
        #aqui guardamos auxi en listatoken
        #aqui guardamos signo en listatoken
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
        #aqui graabamos la listatokenerror    
def S7(concatenada):
    global i,columna,fila,auxiliar,errorcount
    if concatenada.islower() or concatenada.isupper():
        i+=1
        columna+=1
        estado=7
    elif ")"in concatenada: #verdadero o falso
        i+=1
        columna+=1
        if auxiliar.lower()=="verdadero":
            #guardamos en listatoken
            auxiliar=""
            estado=2
        elif auxiliar.lower() =="falso":
            #guardamos en listatoken
            auxiliar=""
            estado=2
        else:
            errorcount+=1
            #aqui graabamos la listatokenerror
            auxiliar=""
            estado=2
        #guardamos en listatoken el signo
    elif "," in concatenada:
        estado=2
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
        #aqui graabamos la listatokenerror
        i+=1
        columna+=1
        estado=7 
def S8(concatenada): 
    global fila,columna,i,errorcount,auxiliar
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
    global i,columna,fila,auxiliar,errorcount
    if ")"in concatenada:
        i+=1
        columna+=1
        #guardamos en listatoken
        auxiliar=""
        estado=3
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1 
        estado=9   
def S10(concatenada):
    global i,fila,columna,errorcount,auxiliar
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=10        
def S11(concatenada):
    global i,fila,columna,errorcount,auxiliar
    if concatenada.isdigit():
        auxiliar+=concatenada
        i+=1
        columna+=1
        estado=11
    elif "," in concatenada:
        #guardamos en listatoken auxiliar
        #guardamos en listatoken signo
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=11                        
def S12(concatenada): 
    global fila,columna,i,errorcount,auxiliar
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
    global i,fila,columna,errorcount,auxiliar
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=15    
def S14(concatenada):
    global i,columna,fila,auxiliar,errorcount
    if ")"in concatenada:
        i+=1
        columna+=1
        #guardamos en listatoken auxiliar
        #guardamos la listatoken el simbolo
        auxiliar=""
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1 
        estado=14   
def S15(concatenada):
    global i,fila,columna,errorcount,auxiliar
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=15        
def S16(concatenada):
    global i, fila,columna, errorcount,auxiliar
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=16                     
def S17(concatenada):
    global fila,columna,i,errorcount,auxiliar
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
    global i,columna,fila,auxiliar,errorcount
    if ")"in concatenada:
        i+=1
        columna+=1
        #guardamos en listatoken auxiliar
        #guardamos la listatoken el simbolo
        auxiliar=""
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1 
        estado=18       
def S19(concatenada):
    global i,fila,columna,errorcount,auxiliar
    if ";"  in concatenada:
        #guardamos en listatoken auxiliar
        #guardamos en listatoken signo
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=19        
def S20(concatenada):
    global i,fila,columna,errorcount,auxiliar
    if ";"  in concatenada:
        #guardamos en listatoken auxiliar
        #guardamos en listatoken signo
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=20            
def S21(concatenada):
    global i,fila,columna,errorcount,auxiliar
    if ";"  in concatenada:
        #guardamos en listatoken auxiliar
        #guardamos en listatoken signo
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
        #aqui graabamos la listatokenerror 
        i+=1
        columna+=1
        estado=21   