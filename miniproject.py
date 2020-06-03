from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:

	def __init__(self,root):
		self.root = root
		self.root.title("MINI PROJECT PYTHON")
		self.root.geometry("1350x700+0+0")

		title = Label(self.root,text="Student Management System",bd=10,relief = GROOVE,font=("times new roman",40,"bold"),bg="salmon",fg="black")
		title.pack(side=TOP,fill=X)

		self.Roll_No_var = StringVar()
		self.name_var = StringVar()
		self.email_var = StringVar()
		self.gender_var = StringVar()
		self.contact_var = StringVar()
		self.dob_var = StringVar()
		self.search_by = StringVar()
		self.search_txt = StringVar()


		Detail_Frame = Frame(self.root,bd=4,relief=RIDGE,bg="azure")
		Detail_Frame.place(x=3,y=80,width=450,height=570)

		d_title = Label(Detail_Frame, text="ENTER THE DETAILS", bg="tan1" ,fg="black" ,font=("times new roman", 20, "bold"))
		d_title.grid(row=0,columnspan=2,pady=10)

		lbl_roll = Label(Detail_Frame, text="ROLL NO.", bg="rosybrown1", fg="black",font=("times new roman", 15, "bold"))
		lbl_roll.grid(row=1, column=0, pady=10,padx=20,sticky="w")

		txt_Roll = Entry(Detail_Frame,textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"),bd=5,relief=GROOVE)
		txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

		lbl_Name = Label(Detail_Frame, text="NAME", bg="rosybrown1", fg="black",font=("times new roman",15, "bold"))
		lbl_Name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

		txt_Name = Entry(Detail_Frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
		txt_Name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

		lbl_Email = Label(Detail_Frame, text="EMAIL", bg="rosybrown1", fg="black",font=("times new roman", 15, "bold"))
		lbl_Email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

		txt_Email = Entry(Detail_Frame, textvariable=self.email_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
		txt_Email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

		lbl_Gender = Label(Detail_Frame, text="GENDER", bg="rosybrown1", fg="black",font=("times new roman", 15, "bold"))
		lbl_Gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

		combo_Gender = ttk.Combobox(Detail_Frame,textvariable=self.gender_var, font=("times new roman", 15, "bold"))
		combo_Gender['values'] = ("MALE","FEMALE","OTHERS")
		combo_Gender.grid(row=4, column=1, pady=10, padx=20, sticky="w")

		lbl_Contact = Label(Detail_Frame, text="CONTACT", bg="rosybrown1", fg="black",font=("times new roman", 15, "bold"))
		lbl_Contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

		txt_Contact = Entry(Detail_Frame, textvariable=self.contact_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
		txt_Contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

		lbl_Dob = Label(Detail_Frame, text="D.O.B", bg="rosybrown1", fg="black",font=("times new roman",15, "bold"))
		lbl_Dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

		txt_Dob = Entry(Detail_Frame, textvariable=self.dob_var,font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
		txt_Dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

		lbl_Address = Label(Detail_Frame, text="ADDRESS", bg="rosybrown1", fg="black",font=("times new roman", 15, "bold"))
		lbl_Address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

		self.txt_Address = Text(Detail_Frame,width=30, height=4 , font=("times new roman",10,"bold"),bd=5, relief=GROOVE)
		self.txt_Address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

   #*******BUTTON FRAME*******
		btn_Frame = Frame(Detail_Frame,bd=4,relief=RIDGE,bg="salmon")
		btn_Frame.place(x=10,y=500,width=420)

		Addbtn = Button(btn_Frame,text="ADD+",width=9,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
		updatebtn = Button(btn_Frame, text="UPDATE~", width=9,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
		deletebtn = Button(btn_Frame, text="DELETE-", width=9,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
		Clearbtn = Button(btn_Frame, text="CLEAR/", width=9,command=self.clear).grid(row=0, column=3, padx=10, pady=10)

#*******DISPLAY FRAME*****
		Display_Frame=Frame(self.root,bd=4,relief=RIDGE, bg="azure")
		Display_Frame.place(x=480,y=80,width=792,height=570)

		lbl_search = Label(Display_Frame, text="Search By", bg="tan1", fg="black",font=("times new roman", 15, "bold"))
		lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

		combo_search=ttk.Combobox(Display_Frame,textvariable=self.search_by,width=10,font=("times new roman",10,"bold"),state='readonly')
		combo_search['values']=("Roll_no","Name","Contact")
		combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="w")

		txt_Search = Entry(Display_Frame, textvariable=self.search_txt,font=("times new roman", 13, "bold"), bd=5, relief=GROOVE)
		txt_Search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

		searchbtn = Button(Display_Frame, text="SEARCH", width=10,command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
		showallbtn = Button(Display_Frame, text="Show All", width=10,command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

#******TABLE FRAME*****

		Table_Frame = Frame(Display_Frame,bd=4,relief=RIDGE,bg="peachpuff")
		Table_Frame.place(x = 10 , y =70 , width=760,height=480)

		scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
		scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

		self.Student_table = ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
		scroll_x.pack(side=BOTTOM,fill=X)
		scroll_y.pack(side=RIGHT, fill=Y)
		scroll_x.config(command=self.Student_table.xview)
		scroll_y.config(command=self.Student_table.yview)

		self.Student_table.heading("Roll",text="Roll No.")
		self.Student_table.heading("Name", text="Name")
		self.Student_table.heading("Email", text="Email")
		self.Student_table.heading("Gender", text="Gender")
		self.Student_table.heading("Contact", text="Contact")
		self.Student_table.heading("DOB", text="DOB")
		self.Student_table.heading("Address", text="Address")
		self.Student_table['show'] = "headings"
		self.Student_table.column("Roll",width=100)
		self.Student_table.column("Name", width=120)
		self.Student_table.column("Email", width=120)
		self.Student_table.column("Gender", width=120)
		self.Student_table.column("Contact", width=120)
		self.Student_table.column("DOB", width=120)
		self.Student_table.column("Address", width=120)
		self.Student_table.pack(fill=BOTH,expand=1)
		self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
		self.fetch_data()

	def add_student(self):
		if(self.Roll_No_var=="" or self.name_var==""):
			message.showinfo("error","All fields are compulsory")
		con = pymysql.connect(host="localhost",user="root",password="",database="nandu")
		cur = con.cursor()
		cur.execute("insert into contacts values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get('1.0',END)))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()
		messagebox.showinfo("success","Record has been added successfully")

	def fetch_data(self):
		con = pymysql.connect(host="localhost", user="root", password="", database="nandu")
		cur = con.cursor()
		cur.execute("select * from contacts")
		rows = cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
		con.commit()
		con.close()

	def search_data(self):
		con = pymysql.connect(host="localhost", user="root", password="", database="nandu")
		cur = con.cursor()
		cur.execute("select * from contacts where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
		rows = cur.fetchall()
		if len(rows)!=0:
			self.Student_table.delete(*self.Student_table.get_children())
			for row in rows:
				self.Student_table.insert('',END,values=row)
		con.commit()
		con.close()

	def clear(self):
			self.Roll_No_var.set("")
			self.name_var.set("")
			self.email_var.set("")
			self.gender_var.set("")
			self.contact_var.set("")
			self.dob_var.set("")
			self.txt_Address.delete("1.0",END)

	def get_cursor(self,ev):
		cursor_row = self.Student_table.focus()
		contents = self.Student_table.item(cursor_row)
		row = contents['values']
		self.Roll_No_var.set(row[0])
		self.name_var.set(row[1])
		self.email_var.set(row[2])
		self.gender_var.set(row[3])
		self.contact_var.set(row[4])
		self.dob_var.set(row[5])
		self.txt_Address.delete("1.0", END)
		self.txt_Address.insert(END, row[6])

	def update_data(self):
		con = pymysql.connect(host="localhost",user="root",password="",database="nandu")
		cur = con.cursor()
		cur.execute("update contacts set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_Address.get('1.0',END),self.Roll_No_var.get()))
		con.commit()
		self.fetch_data()
		self.clear()
		con.close()
		messagebox.showinfo("success", "Record has been updated successfully")

	def delete_data(self):
		con = pymysql.connect(host="localhost", user="root", password="", database="nandu")
		cur = con.cursor()
		cur.execute("delete from contacts where roll_no=%s",self.Roll_No_var.get())
		con.commit()
		con.close()
		self.fetch_data()
		self.clear()
		messagebox.showinfo("success", "Record has been deleted successfully")


root = Tk()
ob = Student(root)
root.mainloop()

