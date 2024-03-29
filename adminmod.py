#ADMIN
from tkinter import *
from tkinter import ttk
import mysql.connector as mys
import functions
from tkinter import messagebox

db=mys.connect(host="localhost",user="root",passwd="sql123",database="online_shopping")
csor=db.cursor()

def buyer():
    global tree,root2,csor
    root2=Toplevel()
    root2.title("Admin-Buyer details")
    root2.state('zoomed')
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root2, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    buyer=Label(root2,text="BUYER DETAILS",font=("Impact",60), fg='forest green',bg='white').pack()
    tree=ttk.Treeview(root2, column=("c1", "c2", "c3","c4","c5"), show='headings')
    tree.column("#1", anchor=CENTER)
    tree.heading("#1", text="BUYER ID")
    tree.column("#2", anchor=CENTER)
    tree.heading("#2", text="PASSWORD")
    tree.column("#3", anchor=CENTER)
    tree.heading("#3", text="DOR")
    tree.column("#4", anchor=CENTER)
    tree.heading("#4", text="EMAIL")
    tree.column("#5", anchor=CENTER)
    tree.heading("#5", text="PHONE NO")
    tree.pack()
    csor.execute('''SELECT * FROM buyer''')
    rows=csor.fetchall()
    for r in rows:
        print(r)
        tree.insert("",END, values=r)
    mainloop()

def seller():
    global tree1,root3,csor
    root3=Toplevel()
    root3.title("Admin - Seller Details")
    root3.state('zoomed')
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root3, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    buyer=Label(root3,text="SELLER DETAILS",font=("Impact",60), fg='forest green',bg='white').pack()
    tree1=ttk.Treeview(root3, column=("c1", "c2", "c3","c4","c5"), show='headings')
    tree1.column("#1", anchor=CENTER)
    tree1.heading("#1", text="SELLER ID")
    tree1.column("#2", anchor=CENTER)
    tree1.heading("#2", text="PASSWORD")
    tree1.column("#3", anchor=CENTER)
    tree1.heading("#3", text="DOR")
    tree1.column("#4", anchor=CENTER)
    tree1.heading("#4", text="EMAIL")
    tree1.column("#5", anchor=CENTER)
    tree1.heading("#5", text="PHONE NO")
    tree1.pack()
    csor.execute('''SELECT * FROM seller''')
    rows=csor.fetchall()
    for r in rows:
        print(r)
        tree1.insert("",END, values=r)
    mainloop()

def products():
    global tree2,root4,csor
    root4=Toplevel()
    root4.title("Admin - Product Details")
    root4.state('zoomed')
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root4, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    buyer=Label(root4,text="PRODUCT DETAILS",font=("Impact",60), fg='forest green',bg='white').pack()
    tree2=ttk.Treeview(root4, column=("c1", "c2", "c3","c4","c5","c6"), show='headings')
    tree2.column("#1", anchor=CENTER)
    tree2.heading("#1", text="PRODUCT ID")
    tree2.column("#2", anchor=CENTER)
    tree2.heading("#2", text="PRODUCT NAME")
    tree2.column("#3", anchor=CENTER)
    tree2.heading("#3", text="PRODUCT DETAILS")
    tree2.column("#4", anchor=CENTER)
    tree2.heading("#4", text="PRODUCT PRICE")
    tree2.column("#5", anchor=CENTER)
    tree2.heading("#5", text="SELLER ID")
    tree2.column("#6", anchor=CENTER)
    tree2.heading("#6", text="BUYER ID")
    tree2.pack()
    csor.execute('''SELECT * FROM products''')
    rows=csor.fetchall()
    for r in rows:
        print(r)
        tree2.insert("",END, values=r)
    #####
    remove=Button(root4, text="REMOVE",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green",command=lambda: functions.remove(rows))
    remove.place(x=650,y=400)
    ####
    mainloop()

def adminpage1():
    global var1,var2,var3,root1
    root1=Toplevel()
    root1.title("Admin Homescreen")
    root1.state('zoomed')
    global bg
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/AdminScreen.png")
    my_label=Label(root1, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    var1=IntVar()
    var2=IntVar()
    var3=IntVar()
    Wel=Label(root1, text="ADMIN", fg="forest green",font=("Impact",60), bg="white").pack()
    ch=Label(root1, text="SELECT THE DATA YOU WANT TO VIEW", font=("Merriweater",24),bg="white",fg="forest green").pack()
    btn1 = Button(root1, text = "BUYERS", height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green",command=buyer)
    btn2 = Button(root1, text = "SELLERS", height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green",command=seller)
    btn3 = Button(root1, text = "PRODUCTS", height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green",command=products)
    btn1.place(x=270, y=500)
    btn2.place(x=680, y=500)
    btn3.place(x=1110, y=500)

def submit():
    global e1,e2,user_id,password,root
    en1=e1.get()
    en2=e2.get()
    print(en1,en2)
    user_id.set("")
    password.set("")
    if en1=="ADMIN" and en2=="pass":
        root.destroy()
        adminpage1()
    else:
        messagebox.showerror("Error","Incorrect Credentials!")

def admin():
    global user_id,password,root,e1,e2
    root=Toplevel()
    root.title("Admin Login")
    root.state('zoomed')
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Admin2.png")
    my_label=Label(root, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    user_id=StringVar()
    password=StringVar()
    welcome=Label(root,text="ADMIN CREDENTIALS",fg="forest green",font=("Impact",60), bg="white")
    welcome.pack()
    user=Label(root,text="USER",font=("Deja Vu Serif",24), fg="white", bg='forest green').place(x=350,y=400)
    passwd=Label(root,text="PASSWORD",font=("Deja Vu Serif",24), fg="white", bg='forest green').place(x=350,y=500)
    e1=ttk.Entry(root, width=20, font=("arial",15))
    e1.place(x=600,y=400)
    e2=ttk.Entry(root,width=20, font=("arial",15))
    e2.place(x=600,y=500)
    submit1=Button(root, text="LOGIN",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green", command=submit).place(x=500,y=650)
    mainloop()
