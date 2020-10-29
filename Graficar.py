import graphviz
from graphviz import Digraph
from graphviz import Source
from graphviz import render
import os.path as path
import os
ruta=""
def guardar():
    global ruta
    ruta=os.path.join(os.path.join(os.environ['USERPROFILE']),'Desktop')+"\\projectGraphviz"
    print(ruta)
    if os.path.isdir(ruta):
        print("La carpeta existe en la Raiz")
    else:
        os.mkdir(ruta) 
        print("carpeta fue creada con exito")  

def Grafico(graphi,name):
    global ruta
    guardar()
    if  path.exists(''+ruta+'\\'+name+'.gv.svg') and path.exists(''+ruta+'\\'+name+'.gv'): 
        os.remove(''+ruta+'\\'+name+'.gv.svg')
        os.remove(''+ruta+'\\'+name+'.gv')   
      #d = Digraph(format='png')
        d=Source(graphi)
        #d.source(grafo)
        #d.format='png'
        d.render(''+name+'.gv', ruta,format='png',view=False) 
        d.render(''+name+'.gv',ruta,format='svg',view=False)
        #render('dot', 'png',name+'.gv') 
    else:
      #d = Digraph(format='png')
      d=Source(graphi)
      #d.source(grafo)
      #d.format='png'
      #d.format='pdf'
      d.render(''+name+'.gv',ruta,format='png',view=False)
      d.render(''+name+'.gv',ruta,format='svg',view=False)
      
      