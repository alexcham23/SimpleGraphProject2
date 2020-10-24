#from Archivo import lectura
#from graphlist import graphfull
#from graphlist import generalizar

contador=0
banderaleer=False
def winprin():
    import tkinter as tk
    import tkinter.messagebox as ms
    import sys

    #creando la ventana principal
    ventana = tk.Tk()
    ventana.title("Proyecto #1 - LFP")
    #configuramos el tamaño de la ventana principal
    ventana.geometry('380x340')

    # panels
    panel1 = tk.Frame()
    panel1.config(bd=50, width=200, height=60)
    panel1.grid(row=1, column=100)
    panel1.grid_rowconfigure(0, weight=1)
    panel1.pack(side="top", fill="both", expand=True)

    # creando el evento

    def imprimr(event):
            ventanad()


    def ventanad():
        #Ahora creamos la ventan secudaria que resibira la respuesta del menu
        ventana2 = tk.Tk()
        ventana2.title("Seleccionar")
        e = tk.Entry(ventana2)
        e.pack()
        e.focus_set()

        def callback(): 
            global contador,banderaleer

            if e.get() =="1":
                ventana2.destroy() #cerrando la ventana secundaria tipo dispose
                ventana.destroy() #cerrando la ventana principal tipo dispose
                contador=lectura()#llamamos al metodo lectura de archivo
                banderaleer=True
                winprin()
            elif e.get() =="2":
                ventana2.destroy()
                ventana.destroy()
 
                            
            elif e.get()== "3":
                ventana2.destroy()
                ventana.destroy()
                sys.exit()              
            else:
                ventana2.destroy()
                ms.showerror(title="Error", message="Error Intentelo de Nuevo")
                ventanad()


        #creaando un evento clic de tipo boton para que reconosca el click en el label
        botton = tk.Button(ventana2, text="ok", width=10, command= callback)
        botton.pack()

        ventana2.mainloop()

    #creando utilidades en la ventana principal
    label = tk.Label(
    panel1, text="Proyecto #2 \nLenguajes Formales de Programacion\nseccion \"A-\"\nJaime Alejandro Armira Us\n 201602983", relief="solid")
    label.config(font=(12))
    label.pack(side="top", fill="x", pady=10)
    label2 = tk.Label(
    panel1, text="1. Cargar Archivo\n2. Generar Grafica\n3. Salir\n\n\n>> Ingrese una Opcion:")
    label2.place(x=0, y=50, width=100, height=50)
    label2.config(justify="left", font=(12))
    label2.pack(side="left")
    label2.bind('<Button-1>', imprimr)


#label3=tk.Label(panel1,text="1. Cargar Archivo\n2. Graficar Operacion\n3. Salir")
#label3.place(x=0 , y=50, width=100, height=50)
# label3.config(justify="left",font=(12))
# label3.pack(side="left")

    ventana.mainloop()
winprin()