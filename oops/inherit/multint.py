print('********multinhertiance*********')

class Student:
	#def __init__(self):
		
	def getinfo(self):
		global name
		global age
		name=input('enter name')
		age=(int)(input('enter age'))

class Marks:
	def getMarks(self):
		global che
		global phy
		global math 
		global per
		phy=(int)(input('enter phy'))
		che=(int)(input('enter che'))
		math=(int)(input('enter maths'))
		per=(phy+che+math)//3
	
class Result(Student,Marks): #using multiple inheritance
	def showResult(self):
		div=''
		if per>=60:
			div='first'
		elif per>=45 and per<60:
			div='second'
		elif per>=33 and div<45:
			div=third
		else:
			div='fail'
		print('name of the student',name)
		print('age of the student',age)
		print('percentage of the student',per)
		print('divison of the student',div)
 	
obj=Result()
obj.getinfo()
obj.getMarks()
obj.showResult()