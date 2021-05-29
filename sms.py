from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql 
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1300x700")
        

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="crimson",fg="white")
        title.pack(side=TOP, fill=X)

#All Variable
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.address_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

#Manage Frame
        ManageFrame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        ManageFrame.place(x=20,y=100,width=450,height=580)

        m_title=Label(ManageFrame,text="Manage Students",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(ManageFrame,text="Roll Number",font=("times new roman",15,"bold"),bg="crimson",fg="white")
        lbl_roll.grid(row=1,column=0,padx=20,pady=10,sticky="w")

        txt_roll=Entry(ManageFrame,textvariable=self.roll_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,padx=20,pady=10,sticky="w")

        lbl_name=Label(ManageFrame,text="Name",font=("times new roman",15,"bold"),bg="crimson",fg="white")
        lbl_name.grid(row=2,column=0,padx=20,pady=10,sticky="w")

        txt_name=Entry(ManageFrame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,padx=20,pady=10,sticky="w")

        lbl_email=Label(ManageFrame,text="Email",font=("times new roman",15,"bold"),bg="crimson",fg="white")
        lbl_email.grid(row=3,column=0,padx=20,pady=10,sticky="w")

        txt_email=Entry(ManageFrame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,padx=20,pady=10,sticky="w")

        lbl_gender=Label(ManageFrame,text="Gender",font=("times new roman",15,"bold"),bg="crimson",fg="white")
        lbl_gender.grid(row=4,column=0,padx=20,pady=10,sticky="w")

        combo_gender=ttk.Combobox(ManageFrame,textvariable=self.gender_var,font=("times new roman",14,"bold"),state="readonly")
        combo_gender['values']=("Male","Female","Others")
        combo_gender.grid(row=4,column=1,padx=20,pady=10,sticky="w")

        lbl_contact=Label(ManageFrame,text="Contact",font=("times new roman",15,"bold"),bg="crimson",fg="white")
        lbl_contact.grid(row=5,column=0,padx=20,pady=10,sticky="w")

        txt_contact=Entry(ManageFrame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,padx=20,pady=10,sticky="w")

        lbl_dob=Label(ManageFrame,text="D.O.B",font=("times new roman",15,"bold"),bg="crimson",fg="white")
        lbl_dob.grid(row=6,column=0,padx=20,pady=10,sticky="w")

        txt_dob=Entry(ManageFrame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,padx=20,pady=10,sticky="w")

        lbl_address=Label(ManageFrame,text="Address",font=("times new roman",15,"bold"),bg="crimson",fg="white")
        lbl_address.grid(row=7,column=0,padx=20,pady=10,sticky="w")

        self.txt_address=Text(ManageFrame,width=30,height=4,font=("",10,"bold"))
        self.txt_address.grid(row=7,column=1,padx=20,pady=10,sticky="w")

        #ButtonFrame
        btnFrame=Frame(ManageFrame,bd=4,relief=RIDGE,bg="crimson")
        btnFrame.place(x=15,y=500,width=410)

        Addbtn=Button(btnFrame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btnFrame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btnFrame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btnFrame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)


#Detail Frame
        DetailFrame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        DetailFrame.place(x=480,y=100,width=800,height=580)

        lblSearch=Label(DetailFrame,text="Search By",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        lblSearch.grid(row=0,column=0,padx=20,pady=10,sticky="w")

        combo_search=ttk.Combobox(DetailFrame,textvariable=self.search_by,width=10,font=("times new roman",16,"bold"),state="readonly")
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10,sticky="w")

        txt_search=Entry(DetailFrame,width=20,textvariable=self.search_txt,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,padx=20,pady=10,sticky="w")

        Searchbtn=Button(DetailFrame,text="Search",command=self.search_data,width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showAllbtn=Button(DetailFrame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)

#Table Frame
        TableFrame=Frame(DetailFrame,bd=4,relief=RIDGE,bg="crimson")
        TableFrame.place(x=10,y=70,width=770,height=485)

        scroll_x=Scrollbar(TableFrame,orient=HORIZONTAL)
        scroll_y=Scrollbar(TableFrame,orient=VERTICAL)
        self.StudentTable=ttk.Treeview(TableFrame,columns=("Roll","Name","Email","Gender","Contact","D.O.B","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)
        self.StudentTable.heading("Roll",text="Roll No.")
        self.StudentTable.heading("Name",text="Name")
        self.StudentTable.heading("Email",text="Email")
        self.StudentTable.heading("Gender",text="Gender")
        self.StudentTable.heading("Contact",text="Contact")
        self.StudentTable.heading("D.O.B",text="D.O.B")
        self.StudentTable.heading("Address",text="Address")
        self.StudentTable['show']='headings'
        self.StudentTable.column("Roll",width=80)
        self.StudentTable.column("Name",width=140)
        self.StudentTable.column("Email",width=140)
        self.StudentTable.column("Gender",width=80)
        self.StudentTable.column("Contact",width=100)
        self.StudentTable.column("D.O.B",width=90)
        self.StudentTable.column("Address",width=140)
        self.StudentTable.pack(fill=BOTH,expand=1)
        self.StudentTable.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.roll_no_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="" or self.txt_address.get("1.0",END)=="":
                messagebox.showerror("Error","All fields are required!!!")
        else:
                con=pymysql.connect(host="localhost",user="root",password="",database="stm")
                cur=con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                                self.name_var.get(),
                                                                                self.email_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.contact_var.get(),
                                                                                self.dob_var.get(),
                                                                                self.txt_address.get("1.0",END)
                                                                                ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for row in rows:
                        self.StudentTable.insert('',END,values=row)
                con.commit()
        con.close()

    def clear(self):
        self.roll_no_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.StudentTable.focus()
        contents=self.StudentTable.item(cursor_row)
        row=contents['values']
        self.roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("update students set Name=%s,Email=%s,Gender=%s,Contact=%s,Dob=%s,Address=%s where Roll_No=%s",
                                                                        (self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_address.get("1.0",END),
                                                                         self.roll_no_var.get()
                                                                        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()
        cur.execute("delete from students where Roll_No=%s",self.roll_no_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="stm")
        cur=con.cursor()

        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for row in rows:
                        self.StudentTable.insert('',END,values=row)
                con.commit()
        con.close()


root=Tk()
ob=Student(root)
root.mainloop()