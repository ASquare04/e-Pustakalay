import tkinter as tk
from tkinter import messagebox, ttk
from tkinter import *
from datetime import date
from datetime import timedelta
import mysql.connector as con

#All Required Packages Are Imported

# db1 = con.connect(host = 'localhost', user = 'root', password = 'admin')
# cursor = db1.cursor()
# cursor.execute("Create Database epustakalay")

#--------------DATABASE "EPUSTAKALAY CREATED" 

db1=con.connect(host = 'localhost', user = 'root', password = 'admin', database = 'epustakalay')
cursor = db1.cursor()

#----------CONNECT WITH THE DATABASE EPUSTAKALAY

#str = "Create Table Books(B_Id Varchar(4) , B_Name Varchar(30) , B_Author Varchar(30) , B_Category Varchar (30) , B_Quantity Int(5), B_Price Float(5,2))"
#cursor.execute(str)

# str = "Create Table Issue( Course_Id Int(4), B_Id Varchar(4), Student_Name Varchar(30), Issue_Date Varchar(30), Return_Date Varchar(30))"
# cursor.execute(str)

# str1 = "Create Table Book_Return( Course_Id Int(4), B_Id Varchar(4), Student_Name Varchar(30), Return_Date Varchar(30))"
# cursor.execute(str1)

#---------SQL QUERIES TO CREATE REQUIRED TABLES IN DATABASE 
#----------------------CAN BE EASILY DONE THROUGH ACCESSING THE MySQL Cmd Client

u_id,u_name,u_author,u_category,u_qnt,u_mrp=None,None,None,None,None,None
v_scourse,v_id,v_sname,v_date,v_rett,v_fine,v_iss=None,None,None,None,None,None,None

#------Major Variables Decalared Globally

def A():

    id = u_id.get()
    name = u_name.get()
    author = u_author.get()
    category = u_category.get()
    quantity = u_qnt.get()
    price = u_mrp.get()

    if(id=="" or name=="" or author=="" or category=="" or quantity=="" or price==""):
        messagebox.showwarning("Mandatory Field*","All Fields Are Required")
    else:            
        sql = "Insert Into Books Values ('{}','{}','{}','{}',{},{}) ".format(id,name,author,category,quantity,price)
        cursor.execute(sql)
        db1.commit()

        u_id.delete(0, 'end')
        u_name.delete(0, 'end')
        u_author.delete(0, 'end')
        u_category.delete(0, 'end')
        u_qnt.delete(0, 'end')
        u_mrp.delete(0, 'end')
        messagebox.showinfo("Status","Added Successfully")

def AddBooks():

    panel.withdraw()

    root = Tk()
    root.geometry("700x450+350+150")
    root.resizable(False,False)
    root.title("Adding Books")
    root.configure(bg = "azure")

    Label(root, text ="ADDING NEW BOOKS", font= "ComicSansms 12 bold",pady=5,bg = "azure").pack(side=TOP)

    id = Label(root, text = 'Enter The Book ID :',bg = "azure")
    id.place(x=140,y=50)

    global u_id

    u_id = Entry(root,borderwidth=3,relief=SUNKEN)
    u_id.place(x=420,y=50,)

    name = Label(root, text = 'Enter The Book Name :',bg = "azure")
    name.place(x=140,y=100)

    global u_name

    u_name = Entry(root,borderwidth=3,relief=SUNKEN)
    u_name.place(x=420,y=100)

    author = Label(root, text = 'Enter The Book Author :',bg = "azure")
    author.place(x=140,y=150)

    global u_author

    u_author = Entry(root,borderwidth=3,relief=SUNKEN)
    u_author.place(x=420,y=150)

    category = Label(root, text = 'Enter The Book Category :',bg = "azure")
    category.place(x=140,y=200)

    global u_category

    u_category = Entry(root,borderwidth=3,relief=SUNKEN)
    u_category.place(x=420,y=200)

    qnt = Label(root, text = 'Enter The Book Quantity :',bg = "azure")
    qnt.place(x=140,y=250)

    global u_qnt

    u_qnt = Entry(root,borderwidth=3,relief=SUNKEN)
    u_qnt.place(x=420,y=250)

    mrp = Label(root, text = 'Enter The Book Price :',bg = "azure")
    mrp.place(x=140,y=300)

    global u_mrp

    u_mrp = Entry(root,borderwidth=3,relief=SUNKEN)
    u_mrp.place(x=420,y=300)

    add = Button(root, text = "ADD Record",width = 14, command=A, bg = "green", fg = "white", borderwidth=3)
    add.place(x=220,y=360)

    ex = Button(root,text = "Exit OUT",width = 14, command=lambda:[root.destroy(), panel.deiconify()], bg = "red", fg = "white" , borderwidth=3)
    ex.place(x=380,y=360)

    root.mainloop()

def D():
    
    del_id = d_id.get()

    if(del_id==""):
        messagebox.showwarning("Mandatory Field*","Book ID Required")
    else:
        sel = "Select B_Id From Books"
        cursor = db1.cursor()
        cursor.execute(sel)
        display = cursor.fetchall()

        for i in display:
            if del_id==i[0]:
                chk = messagebox.askquestion("Confirm","Do You Really Want To Delete")
                if chk=="yes":
                        delt = "Delete From Books Where B_Id = %s"
                        data = (del_id,)
                        cursor = db1.cursor()
                        cursor.execute(delt,data)
                        db1.commit()
                        messagebox.showinfo("Status","Deleted Successfully")
                        d_id.delete(0, 'end')
                else:
                        d_id.delete(0,'end')
            else:
                messagebox.showerror("Error","No Such Record")
                d_id.delete(0,'end')

def DeleteBooks():

    panel.withdraw()

    root = Tk()
    root.geometry("550x250+400+250")
    root.resizable(False,False)
    root.configure(bg = "azure")
    root.title("Delete Books")

    Label(root, text ="DELETION OF  RECORD", font= "ComicSansms 12 bold",pady=5,bg = "azure").pack(side=TOP)

    id = Label(root, text = 'Enter The Book ID :',bg = "azure")
    id.place(x=100,y=60)

    global d_id

    d_id = Entry(root,borderwidth=3,relief=SUNKEN)
    d_id.place(x=280,y=60)

    add = Button(root, text = "DELETE Record",width = 14, command=D, bg = "orange", fg = "white" , borderwidth=3,)
    add.place(x=160,y=125)

    ex = Button(root,text = "Exit OUT",width = 14, command=lambda:[root.destroy(), panel.deiconify()], bg = "red", fg = "white" , borderwidth=3)
    ex.place(x=310,y=125)

    root.mainloop()


def UpdateBooks(id,u):
    
    sel = "Select B_Quantity From Books Where B_Id = %s"
    data =(id,)
    cursor = db1.cursor()
    cursor.execute(sel,data)
    result = cursor.fetchone()
    update = result[0]+u
    sql = "Update Books Set B_Quantity = %s where B_Id =%s"
    value =(update,id)
    cursor.execute(sql,value)
    db1.commit()


def AvailBooks():

    panel.withdraw()

    root=tk.Tk()
    root.geometry("800x295+270+200")
    root.resizable(False,False)
    root.configure(bg = "azure")

    root.title("Display Books")
    Label(root, text ="AVAILABLE BOOKS", font= "ComicSansms 12 bold",pady=7,bg = "azure").pack(side=TOP)
    tree = ttk.Treeview(root)

    ex = Button(root,text = "CLOSE",width = 14,command=lambda:[root.destroy(), panel.deiconify()], bg = "red", fg = "white" , borderwidth=3)
    ex.place(x=350,y=258)

    st = ttk.Style(root)
    st.theme_use("classic")

    st.configure("Treeview.Heading", foreground = 'cyan', background = 'black')

    tree["columns"]=("B_Id","B_Name","B_Author","B_Category","B_Quantity","B_Price")

    tree.heading("#0", text ="", anchor=tk.CENTER)
    tree.heading("B_Id",text = "B_Id",anchor=tk.CENTER)
    tree.heading("B_Name",text = "B_Name",anchor=tk.CENTER)
    tree.heading("B_Author",text = "B_Author",anchor=tk.CENTER)
    tree.heading("B_Category",text ="B_Category",anchor=tk.CENTER)
    tree.heading("B_Quantity",text = "B_Quantity",anchor=tk.CENTER)
    tree.heading("B_Price", text = "B_Price",anchor=tk.CENTER)

    tree.column("#0", width=0, stretch=NO)
    tree.column("B_Id",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("B_Name",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("B_Author",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("B_Category",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("B_Quantity",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("B_Price",minwidth=0,width=100,anchor=tk.CENTER)

    index=0
    iid =0

    sel = "Select * From Books Where B_Quantity>=0"
    cursor = db1.cursor()
    cursor.execute(sel)
    display = cursor.fetchall()

    for i in display:
        tree.insert("",index,iid, value=i)
        index = iid=index+1

    scr = ttk.Scrollbar(root,orient="vertical")
    scr.configure(command=tree.yview)
    tree.configure(yscrollcommand=scr.set)
    scr.pack(fill=BOTH,side=RIGHT)

    tree.pack()
    root.mainloop()

def Clr_Txt():
    s_aid.delete(0, END)
    s_name.delete(0, END)
    s_course.delete(0,END)


def Clr_Credentials():
    admin_pass.delete(0, END)
    admin_id.delete(0, END) 
                
def Verify():

    v_sid = s_aid.get()
    v_name = s_name.get()
    v_course = s_course.get()

    iss_date = date.today()
    iss_dd  = iss_date
    ret_dd = iss_dd + timedelta(days=10)

    if(v_sid=="" or v_name=="" or v_course==""):
        messagebox.showwarning("Mandatory Field*","All Fields Are Required")
    else:    
        sql = "Insert Into Issue Values ('{}','{}','{}','{}','{}')".format(v_course,v_sid,v_name,iss_dd,ret_dd)
        cursor.execute(sql)
        db1.commit()
        updated_id = v_sid
        UpdateBooks(updated_id,-1)
        Clr_Txt()
        messagebox.showinfo("Status","Book Is Successfully Issued")
        messagebox.showinfo("Validity","Return Within 10 Days")

def Iss():

    global iss_id
    iss_id = i_id.get()
   
    if(iss_id==""):
        messagebox.showwarning("Mandatory Field*","Book ID Required")
    else:
        sel = "Select B_Id From Books Where B_Quantity>0"
        cursor = db1.cursor()
        cursor.execute(sel)
        display = cursor.fetchmany(15)

        for i in display:
            if iss_id==i[0]:
                messagebox.showinfo("Status","Book Is Available")
                chk = messagebox.askquestion("Confirm","Do You Really Want To Issue")
                if chk=="yes":
                    i_id.delete(0,'end')
                    
                    wd = Tk()
                    wd.geometry("550x250+400+250")
                    wd.resizable(False,False)
                    wd.title("Add Details")
                    wd.configure(bg = "azure")
                    Label(wd, text ="FILL THE DETAILS", font= "ComicSansms 12 bold",pady=7,bg = "azure").pack(side=TOP)
                    name = Label(wd, text="Enter Your Name",bg = "azure")
                    name.place(x=120,y=60)
                    
                    global s_name

                    s_name = Entry(wd,borderwidth=3,relief=SUNKEN)
                    s_name.place(x=350, y=60)

                    course = Label(wd, text="Enter Your Course ID",bg = "azure")
                    course.place(x=120,y=100)

                    global s_course

                    s_course = Entry(wd,borderwidth=3,relief=SUNKEN)
                    s_course.place(x=350, y=100)

                    aid = Label(wd, text="Enter Book ID Again",bg = "azure")
                    aid.place(x=120,y=140)

                    global s_aid

                    s_aid= Entry(wd,borderwidth=3,relief=SUNKEN)
                    s_aid.place(x=350,y=140)

                    submit = Button(wd, text = "Issue Now" , command=Verify, bg  = "blue", fg = "white" , borderwidth =3)
                    submit.place(x=140,y=185)

                    ex = Button(wd, text = "Exit OUT", command=wd.destroy, bg = "red", fg = "white" , borderwidth=3)
                    ex.place(x=380,y=185)
        
                else:
                    i_id.delete(0,'end')
            else:
                messagebox.showerror("Error","Book Is Not Available")
                i_id.delete(0,'end')


def IssueBooks():

    panel.withdraw()

    root = Tk()
    root.geometry("550x250+400+250")
    root.resizable(False,False)
    root.title("Issue Books")
    root.configure(bg = "azure")
    Label(root, text ="ISSUE A BOOK", font= "ComicSansms 12 bold",pady=7,bg = "azure").pack(side=TOP)

    id = Label(root, text = 'Enter The Book ID :',bg = "azure")
    id.place(x=100,y=60)

    global i_id

    i_id = Entry(root,borderwidth=3,relief=SUNKEN)
    i_id.place(x=280,y=60)

    iss = Button(root, text = "Search ID",width = 14,command=Iss, bg = "blue", fg = "white" , borderwidth=3,)
    iss.place(x=120,y=120)

    ex = Button(root,text = "Exit OUT",width = 14, command=lambda:[root.destroy(), panel.deiconify()], bg = "red", fg = "white" , borderwidth=3)
    ex.place(x=320,y=120)

    root.mainloop()

def Ret():

    global crs_id
    crs_id = c_id.get()

    if(crs_id==""):
        messagebox.showwarning("Mandatory Field*","Course ID Required")
    else:
        qry = "Select * From Issue"
        cursor = db1.cursor()
        cursor.execute(qry)
        show = cursor.fetchall()
        
        for i in show:
            if crs_id==i[0]: 
                messagebox.showinfo("Pending","Book Is Issued On This ID")
                response = messagebox.askquestion("Return","Do You Want To Return")
                if response =="yes":
                    damage = messagebox.askquestion("Damage","Is There Any Damage To Book")

                    v_scourse=i[0]
                    v_id=i[1]
                    v_sname=i[2]
                    v_iss=i[3]
                    v_rett=i[4]
                    v_date = date.today()


                    sql = "Insert Into Book_Return Values ('{}','{}','{}','{}')".format(v_scourse,v_id,v_sname,v_date)
                    cursor.execute(sql)
                    db1.commit()
                    UpdateBooks(v_id,1)

                    sel = "Delete From Issue Where Course_Id ={}".format(v_scourse)
                    cursor = db1.cursor()
                    cursor.execute(sel)
                    db1.commit()

                    win = Tk()
                    win.geometry("550x340+400+250")
                    win.resizable(False,False)
                    win.title('Details')
                    win.configure(bg = "azure")

                    Label(win, text ="RECIEPT TO BORROWER", font= "ComicSansms 12 bold",pady=7,bg = "azure").pack(side=TOP)

                    Label(win, text="Course ID :",bg = "azure").place(x=100,y=60)
                    a=Entry(win,borderwidth=3,relief=SUNKEN)
                    a.place(x=280,y=60)
                    a.insert(END, v_scourse)
                    a.configure(state='disabled')

                    Label(win, text="Issued Book :",bg = "azure").place(x=100,y=100)
                    b=Entry(win,borderwidth=3,relief=SUNKEN)
                    b.place(x=280,y=100)
                    b.insert(END, v_id )
                    b.configure(state='disabled')

                    Label(win, text="Student Name :",bg = "azure").place(x=100,y=140)
                    c=Entry(win,borderwidth=3,relief=SUNKEN)
                    c.place(x=280,y=140)
                    c.insert(END, v_sname )
                    c.configure(state='disabled')

                    Label(win, text="Date Of Issue :",bg = "azure").place(x=100,y=180)
                    d=Entry(win,borderwidth=3,relief=SUNKEN)
                    d.place(x=280,y=180)
                    d.insert(END, v_iss )
                    d.configure(state='disabled')

                    Label(win, text="To Return By :",bg = "azure").place(x=100,y=220)
                    e=Entry(win,borderwidth=3,relief=SUNKEN)
                    e.place(x=280,y=220)
                    e.insert(END, v_rett)
                    e.configure(state='disabled')

                    Label(win, text="Date Of Return :",bg = "azure").place(x=100,y=260)
                    f=Entry(win,borderwidth=3,relief=SUNKEN)
                    f.place(x=280,y=260)
                    f.insert(END, v_date)
                    f.configure(state='disabled')

                    if damage=="yes":
                        Label(win, text="Fine Imposed :",bg = "azure").place(x=100,y=300)
                        g=Entry(win,borderwidth=3,relief=SUNKEN)
                        g.place(x=280,y=300)
                        g.insert(END, "500")
                        g.configure(state='disabled')
                    else:
                        c_id.delete(0,'end')
            else:
                c_id.delete(0,'end')
                messagebox.showinfo("Clear","No Book Is Issued To You")
                     
def ReturnBooks():

    panel.withdraw()

    root = Tk()
    root.geometry("550x250+400+250")
    root.resizable(False,False)
    root.title("Return Books")
    root.configure(bg = "azure")
    Label(root, text ="RETURN A BOOK", font= "ComicSansms 12 bold",pady=7,bg = "azure").pack(side=TOP)

    id = Label(root, text = 'Enter Your Course ID :',bg = "azure")
    id.place(x=100,y=60)

    global c_id

    c_id = Entry(root,borderwidth=3,relief=SUNKEN)
    c_id.place(x=280,y=60)

    ret = Button(root, text = "Search ID",width = 14,command=Ret, bg = "lawn green", fg = "white" , borderwidth=3,)
    ret.place(x=120,y=120)

    ex = Button(root,text = "Exit OUT" ,width = 14, command=lambda:[root.destroy(), panel.deiconify()], bg = "red", fg = "white" , borderwidth=3)
    ex.place(x=320,y=120)

    root.mainloop()

def IssRecord():

    panel.withdraw()

    root=tk.Tk()
    root.geometry("800x295+270+200")
    root.resizable(False,False)
    root.configure(bg = "azure")

    root.title("Issue Record")
    Label(root, text ="ISSUED BOOKS", font= "ComicSansms 12 bold",pady=7,bg = "azure").pack(side=TOP)
    tree = ttk.Treeview(root)

    ex = Button(root,text = "CLOSE",width = 14, command=lambda:[root.destroy(), panel.deiconify()], bg = "red", fg = "white" , borderwidth=3)
    ex.place(x=335,y=258)

    st = ttk.Style(root)
    st.theme_use("classic")

    st.configure("Treeview.Heading", foreground = 'lawn green', background = 'black')

    tree["columns"]=("Course_Id","B_Id","Student_Name","Issue_Date","Return_Date")


    tree.heading("#0", text ="", anchor=tk.CENTER)
    tree.heading("Course_Id",text = "Course_Id",anchor=tk.CENTER)
    tree.heading("B_Id",text = "B_Id",anchor=tk.CENTER)
    tree.heading("Student_Name",text = "Student_Name",anchor=tk.CENTER)
    tree.heading("Issue_Date",text ="Issue_Date",anchor=tk.CENTER)
    tree.heading("Return_Date",text = "Return_Date",anchor=tk.CENTER)
    
    tree.column("#0", width=0, stretch=NO)
    tree.column("Course_Id",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("B_Id",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("Student_Name",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("Issue_Date",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("Return_Date",minwidth=0,width=100,anchor=tk.CENTER)

    index=0
    iid =0

    sel = "Select * From Issue"
    cursor = db1.cursor()
    cursor.execute(sel)
    display = cursor.fetchall()

    for i in display:
        tree.insert("",index,iid, value=i)
        index = iid=index+1

    scr = ttk.Scrollbar(root,orient="vertical")
    scr.configure(command=tree.yview)
    tree.configure(yscrollcommand=scr.set)
    scr.pack(fill=BOTH,side=RIGHT)

    tree.pack()
    root.mainloop()

def RetRecord():

    panel.withdraw()

    root=tk.Tk()
    root.geometry("800x295+270+200")
    root.resizable(False,False)
    root.configure(bg = "azure")

    root.title("Return Record")
    Label(root, text ="RETURNED BOOKS", font= "ComicSansms 12 bold",pady=7,bg = "azure").pack(side=TOP)
    tree = ttk.Treeview(root)

    ex = Button(root,text = "CLOSE" ,width = 14, command=lambda:[root.destroy(), panel.deiconify()], bg = "red", fg = "white" , borderwidth=3)
    ex.place(x=335,y=258)

    st = ttk.Style(root)
    st.theme_use("classic")

    st.configure("Treeview.Heading", foreground = 'lawn green', background = 'black')

    tree["columns"]=("Course_Id","B_Id","Student_Name","Return_Date")

    tree.heading("#0", text ="", anchor=tk.CENTER)
    tree.heading("Course_Id",text = "Course_Id",anchor=tk.CENTER)
    tree.heading("B_Id",text = "B_Id",anchor=tk.CENTER)
    tree.heading("Student_Name",text = "Student_Name",anchor=tk.CENTER)
    tree.heading("Return_Date",text = "Return_Date",anchor=tk.CENTER)
    
    tree.column("#0", width=0, stretch=NO)
    tree.column("Course_Id",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("B_Id",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("Student_Name",minwidth=0,width=100,anchor=tk.CENTER)
    tree.column("Return_Date",minwidth=0,width=100,anchor=tk.CENTER)

    index=0
    iid =0

    sel = "Select * From Book_Return"
    cursor = db1.cursor()
    cursor.execute(sel)
    display = cursor.fetchall()

    for i in display:
        tree.insert("",index,iid, value=i)
        index = iid=index+1

    scr = ttk.Scrollbar(root,orient="vertical")
    scr.configure(command=tree.yview)
    tree.configure(yscrollcommand=scr.set)
    scr.pack(fill=BOTH,side=RIGHT)

    tree.pack()
    root.mainloop()

 
def Password():

    a_id = admin_id.get()
    a_pass = admin_pass.get()

    admin = "412002"
    code = "ambivert"


    if(a_id=="" or a_pass==""):
        messagebox.showwarning("Mandatory Field*","All Fields Are Required")

    else:
        if a_id == admin and a_pass == code:
            messagebox.showinfo("Status","Woohoo! Login Success")
            rot.after(50, lambda:rot.destroy())
            AdminPanel()

        elif a_id == admin and a_pass != code:
            messagebox.showerror("Status","Sorry! Password Is Incorrect") 
            rot.after(50, lambda:rot.destroy())

        elif a_id != admin and a_pass == code:
            messagebox.showerror("Status","sorry! ID Is Incorrect")  
            rot.after(50, lambda:rot.destroy())

        else:
            messagebox.showerror("Status","Both Details Are Incorrect")
            rot.after(50, lambda:rot.destroy())
          
def Admin():

    global rot

    rot = Tk()
    rot.geometry("550x250+420+240")
    rot.resizable(False,False)
    rot.title("Admin-Login")
    rot.configure(bg = "azure")

    Label(rot, text = "ENTER CREDENTIALS", font= "ComicSansms 12 bold", pady=5,bg = "azure").pack(side=TOP)

    Label(rot, text = 'Enter Your 6 Digit ID :',bg = "azure").place(x=120,y=80)

    global admin_id

    admin_id = Entry(rot,borderwidth=4,relief=SUNKEN)
    admin_id.place(x=300,y=80)

    Label(rot, text = 'Enter Your Password :',bg = "azure").place(x=120,y=120)

    global admin_pass

    admin_pass = Entry(rot,borderwidth=4,relief=SUNKEN)
    admin_pass.place(x=300,y=120)

    submit = Button(rot, text = "Sign In",width = 14, command=Password, bg = "green", fg = "white" , borderwidth=3,)
    submit.place(x=70,y=180)

    clr = Button(rot,text = "Clear",width = 14, command=Clr_Credentials, bg = "blue", fg = "white" , borderwidth=3)
    clr.place(x=225,y=180)
    
    exit = Button(rot,text = "Exit OUT",width = 14, command=rot.destroy, bg = "red", fg = "white" , borderwidth=3)
    exit.place(x=380,y=180)

    rot.mainloop()


def AdminPanel():

    global panel

    display.destroy()

    panel = Tk()
    panel.geometry("600x450+400+120")
    panel.title("Admin")
    panel.resizable(False,False)
    panel.configure(bg = "azure")

    Label(panel, text = "ADMIN PANEL", font= "ComicSansms 12 bold", pady=5,bg = "azure").pack(side=TOP)
    Label(panel, text = "Select From The Operations Below", font= "SansSerif 12 ",pady=20,bg = "azure").pack()

    Button(panel, text = "ADD NEW BOOK",command=AddBooks, width = 16, borderwidth=8 , fg = "white" , bg = "orange" ).place(x=70,y=130,)
    Button(panel, text = "VIEW ALL BOOK",command=AvailBooks, width = 16, borderwidth=8 , fg = "white" , bg = "orangered" ).place(x=250,y=130)
    Button(panel, text = "DELETE A BOOK",command=DeleteBooks, width = 16, borderwidth=8 , fg = "white" , bg = "orange" ).place(x=430,y=130)
    Button(panel, text = "ISSUE A BOOK",command=IssueBooks, width = 16, borderwidth=8 , fg = "white" , bg = "blue" ).place(x=70,y=200)
    Button(panel, text = "RETURN A BOOK",command=ReturnBooks, width = 16, borderwidth=8 , fg = "white" , bg = "green" ).place(x=250,y=200)
    Button(panel, text = "ISSUE RECORDS",command=IssRecord, width = 16, borderwidth=8 , fg = "white" , bg = "blue" ).place(x=430,y=200)
    Button(panel, text = "RETURN RECORDS",command=RetRecord, width = 16 , borderwidth=8 , fg = "white" , bg = "green").place(x=250,y=270)

    panel.mainloop()  

def UserPanel():
  
    global panel

    display.destroy()

    panel = Tk()
    panel.geometry("600x250+400+200")
    panel.title("User")
    panel.resizable(False,False)
    panel.configure(bg = "azure")

    Label(panel, text = "USER PANEL", font= "ComicSansms 12 bold", pady=5,bg = "azure").pack(side=TOP)
    Label(panel, text = "Select From The Operations Below", font= "SansSerif 12 ",pady=20,bg = "azure").pack()

    Button(panel, text = "VIEW ALL BOOK",command=AvailBooks, width = 16, borderwidth=5 , fg = "white" , bg = "green" ).place(x=70,y=130,)
    Button(panel, text = "ISSUE A BOOK",command=IssueBooks, width = 16, borderwidth=5 , fg = "white" , bg = "blue" ).place(x=250,y=130)
    Button(panel, text = "RETURN A BOOK",command=ReturnBooks, width = 16, borderwidth=5 , fg = "white" , bg = "orange" ).place(x=430,y=130)

    panel.mainloop()


def Main():

    global display

    display = Tk()
    display.geometry("750x500+330+100")
    display.resizable(False,False)
    display.title("DashBoard")

    display.configure(bg = "azure")

    Label(display, text = "e-PUSTAKALAY", font= "ComicSansms 16 bold", pady=5,bg = "azure").pack(side=TOP)
    Label(display, text = "Welcome To The World Of Wisdom", font= "SansSerif 14 italic", pady = 10,bg = "azure").pack(side=TOP)
    Label(display, text = "Please Select Your User Profile !", font= "ComicSansms 12", pady =60,bg = "azure").pack()

    user = Button(display, text = "LOGIN AS AN USER", width = 18,font = 'sans 10 bold',command=UserPanel, fg = "white", bg = "chartreuse2", borderwidth=5)
    user.place(x=305,y=220)

    admin = Button(display, text = "LOGIN AS AN ADMIN",width = 18,font = 'sans 10 bold',command=Admin, fg = "white", bg = "deepskyblue2" , borderwidth=5)
    admin.place(x=305,y=280)

    Label(display, text = "Copyright 2022. All Rights Reserved To The Creator",bg = "azure", font= "ComicSansms 8", pady = 5).pack(side=BOTTOM)
    
    display.mainloop()

Main()
