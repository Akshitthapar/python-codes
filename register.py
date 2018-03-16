from tkinter import *
import tkinter.messagebox as tm
import pymysql

class RegisterFrame(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.label_firstname=Label(self,text="First name :")
		self.label_lastname=Label(self,text="Last name :")

		self.label_username=Label(self,text="User name :")
		self.label_password=Label(self,text="Password :")

		self.entry_firstname=Entry(self)
		self.entry_lastname=Entry(self)

		self.entry_username=Entry(self)
		self.entry_password=Entry(self,show='#')

		self.label_firstname.grid(row=0,sticky=E)
		self.label_lastname.grid(row=1,sticky=E)
		self.label_username.grid(row=2,sticky=E)
		self.label_password.grid(row=3,sticky=E)
		
		self.entry_firstname.grid(row=0,column=1)
		self.entry_lastname.grid(row=1,column=1)

		self.entry_username.grid(row=2,column=1)
		self.entry_password.grid(row=3,column=1)

		self.logbtn=Button(self,text="Register",command=self.register_btn_clicked)
		self.logbtn.grid(row=4)

		self.quit=Button(self,text='Quit',command=root.quit)
		self.quit.grid(row=4,column=1)
		self.pack()		

	def register_btn_clicked(self):
		fname=self.entry_firstname.get()
		lname=self.entry_lastname.get()
		uname=self.entry_username.get()
		passwd=self.entry_password.get()
		con=pymysql.connect(db='mydb',user='root',passwd='asda0074',host='localhost')
		cur=con.cursor()
		cur.execute("insert into empl(fname,lname,uname,passwd) values('%s','%s','%s','%s')"%(fname,lname,uname,passwd))
		con.commit()
		print('Record Saved')

root=Tk()
lf=RegisterFrame(root)
root.mainloop()
		

		
