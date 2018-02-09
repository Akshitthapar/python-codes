class Abc:
	def show(self):
		print('hi')
class Xyz (Abc):
	def print(self):
		print('welcome')
class Welcome(Xyz):
	def Hello(self,name):
		print('hello',name)

w=Welcome()
w.show()
w.print()
w.Hello('Ratan singh')