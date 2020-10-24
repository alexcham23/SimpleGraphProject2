from tkinter import filedialog
import tkinter as tk
#from Analizador import analizador
#from numeroaleatorios import aleatorios

def lectura():
    ls= tk.Tk()
    ls.title("Archivo")
    ls.withdraw()
    ls.filename= filedialog.askopenfilename(initialdir="c:/Desktop",title="Seleccionar Archivo",filetypes=(("txt files","*.txt"),("all files","*.*")))
    ls.destroy()
    ls.mainloop()
   
    file=open(ls.filename,"r",encoding='utf-8')
    info=""
    for obten in file.readlines():
        info += obten

    #contador=analizador(info)
    #return contador
    info=""
    file.close()   

    #aleatorios(info)