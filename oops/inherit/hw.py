class Employee:
 
	def credit (self):
		global name
		global des
		global salary
		global n
		x=0
		n=(int)(input('enter how many times u want to enter record'))
		while(x<n):
			name=input('enter name of employee     ')
			des=input('enter designation of employe   ')
			salary=input('enter salary of employee  ')
			fo=open('foo.txt','a+')
		
			fo.write(name)
			fo.write(des)
			fo.write(salary)
			#fo.close()
			x=x+1
		fo.close()

'''class  file:
	def input(self):		
			
		fo=open('foo.txt','a+')
		
		fo.write(name)
		fo.close()'''
	
	
class Output(Employee):
	def info(self):
		print(name,des,salary)

		

m=Output()
m.credit()
#m.input()
m.info()