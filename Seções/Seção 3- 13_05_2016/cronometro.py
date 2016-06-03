#-*- encoding=UTF-8 -*-

import time
import sys

import Tkinter # importa o modulo para interface grafica
rel = Tkinter.Label() # criar uma label vazia
rel.pack() # deixa o conteudo visivel dentro da label
rel['font'] = 'Helvita 50 bold' # define a fonte do relogio
rel['foreground'] = 'blue' # define a cor dos numeros
rel['bg'] = 'white' # define a cor do fundo bg e a abreviatura de background
rel['height'] = 3 # define a altura da janela
rel['width'] = 10 # define a largura da janela
i = int(raw_input('Minutos dessa seção:')) * 60
def contador(): # funcao contador
        global i
        rel['text'] = i
        i -= 1
        rel.after(1000, contador) # essa parte do codigo e muito legal. a cada 100O milisegundos ou 1 segundo a funcao contador sera chamada e os segundos serão!

contador() # chama a funcao contador
rel.mainloop()
