class Instrumento:
	def __init__(self, precio):
		self.precio = precio

	def tocar(self):
		print("estamos tocando musica")


	def romper(self):
		print("esto lo pagas tu")
		print('son', self.precio, "$$")

class Bateria(Instrumento):
	pass
class Guitarra(Instrumento):
	def __init__(self, tipo):
		self.tipo = tipo
		Instrumento.__init__(self,precio)



 
 		
ins = Instrumento(23)
ins.tocar()
ins.romper()
print('+++++++++++')


bat = Bateria('joderrrrrrr')
bat.tocar()
bat.romper()