class Myclass:
	def	__init__(self):
		print('constructor fired')
		self.x=10
		self.y=20
	def add (self):
		k=self.x+self.y
		print(k)
obj=Myclass()
obj.add()