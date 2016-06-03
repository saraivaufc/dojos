from Tkinter import * 
class Window: 
	def __init__(self, Tk): 
		self.containers = [Frame(Tk), Frame(Tk), Frame(Tk), Frame(Tk)]
		self.containers[0].pack(side=LEFT)
		self.containers[1].pack(side=RIGHT)
		self.containers[2].pack(side=TOP)
		self.containers[3].pack(side=BOTTOM)
		
		self.b1 = Button(self.containers[0], text="ola", width=10, height=10)
		self.b1.pack()
		Button(self.containers[1], text="eu", width=10, height=10).pack()
		Button(self.containers[2], text="sd", width=10, height=10).pack()
		Button(self.containers[3], text="ds", width=10, height=10).pack()

raiz=Tk() 
Window(raiz) 
raiz.mainloop() 
