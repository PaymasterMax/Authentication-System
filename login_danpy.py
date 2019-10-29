
from tkinter import*
from tkinter import messagebox
import pyautogui,time,os
import sqlite3
macwidth,maclength=pyautogui.size()
#accesslist={"Paymaster":"xcmbyzwvy","Ever":"Ever"}
root=Tk()

root.title("Access your account")
root.geometry("{}x{}+{}+{}".format(int(macwidth*.7),int(maclength*.7),int(.001*macwidth),int(.001*maclength)))
txtVar=StringVar()

#database
#create the database
db=sqlite3.connect("dan_login.db")
cursor=db.cursor()
#create the table
cursor.execute("""CREATE TABLE IF NOT EXISTS login(id INTEGER PRIMARY KEY,name text UNIQUE NOT NULL,password TEXT NOT NULL)""")

class gui:
	def __init__(self,root,db,cursor):
		self.frame=None
		self.cursor=cursor
		self.db=db
		self.root=root
		self.frame1=None
		self.frame2=None
		self.lab1=None
		self.username=None
		self.Password=None
		self.lab2=None
		self.frame3=None
		self.btn=None
		self.text=StringVar()
		self.innerFrame=None
		self.innerlab=None
		#self.accesslist=accesslist
		self.root.resizable(0,0)
		self.packer()

	def respondMouse(self,event):
		if self.username.get()=="" or self.Password.get()=="":
			self.innerlab.configure(background="red")
			self.text.set("One of the text box is blank. Make to fill it and try again.")


			# the notification manager of the gui class

			messagebox.showerror("Notification Manager","One of the text box is blank")

		else:
			uname=self.username.get()
			pas=self.Password.get()

			#check if the user entered values are on the db
			log=self.cursor.execute("""SELECT * FROM login WHERE name = ? AND password =  ?""",(uname,pas))
			self.username.delete(0,END)
			self.Password.delete(0,END)
			print(log.fetchone())
			if (log.fetchone() is not None):
				self.innerlab.configure(background="green")
				self.text.set("**Access Granted.**")
				messagebox.showinfo('logged in',"You have successfully logged in")
				self.username.focus()
			else:
				#if entry not in db
				self.innerlab.configure(background="red")
				self.text.set("**Access Denied. No user with such details found.**")
				messagebox.showinfo('failed',"Login Failed Please try again")
				self.username.focus()

			'''if self.username.get() in self.accesslist:

				try:
					regcomp=self.accesslist[self.username.get()]
				except KeyError:
					self.text.set("**No such user with thise details**")


				else:

					if self.Password.get()==regcomp:
						self.innerlab.configure(background="green")
						self.text.set("**Access Granted.**")

					else:
						self.innerlab.configure(background="red")
						self.text.set("**Access Denied.Wrong Password**")

						# the notification manager of the gui class

						messagebox.showerror("Notification Manager","Access Denied. Wrong Password**")
				#<<Wait ill get to you shortly cool computer?>>

			else:
				self.innerlab.configure(background="red")
				self.text.set("**Access Denied. No user with such details found.**")

				# the notification manager of the gui class

				messagebox.showerror("Notification Manager","Access Denied, No user with such details found**")	'''

	def packer(self):

		self.frame=Frame(self.frame,background="#456",width=f"{macwidth}",height=f"{maclength}",relief="raised",borderwidth=10,padx=100,pady=100,highlightbackground="red")
		self.frame.pack(anchor="center")

		self.parentF=Frame(self.frame,background="#000",relief="raised",borderwidth=.1,padx=5,pady=5,highlightbackground="red")
		self.parentF.pack()

		self.frame_main=Frame(self.parentF,background="#456")
		self.frame_main.pack()
		self.lab_main=Label(self.parentF,text="Enter your login details below",font=("verdana",16,"bold"),background="#000",foreground="#fff",padx=10,pady=10)
		self.lab_main.pack()

		self.frame1=Frame(self.frame,background="#456")
		self.frame1.pack()

		self.frame2=Frame(self.frame,background="#456")
		self.frame2.pack()

		self.lab1=Label(self.frame1,text="Username        \n",font=("elephant",16,"bold"),padx=10,pady=10,border=1,background="#456")
		self.lab1.pack(side="left")

		self.username=Entry(self.frame1,border=10,width=50,font=("old english text mt",16,"bold"),relief="ridge")
		self.username.pack(side="top")
		self.username.focus()

		self.lab2=Label(self.frame2,text="Password        \n",font=("elephant",16,"bold"),padx=10,pady=10,border=1,background="#456")
		self.lab2.pack(side="left")

		self.Password=Entry(self.frame2,border=10,width=50,font=("old english text mt",16,"bold"),show="*",relief="ridge")
		self.Password.pack(side="top")

		self.frame3=Frame(self.frame,background="#000",border=10)
		self.frame3.pack()
		self.btn=Button(self.frame3,text="Login",font=("old english text mt",15),relief="raised",background="#0ff",activebackground="#f00",activeforeground="#fff")
		self.btn.bind("<Button-1>",self.respondMouse)
		self.btn.bind("<Return>",self.respondMouse)
		self.btn.configure(padx=10,pady=10,borderwidth=10,border=10)
		self.btn.pack()

		self.innerFrame=Frame(self.frame)
		self.innerlab=Label(self.innerFrame,textvariable=self.text,foreground="#fff",background="#000",font=("imprint mt shadow",17,"bold","italic","underline"))
		self.innerFrame.pack(side="bottom",anchor="se")
		self.innerlab.pack()

#$$New class for the menu bar of the gui$$
class access_adder():

	def __init__(self,parent_window,main_menu,submenu,cursor,db):
		self.frame=None
		self.text=StringVar()
		self.parent_window=parent_window
		self.main_menu=main_menu

		self.submenu=submenu

		self.Colorsubmenu=Menu(self.main_menu,tearoff=False)

		self.main_menu.add_cascade(label="Add user",menu=self.submenu)

		self.main_menu.add_cascade(label="Change background",menu=self.Colorsubmenu)

		self.new_username=None
		self.new_userpass=None
		self.toplevel=None
		self.adduserLabel=None
		self.adduserEntry=None
		self.adduserLabel2=None
		self.adduserPass=None
		self.adduserButton=None
		self.cursor=cursor
		self.db=db

		self.submenuFun()
		self.change_color()
	#regestration function
	def adduser(self):
		self.toplevel=Toplevel(self.parent_window)
		self.toplevel.geometry("400x400")
		self.toplevel.resizable(0,0)
		self.adduserLabel=Label(self.toplevel,text="Enter the name of the user",font=("verdana",16,"bold"))
		self.adduserLabel.pack()
		self.adduser_new_user=Entry(self.toplevel,background="#456",font=("elephant",14,"bold"))
		self.adduser_new_user.pack()

		self.adduserLabel2=Label(self.toplevel,text="Enter Password",font=("verdana",16,"bold"))
		self.adduserLabel2.pack()
		self.adduserPass=Entry(self.toplevel,background="#456",font=("elephant",14,"bold"),show="$")
		self.adduserPass.pack()

		self.adduserButton=Button(self.toplevel,text="Add",background="cyan",font=("impact",17,"bold"),width=10)
		self.adduserButton.bind("<Button-1>",self.adduserBtnrespond)
		self.adduserButton.pack()

		self.toplevel.mainloop()


	def adduserBtnrespond(self,event):

		self.frame=Frame(self.frame,background="#456",width=f"{x}",height=f"{y}",relief="raised",borderwidth=10,padx=100,pady=100,highlightbackground="red")
		self.frame.pack(anchor="center")
		self.innerFrame=Frame(self.frame)
		self.innerlab=Label(self.innerFrame,textvariable=self.text,foreground="#fff",background="#000",font=("imprint mt shadow",17,"bold","italic","underline"))
		self.innerFrame.pack(side="bottom",anchor="se")
		self.innerlab.pack()
		#check if any of the entry is empty
		if self.adduser_new_user.get()!="" and self.adduserPass.get() !="":
			#check if the username is on the db
			user=self.cursor.execute("""SELECT* FROM login WHERE name = ?""",(self.adduser_new_user.get(),) )
			self.adduser_new_user.delete(0,END)
			self.adduserPass.delete(0,END)
			if (user.fetchone() is not None):
				self.innerlab.configure(background="red")
				self.text.set("**Username Already EXISTS!.**")
				messagebox.showinfo('username used',"Choose another username !")
			else:
				#if not empty insert the data

				self.cursor.execute("""INSERT INTO login (name,password) VALUES(?,?)""",(self.adduser_new_user.get(),self.adduserPass.get()))
				self.new_username=self.adduser_new_user.get()
				self.new_userpass=self.adduserPass.get()
				self.db.commit()
				self.innerlab.configure(background="green")
				self.text.set("**You Have Regestered successfully!.**")
				messagebox.showinfo('success',"Data added successfully")



		else:
			#if any of the entry is empty
			messagebox.showerror("Add user Tab","One or all of the input fields is empty")
		self.adduser_new_user.focus()

	def submenuFun(self):
		self.submenu.add_command(label="New user",command=self.adduser)

	#<<The exadecimal colors to pick from>>
	def change_color(self):
		self.Colorsubmenu.add_command(label="English based colours",command=self.Themecolor)
		self.Colorsubmenu.add_separator()
		self.Colorsubmenu.add_command(label="exadecimal colors",command=self.Themecolor)


	def Themecolor(self):
		self.root.configure(background="red")
		self.toplevel=Toplevel(self.parent_window)
		self.toplevel.mainloop()

#	<<The parent gui is called to pack the common widgets>>
gui(root,cursor,db)

#<<The program starts frin this point to execute. The cllin gobjects are written down in the next line>>
main_menu=Menu(root)
submenu=Menu(main_menu,tearoff=False)
access_adder(root,main_menu,submenu,cursor,db)
root.configure(menu=main_menu)
root.mainloop()
