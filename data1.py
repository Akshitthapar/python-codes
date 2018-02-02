print('******************welcome to data manager****************')
print('please select from the follwing languages')
print('1.Add entry')
print('2.print all entries')
print('3.exit')
#above code prints options
n=(int)(input('enter your choice:  '))

if n==1:
	print('enter record')
	fopen=('base.txt','w+')
	fwrite=(name)
	name=(input('enter name'))
	print('record created')
	#f.close()
elif n==2:
	fopen=('base.txt')
	print(read())
	f.seek(0)

elif n==3 :
	print('thank you for using data manager program will now exit')
	exit
	
else :
	print('wrong option')