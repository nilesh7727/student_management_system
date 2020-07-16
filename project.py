from tkinter import *
from tkinter import scrolledtext 
from cx_Oracle import *
from tkinter import messagebox
root = Tk()
root.title("Student Management Record")
root.geometry("550x450+200+200")

def only_numeric_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isdigit() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False

def only_text_input(P):
    # checks if entry's value is an integer or empty and returns an appropriate boolean
    if P.isalpha() or P == "":  # if a digit was entered or nothing was entered
        return True
    return False


def fun1():
	import socket
	import requests

	try:
		socket.create_connection(("www.google.com",80))
		#print("u r connected")
		res1=requests.get("https://ipinfo.io")
		data1=res1.json()
		city=data1['city']
		return(city)
		
	except OSError as e:
		return ("check network")
def fun2():
	import socket
	import requests

	try:
		socket.create_connection(("www.google.com",80))
		#print("u r connected")
		res1=requests.get("https://ipinfo.io")
		data1=res1.json()
		city=data1['city']
		#print("City Name",city)
		a1="http://api.openweathermap.org/data/2.5/weather?units=metric"
		a2= "&q=" + city
		a3="&appid=c6e315d09197cec231495138183954bd"
		api_address=a1+a2+a3
		res=requests.get(api_address)
	
		data=res.json()
		
		temp=data['main']
		
		temp1=temp['temp']
		return(temp1)
	except OSError as e:
		return ("check network")
def fun3():
	import socket
	import requests
	import bs4
	import datetime
	try:
		socket.create_connection(("www.google.com",80))
		res=requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
		soup=bs4.BeautifulSoup(res.text,'lxml')
		quote=soup.find('img',{"class":"p-qotd"})
		#print(quote)
		msg=quote['alt']
		return(msg)
	except OSError as e:
		return("check network ")
def f1():
	root.withdraw()
	adds.deiconify()


def f2():
	adds.withdraw()
	root.deiconify()

def f3():
	
	root.withdraw()
	visit.deiconify()
	stdata.delete(1.0,END)
	con = None
	
	try:
		con =connect('system/abc123')
		cursor = con.cursor()
		sql = "select * from SMS "
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg +"Rno = "+str(d[0])+" Name = "+str(d[1])+" Marks = "+str(d[2]) + "\n"
		stdata.insert(INSERT, msg)		
		
	
	except DatabaseError as e :

		print("issue",e)
	

	finally :
		if con is not None :
			con.close()

	


def f4():
	visit.withdraw()
	root.deiconify()

def f5():

	con = None

	try:
		con = connect('system/abc123')
		rno = int(entAddRno.get())
		name = entAddName.get()
		marks = int(entAddMarks.get())
		cursor = con.cursor()
		sql = "insert into SMS values('%d','%s','%d' )"
		args=(rno, name ,marks)
		cursor.execute(sql%args)
		con.commit()
		messagebox.showinfo("success", "record inserted ")
		entAddRno.delete(0,END)
		entAddName.delete(0, END)
		entAddMarks.delete(0 , END)
		entAddRno.focus()
		
	except DatabaseError as e :	
		con.rollback()
		messagebox.showerror("issue",e)
	except ValueError as a:
		messagebox.showerror("Error","Enter only Text as input")
	

	finally :
		if con is not None :
			con.close()

def f6():
	root.withdraw()
	updt.deiconify()
	
def f10():
	con = None

	try:
		con = connect('system/abc123')
		rno= int(entupdRno.get())
		name = entupdName.get()
		marks = int(entupdMarks.get())
		cursor = con.cursor()
		sql = "update SMS set name = '%s', marks= '%d'  where rno = '%d' "
		args =(name, marks, rno, name)
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + "  record updated"
		messagebox.showinfo("updated", msg)
		entupdRno.delete(0,END)
		entupdName.delete(0,END)
		entupdMarks.delete(0,END)
		entupdRno.focus()
	except DatabaseError as e :
		con.rollback()
		messagebox.showerror("issue",e)
	except ValueError as a:
		messagebox.showerror("Error", "Enter only Text as input")
	

	finally :
		if con is not None :
			con.close()

	

def f7():
	root.withdraw()
	delt.deiconify()
def f8():
	con = None
	try :

		con = connect('system/abc123')
		rno = int(entdelRno.get())
		cursor = con.cursor()
		sql = "delete from SMS where rno = '%d' "
		args =(rno )
		cursor.execute(sql % args)
		con.commit()
		msg = str(cursor.rowcount) + "record deleted"
		messagebox.showinfo("deleted", msg)
		entdelRno.delete(0,END)
		entdelRno.focus()
	except DatabaseError as e :
		con.rollback()
		messagebox.showerror("issue",e)
	

	finally :
		if con is not None :
			con.close()

	
def f9():
	updt.withdraw()
	root.deiconify()

def f11():
	delt.withdraw()
	root.deiconify()


btnAdd= Button(root, text="Add", width=10, command=f1,font=('arial' , 16 ,'bold italic '))
btnView=Button(root, text="View", width=10, command=f3,font=('arial' , 16 ,'bold italic '))
btnUpdate=Button(root, text="Update", width=10, command=f6,font=('arial' , 16 ,'bold italic '))
btnDelete=Button(root, text="Delete", width=10, command=f7,font=('arial' , 16 ,'bold italic '))
btnGraph=Button(root, text="Graph", width=10,font=('arial' , 16 ,'bold italic '))
lbcity=Label(root, text= "City:",font=('arial'))
lbcval=Label(root, text=fun1())
lbtemp=Label(root, text="Temperature =",font=('arial' ))
lbtval=Label(root, text=fun2())
lbqot=Label(root, text="QOTD:",font=('arial'))
lbqval=Label(root, text=fun3())

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
lbcity.place(y=300)
lbcval.place(y=305,x=47)

lbtval.place(y=305,x=491)
lbtemp.place(y=300,x=349)
lbqot.place(y=350)
lbqval.place(y=355,x=64)


adds = Toplevel(root)
adds.title("Add S ")
adds.geometry("550x550+200+200")

lblAddRno = Label(adds , text="Enter roll no", font=('arial' , 16 ,'bold italic '))
entAddRno = Entry(adds , bd = 10 ,font=('arial' , 16 ,'bold italic '))


lblAddName = Label(adds , text="Enter Name", font=('arial' , 16 ,'bold italic '))
entAddName= Entry(adds , bd = 10 ,font=('arial' , 16 ,'bold italic '))


lblAddMarks = Label(adds , text="Enter Marks", font=('arial' , 16 ,'bold italic '))
entAddMarks= Entry(adds , bd = 10 ,font=('arial' , 16 ,'bold italic '))

btnAddSave = Button(adds , text = "Save" ,font=('arial' , 16 ,'bold italic '),command=f5 )

btnAddBack = Button(adds , text = "Back" ,font=('arial' , 16 ,'bold italic ') ,command = f2 )


lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
callback = adds.register(only_numeric_input)  # registers a Tcl to Python callback
entAddRno.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

lblAddName.pack(pady=10)
entAddName.pack(pady=10)
callback = adds.register(only_text_input)  # registers a Tcl to Python callback
entAddName.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

lblAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
callback = adds.register(only_numeric_input)  # registers a Tcl to Python callback
entAddMarks.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

adds.withdraw()


visit = Toplevel(root)
visit.title("View S")
visit.geometry("550x550+200+200")

stdata = scrolledtext.ScrolledText(visit , width =40 , height =25)
btnViewBack = Button(visit , text = "Back" ,font=('arial' , 16 ,'bold italic ') ,command = f4)

stdata.pack(pady=10)
btnViewBack.pack(pady=10)
visit.withdraw()


updt = Toplevel(root)
updt.title("Update S")
updt.geometry("500x500+300+300")

lblupdRno = Label(updt, text="Enter roll no", font=('arial' , 16 ,'bold italic '))
entupdRno = Entry(updt , bd = 10 ,font=('arial' , 16 ,'bold italic '))

lblupdName = Label(updt , text="Enter New Name", font=('arial' , 16 ,'bold italic '))
entupdName= Entry(updt , bd = 10 ,font=('arial' , 16 ,'bold italic '))

lblupdMarks = Label(updt, text="Enter New Marks", font=('arial' , 16 ,'bold italic '))
entupdMarks= Entry(updt , bd = 10 ,font=('arial' , 16 ,'bold italic '))

btnupdSave = Button(updt , text = "Save" ,font=('arial' , 16 ,'bold italic ') , command = f10 )

btnupdBack = Button(updt , text = "Back" ,font=('arial' , 16 ,'bold italic ') ,command = f9 )


lblupdRno.pack(pady=10)
entupdRno.pack(pady=10)
callback = updt.register(only_numeric_input)  # registers a Tcl to Python callback
entupdRno.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

lblupdName.pack(pady=10)
entupdName.pack(pady=10)
callback = updt.register(only_text_input)  # registers a Tcl to Python callback
entupdName.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation


lblupdMarks.pack(pady=10)
entupdMarks.pack(pady=10)
callback = updt.register(only_numeric_input)  # registers a Tcl to Python callback
entupdMarks.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

btnupdSave.pack(pady=10)
btnupdBack.pack(pady=10)

updt.withdraw()

delt = Toplevel(root)
delt.title("Delete S")
delt.geometry("550x550+200+200")

lbldelRno = Label(delt , text="Enter roll no to delete", font=('arial' , 16 ,'bold italic '))
entdelRno = Entry(delt , bd = 10 ,font=('arial' , 16 ,'bold italic '))

btndelSave = Button(delt , text = "Save" ,font=('arial' , 16 ,'bold italic '),command = f8 )

btndelBack = Button(delt , text = "Back" ,font=('arial' , 16 ,'bold italic ') ,command = f11 )


lbldelRno.pack(pady=10)
entdelRno.pack(pady=10)
callback = delt.register(only_numeric_input)  # registers a Tcl to Python callback
entdelRno.configure(validate="key", validatecommand=(callback, "%P"))  # enables validation

btndelSave.pack(pady=10)
btndelBack.pack(pady=10)

delt.withdraw()

root.mainloop()