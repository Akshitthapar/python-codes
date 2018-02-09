class student:
	def __init__(self): #self is used to associate with class
		 self.name='' 
		 self.age=0
	def getinfo(self):
		self.name=input('enter name')
		self.name=(int)(input('enter age'))
	
class Marks(student):
	def getmarks(self):
		print('marks is updated')

m=Marks()
m.getinfo()
m.getmarks()
	
	