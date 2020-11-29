from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
import tkinter as tk
#-------------------------------------
#for graph.
import numpy as np
import matplotlib.pyplot as plt
#-------------------------------------
# for temperature.
import socket
import requests
#------------------------------------- 
import bs4
#------------------------------------
from cx_Oracle import *
#f1
def Add():
	root.withdraw()
	adst.deiconify()
#f2
def AddBack():
	adst.withdraw()
	root.deiconify()
#f3
def View():
	stViewData.delete(1.0,END)
	root.withdraw()

	vist.deiconify()

	con = None
	try:
		con = connect("system/abc123")
		cursor = con.cursor()
		sql ="SELECT * FROM student_database ORDER BY rno ASC"	# sql ="select rno,name,marks form student_database order by asc"     #"select asc rno, name,marks from student_database" 
		cursor.execute(sql)
		data = cursor.fetchall()
		msg = ""
		for d in data:
			msg = msg + " rno = " + str(d[0])+ " " + "name = " + str(d[1])+ " " + "marks = " + str(d[2]) + "\n"
		stViewData.insert(INSERT,msg)
		
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ", e)
	
	finally:
		if con is not None:
			con.close()
#f4
def ViewBack():
	vist.withdraw()
	root.deiconify()
#f5
def AddSave():
	con = None
	try:
		con = connect("system/abc123")
		rno = int(entAddRno.get())
		# Validation of Rno:
		if rno > 0:
			pass
		else:
			raise ValueError("Invalid Number")
		
		name = entAddName.get()
		# Validation of Name:
		if len(name) >= 2 and name.isalpha():
			pass
		else:
			raise ValueError("Invalid Name")

		marks = int(entAddMarks.get())
		# Validation of Marks:
		if  marks <= 100 and marks >= 0:
			pass
		else:
			raise ValueError("Invalid Marks")
			#focus de
		
		args = (rno, name,marks)
		
		cursor = con.cursor()
		sql = "insert into student_database values('%d', '%s','%d')"
		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Sahi kiya", str(cursor.rowcount) + "rows inserted")
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ", e)
		con.rollback()
	except ValueError as e:
		messagebox.showerror("Error",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entAddRno.delete(0, END)
		entAddName.delete(0, END)
		entAddMarks.delete(0, END)
		entAddRno.focus()




#f6
def Update():
	root.withdraw()
	upst.deiconify()

#f7
def UpdateBack():
	upst.withdraw()
	root.deiconify()

#f8
def UpdateSave():
	con = None
	try:
		con = connect("system/abc123")
		rno = int(entUpdateRno.get())
		# Validation of Rno:
		if rno > 0:
			pass
		else:
			raise ValueError("Invalid Number")
		
		name = entUpdateName.get()
		# Validation of Name:
		if len(name) >= 2 and name.isalpha():
			pass
		else:
			raise ValueError("Invalid Name")

		marks = int(entUpdateMarks.get())
		# Validation of Marks:
		if  marks <= 100 and marks >= 0:
			pass
		else:
			raise ValueError("Invalid Marks")
		
		args = (marks,name,rno)
		
		cursor = con.cursor()

		sql = "update student_database set  marks = '%d',name = '%s' where rno = '%d' " 

		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Sahi kiya", str(cursor.rowcount) + "rows updated")
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ", e)
	except ValueError as e:
		messagebox.showerror("Error",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entUpdateRno.delete(0, END)
		entUpdateName.delete(0, END)
		entUpdateMarks.delete(0, END)
		entUpdateRno.focus()

#f9
def Delete():
	root.withdraw()
	dest.deiconify()

#f10
def DeleteBack():
	dest.withdraw()
	root.deiconify()

#f11
def DeleteSave():
	con = None
	try:
		con = connect("system/abc123")
		rno = int(entDeleteRno.get())
		# Validation of Rno:
		if rno > 0:
			pass
		else:
			raise ValueError("Invalid Number")
		
		args = (rno)
		
		cursor = con.cursor()

		sql = "delete from student_database where rno = '%d' " 

		cursor.execute(sql % args)
		con.commit()
		messagebox.showinfo("Sahi kiya", str(cursor.rowcount) + "rows deleted")
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ", e)
	except ValueError as e:
		messagebox.showerror("Error",e)
		con.rollback()
	finally:
		if con is not None:
			con.close()
		entDeleteRno.delete(0, END)
		entDeleteRno.focus()
#--------------------------------------------------------------------------------------------------------------------------
#f12
def Graph():
#for storing rno,name,marks dynamically.
	rno = []
	name = []
	marks = []
	
	con = None
	try:
		con = connect("system/abc123")
		cursor = con.cursor()
		sql = "select * from (select * from student_database order by marks desc) where rownum <=3 order by marks";
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data:
			rno.append(d[0])
			name.append(d[1])
			marks.append(d[2])

		x = np.arange(len(name))
		plt.bar(x, marks, width=0.30,label="Student Marks")
		plt.xticks(x, name)
		plt.ylabel('Marks')
		plt.xlabel('Name')
		plt.title('Score')
		plt.show()
		
				
	except DatabaseError as e:
		messagebox.showerror("Galat kiya ", e)
	finally:
		if con is not None:
			con.close()	

#---------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("SMS")
root.geometry("500x500+200+200")
#root.configure(bg='cyan')
root['bg'] = '#49A'

btnAdd = Button(root,bg='black',fg='white', text="Add", font=("arial", 18, 'bold'),
width=10, command=Add)
btnView = Button(root,bg='black',fg='white', text="View",font=("arial", 18, 'bold'),
width=10, command=View)
btnUpdate = Button(root,bg='black',fg='white', text="Update", font=("arial", 18, 'bold'),
width=10, command=Update)
btnDelete = Button(root,bg='black',fg='white', text="Delete", font=("arial", 18, 'bold'),
width=10, command=Delete)
btnGraph = Button(root,bg='black',fg='white', text="Graph", font=("arial", 18, 'bold'),
width=10, command=Graph)


try:
	socket.create_connection(("www.google.com", 80))
	print("You are connected")
	city = "mumbai"
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	api_address = a1 + a2 + a3
	res1 = requests.get(api_address)
	#print(res1)
	data = res1.json()

	main = data['main']
	#print(main)
	temp = main['temp']
	#print("temp= ", temp)

	temp1 = data['main']['temp']
	#print("temp1= ", temp1)
	tempp = "Mumbai Temperature is : " + str(temp1)
except OSError as e:
	print("check network ", e)

lblAddTemp = Label(root,bg='#49A',fg='black', text=tempp,font=("arial",18,'underline bold'))


#-------------------------------------------------------------

msg ,qu = '',''
	
	
res = requests.get("https://www.brainyquote.com/quotes_of_the_day.html")
print(res)
soup = bs4.BeautifulSoup(res.text ,'lxml')

qu = soup.find('img', {"class":"p-qotd"})
#print(qu)

msg = "' " +  qu['alt'] + " '"








lblAddQuote = Label(root,bg='#49A',fg='black', text=msg ,font=("Bahnschrift Light Condensed",10,'underline bold'))

btnAdd.pack(pady=10)
btnView.pack(pady=10)
btnUpdate.pack(pady=10)
btnDelete.pack(pady=10)
btnGraph.pack(pady=10)
lblAddTemp.pack(pady=10)
lblAddQuote.pack(pady=10)



adst = Toplevel(root)
adst.title("Add St.")
adst.geometry("800x800+50+50")
adst.withdraw()
adst['bg'] = '#49A'

lblAddRno = Label(adst, bg='black' ,fg='white',  text="Enter Rno",font=("arial",18,'bold'))
entAddRno = Entry(adst,bg='grey', bd=10, font=("arial", 18, 'bold'))

lblAddName = Label(adst,bg='black' ,fg='white', text="Enter Name",font=("arial",18,'bold'))
entAddName = Entry(adst,bg='grey', bd=10, font=("arial", 18, 'bold'))

lblAddMarks = Label(adst, bg='black' ,fg='white', text="Enter Marks",font=("arial",18,'bold'))
entAddMarks = Entry(adst,bg='grey', bd=10, font=("arial", 18, 'bold'))

btnAddSave = Button(adst, bg='black' ,fg='white', text="Save",font=("arial",18,'bold'),
command=AddSave)
btnAddBack = Button(adst,bg='black' ,fg='white', text="Back",font=("arial",18,'bold'),
command=AddBack)

lblAddRno.pack(pady=10)
entAddRno.pack(pady=10)
lblAddName.pack(pady=10)
entAddName.pack(pady=10)
lblAddMarks.pack(pady=10)
entAddMarks.pack(pady=10)
btnAddSave.pack(pady=10)
btnAddBack.pack(pady=10)

# update saathi

upst = Toplevel(root)
upst.title("Update St.")
upst.geometry("800x800+50+50")
upst.withdraw()
upst['bg'] = '#49A'

lblUpdateRno = Label(upst,bg='black' ,fg='white', text="Enter rno",font=("arial",18,'bold'))
entUpdateRno = Entry(upst, bg='grey',bd=10, font=("arial", 18, 'bold'))

lblUpdateName = Label(upst,bg='black' ,fg='white', text="Enter name",font=("arial",18,'bold'))
entUpdateName = Entry(upst, bg='grey' , bd=10, font=("arial", 18, 'bold'))

lblUpdateMarks = Label(upst,bg='black' ,fg='white', text="Enter marks",font=("arial",18,'bold'))
entUpdateMarks = Entry(upst,bg='grey', bd=10, font=("arial", 18, 'bold'))

btnUpdateSave = Button(upst,bg='black' ,fg='white', text="Save",font=("arial",18,'bold'),
command=UpdateSave)
btnUpdateBack = Button(upst,bg='black' ,fg='white', text="Back",font=("arial",18,'bold'),
command=UpdateBack)

lblUpdateRno.pack(pady=10)
entUpdateRno.pack(pady=10)
lblUpdateName.pack(pady=10)
entUpdateName.pack(pady=10)
lblUpdateMarks.pack(pady=10)
entUpdateMarks.pack(pady=10)
btnUpdateSave.pack(pady=10)
btnUpdateBack.pack(pady=10)
#
 
#Delete saathi

dest = Toplevel(root)
dest.title("Delete St.")
dest.geometry("800x800+50+50")
dest.withdraw()
dest['bg'] = '#49A'

lblDeleteRno = Label(dest,bg='black' ,fg='white', text="Enter rno",font=("arial",18,'bold'))
entDeleteRno = Entry(dest,bg='grey', bd=10, font=("arial", 18, 'bold'))

btnDeleteSave = Button(dest,bg='black' ,fg='white', text="Save",font=("arial",18,'bold'),
command=DeleteSave)
btnDeleteBack = Button(dest,bg='black' ,fg='white', text="Back",font=("arial",18,'bold'),
command=DeleteBack)

lblDeleteRno.pack(pady=10)
entDeleteRno.pack(pady=10)
btnDeleteSave.pack(pady=10)
btnDeleteBack.pack(pady=10)



vist = Toplevel(root)
vist.title("View st.")
vist.geometry("500x400+200+200")
vist.withdraw()
vist['bg'] = '#49A'

stViewData = scrolledtext.ScrolledText(vist, width=60,height=10)
btnViewBack = Button(vist,bg='black' ,fg='white', text="Back",font=("arial", 18,'bold'), command=ViewBack)

stViewData.pack(pady=10)
btnViewBack.pack(pady=10)
root.mainloop()







