class ClasseCalculadora():

	def multiplicacao(self, x, y):
		return x * y

	def divisao(self,x,y):
		return x/y

	def subtracao(self,x,y):
		return x - y


if __name__=='__main__':
	calculadora = ClasseCalculadora()

	print calculadora.divisao(10,2)
	print calculadora.multiplicacao(1,2)
	print calculadora.subtracao(3,1)
