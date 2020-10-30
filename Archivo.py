from tkinter import filedialog
import tkinter as tk
from analizadolista import analizador
from analizadormatriz import analizadorMatriz
#from numeroaleatorios import aleatorios

def lectura():
    ls= tk.Tk()
    ls.title("Archivo")
    ls.withdraw()
    ls.filename= filedialog.askopenfilename(initialdir="c:/Desktop",title="Seleccionar Archivo",filetypes=(("lfp files","*.lfp"),("all files","*.*")))
    ls.destroy()
    ls.mainloop()
   
    file=open(ls.filename,"r",encoding='utf-8')#codig utf-8 archivo
    info=""
    for obten in file.readlines():
        info += obten
    if 'lista' in info.lower():
        analizador(info)
    elif 'matriz' in info.lower():
        analizadorMatriz(info)
    #contador=analizador(info)
    #return contador
    info=""
    file.close()   

    #aleatorios(info)