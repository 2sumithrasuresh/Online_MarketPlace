#Small Modules
from datetime import date
import sellermod
import buyermod
import mysql.connector as mys
import random
from tkinter import *
from tkinter import messagebox
from email_validator import validate_email, EmailNotValidError
from tkinter import ttk
import buyermod

#SQL Connection
db=mys.connect(host="localhost", user="root", passwd="sql123", database="online_shopping")
if db.is_connected():
    print("Connection Successful")
    cursor=db.cursor()

def createpid():
    cursor.execute("select * from products")
    data=cursor.fetchall()
    print(data)
    lst=[]
    for i in data:
        lst.append(i[0])
    print(lst)
    pid=0
    for i in lst:
        if pid<int(i):
            pid=int(i)
    pid+=1
    print(pid)
    return pid

def submitbuyers(uid,pw,em,no):
    print(pw,em,no)
    print(pw, em, no)
    q1="insert into buyer(buyer_id,passwd,DOR,email,ph_no) values(%s,%s,%s,%s,%s)"
    print("Q! ")
    cursor.execute(q1,(uid, pw, date.today(),em, no))
    db.commit()
    messagebox.showinfo("Confirmation","You have successfully registered as a Buyer")
    print("PP")

def submitsellers(uid,pw,em,no):
    q1="insert into seller values(%s,%s,%s,%s,%s)"
    cursor.execute(q1,(uid, pw, date.today(), em, no))
    db.commit()
    messagebox.showinfo("Confirmation","You have successfully registered as a Seller")

def submitdetails(uid,pw):
    cursor.execute("select * from seller")
    data=cursor.fetchall()
    selleruid=[]
    sellerpw=[]
    for i in data:
        selleruid.append(i[0])
    for i in data:
        sellerpw.append(i[1])
    print(selleruid)
    print(sellerpw)
    cursor.execute("select * from buyer")
    data=cursor.fetchall()
    buyeruid=[]
    buyerpw=[]
    for i in data:
        buyeruid.append(i[0])
    for i in data:
        buyerpw.append(i[1])
    print(buyeruid)
    print(buyerpw)
    ch=0
    for i in selleruid:
        if str(uid)==i:
            ind=selleruid.index(i)
            ch=1            
        print(type(i))
        print(type(uid))
        print(i)
        print(uid)
    for i in buyeruid:
        if str(uid)==i:
            ind=buyeruid.index(i)
            ch=2
    if ch==1:
        print(sellerpw[ind],pw)
        if sellerpw[ind]==str(pw):
            sellermod.seller(uid)
        else:
            messagebox.showerror("Error","Incorrect Password")
    elif ch==2:
        if buyerpw[ind]==pw:
            buyermod.show()

        else:
            messagebox.showerror("Error","Incorrect Password")
    else:
        messagebox.showerror("Error","User ID does not exist")
                               
    cursor.execute("select * from buyer")
    data=cursor.fetchall()
    buyeruid=[]
    buyerpw=[]
    for i in data:
        buyeruid.append(i[0])
    for i in data:
        buyerpw.append(i[2])

def delprod(i):
    cursor.execute("delete from products where prod_id=(%s)", (i[0],))
    db.commit()
    messagebox.showinfo("Confirmation","Product has been removed from sale")

def remove(data):
    root=Toplevel()
    root.title("Remove Products")
    root.state('zoomed')
    global bg
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    msg=Label(root, text="Select the product you want to remove",font=("Merriweater",24),bg="white",fg="forest green")
    msg.pack()
    for i in data:
        prod=Button(root, text=i[1],height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green", command=lambda: delprod(i))
        prod.pack()
        
def add(uid):
    root=Toplevel()
    root.title("Add Products")
    root.state('zoomed')
    global bg
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    msg=Label(root, text="Fill out details of product you wish to add",font=("Merriweater",24),bg="white",fg="forest green")
    msg.pack()
    dropdown=Label(root, text="Select Category",font=("Merriweater",24),bg="white",fg="forest green")
    dropdown.place(x=480,y=350)
    choice=StringVar()
    drop=OptionMenu(root, choice, "Electronics", "Books","Furniture","Fashion","Other").place(x=750,y=350)
    print(choice.get())
    a=Entry(root,width=20,font=('Arial 24',19))
    b=Entry(root,width=20,font=('Arial 24',19))
    c=Entry(root,width=20,font=('Arial 24',19))
    a.place(x=480,y=200)
    b.place(x=480,y=250)
    c.place(x=480,y=300)
    a.insert(0, "Enter Product Name")
    b.insert(0, "Enter Price")
    c.insert(0, "Enter Product Details")
    submit=Button(root, text="Submit",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green", command=lambda:insert(uid,a.get(),b.get(),c.get(),choice.get()))
    submit.place(x=500,y=450)

def insert(uid,pname,price,details,category):
    print(category)
    pid=createpid()
    buid=None
    q1="insert into products values(%s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(q1,(pid, pname,details, int(price), str(uid),"On sale",category))
    db.commit()
    messagebox.showinfo("Confirmation","Product has been put up for sale")

def checkdetails(uid,pw,email,no,choice):
    #Check if UserID already exists
    cursor.execute("select * from buyer")
    bdata=cursor.fetchall()
    cursor.execute("select * from seller")
    sdata=cursor.fetchall()
    print(bdata,sdata)
    flag1=False
    for i in sdata:
        if i[0]==uid:
            flag1=True
    for j in bdata:
        if j[0]==uid:
            flag1=True
    if flag1==True:
        messagebox.showerror("Error","UserID already exists!")
    #Check if email is valid
    flag2=False
    try:
        v = validate_email(email) 
        email = v["email"]  
    except EmailNotValidError as e:
        messagebox.showerror("Error",str(e))
        flag2=True
    if flag1==False and flag2==False:
        if choice=="B":
            submitbuyers(uid,pw,email,no)
        else:
            submitbuyers(uid,pw,email,no)
    mainloop()

def sold(data):
    root=Toplevel()
    root.title("Mark as Sold")
    root.state('zoomed')
    global bg
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    msg=Label(root, text="Select the product you want to mark as sold",font=("Merriweater",24),bg="white",fg="forest green")
    msg.pack()
    for i in data:
        prod=Button(root, text=i[1],height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green", command=lambda: mark(i))
        prod.pack()

def mark(i):
    cursor.execute('''UPDATE products SET Status="Sold" WHERE prod_id=(%s)''', (i[0],))
    db.commit()
    messagebox.showinfo("Confirmation","Product has been marked as sold")

def filterout(ch):
    print("In filter fxn")
    root=Toplevel()
    root.title("Filtered Products")
    root.state('zoomed')
    global bg
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    buyer=Label(root, text=ch.upper(),font=("Impact",60), fg='forest green',bg='white').pack()
    tree=ttk.Treeview(root, column=("c1", "c2", "c3","c4"), show='headings')
    tree.column("#1", anchor=CENTER)
    tree.heading("#1", text="PRODUCT ID")
    tree.column("#2", anchor=CENTER)
    tree.heading("#2", text="PRODUCT NAME")
    tree.column("#3", anchor=CENTER)
    tree.heading("#3", text="PRODUCT PRICE")
    tree.column("#4", anchor=CENTER)
    tree.heading("#4", text="CATEGORY")
    tree.pack()
    cursor.execute('''SELECT prod_id,prod_name,prod_price, category FROM PRODUCTS WHERE status ="On Sale" and category=(%s)''', (ch,))
    rows=cursor.fetchall()
    for r in rows:
        print("Filter fxn")
        print(r)
        tree.insert("",END, values=r)
      
