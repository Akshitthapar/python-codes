print('welcome to all things list')
list=[1,2,3,3,4,4,5,6,7]
print ('defaulist',list)

#to print any value from list 
print(list[8])

#to print before certain elements
print(list[:6])

#to print after certain elements
print(list[:4])

#to add an element into list
list.append(34)
list.append(44)#write multiple times for multiple times adding an element
print(list)

#to remove an elemnt from list
list.pop()
print(list)

pow=[]
for x in range (2,20):
	m=x**2 
	pow.append(m) #this tells add m into list pow and keep doing until for  loop ends
print (pow)
