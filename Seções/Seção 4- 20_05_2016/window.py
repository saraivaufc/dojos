#-*- encoding=UTF-8 -*-

from Tkinter import *

i = int(raw_input('Minutos dessa seção:')) * 60

root = Tk()
root.wm_attributes("-topmost", 1)
root.texto = Label(root, text=str(i))
root.texto['width']=5
root.texto['height']=3
root.texto['font'] = 'Helvita 50 bold'
root.texto['foreground'] = 'blue'
root.texto['bg'] = 'white'

def contador(): # funcao contador
        global i
        root.texto['text'] = str(i)
        root.texto.pack()
        i -= 1
        root.after(1000, contador)
         
contador()

root.mainloop()
