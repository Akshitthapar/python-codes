class Myclass:

 
 def addno(self,x,y):
  a=x+y 
  return a

 def sum(self,x=1,y=2):
  b=y/x
  print('output',b)

obj=Myclass()

i=obj.addno(23,34)
print(i,'main')
obj.sum(10,100)
   
	
 
	