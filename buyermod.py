from tkinter import *
from tkinter import ttk
import functions
import mysql.connector as mys
from tkinter import messagebox
db=mys.connect(host="localhost",user="root",passwd="sql123",database="online_shopping")
csor=db.cursor()

def proceed():
    global csor,db,ch_prod
    ch=int(ch_prod.get())
    csor.execute('''SELECT seller_id  FROM products WHERE  prod_id = %s''',(ch,))
    data1=csor.fetchone()
    print(data1)
    seller_id=data1[0]
    root8=Toplevel()
    root8.title("Seller Details")
    root8.state('zoomed')
    global bg
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root8, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    label1=Label(root8, text="SELLER DETAILS",font=("Impact",60), fg='forest green',bg='white').pack()
    csor.execute('''SELECT seller_id,email,ph_no FROM SELLER WHERE seller_id = %s''',(seller_id,))
    data=csor.fetchone()
    name,email_id,phone_no=tuple(data)
    label2=Label(root8, text=("Seller-ID:",name),font=("merriweater",20),padx=10,pady=10,bg="white").pack()
    label1=Label(root8, text=("EMAIL-ID:",email_id),font=("merriweater",20),padx=10,pady=10,bg="white").pack()
    label1=Label(root8, text=("PHONE-NUMBER:",phone_no),font=("merriweater",20),padx=10,pady=10,bg="white").pack()

#SEARCH PRODUCTS
def search():
    global productid,csor,ch_prod,root6,proname,product_name,prodID,seller_id
    print("In search fxn")
    ch=ch_prod.get()
    root6=Toplevel()
    root6.title("Product Details")
    root6.state('zoomed')
    global bg
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root6, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    csor.execute('''SELECT prod_id,prod_name,product_det,prod_price,seller_id FROM PRODUCTS WHERE prod_id = %s ''',(int(ch),))
    data=csor.fetchone()
    print(data)
    product_id,product_name,product_det,product_price,seller_id=tuple(data)
    prod=Label(root6,text="PRODUCT DETAILS",font=("Impact",60), fg='forest green',bg='white').pack()
    prod1=Label(root6,text=("PRODUCT-ID:",product_id),font=("merriweater",20),padx=10,pady=10,bg="white").pack()
    prod2=Label(root6,text=("PRODUCT-NAME:",product_name),font=("merriweater",20),padx=10,pady=10,bg="white").pack()
    prod3=Label(root6,text=("PRODUCT-DETAILS:",product_det),font=("merriweater",20),padx=10,pady=10,bg="white").pack()
    prod4=Label(root6,text=("PRODUCT-PRICE:",product_price),font=("merriweater",20),padx=10,pady=10,bg="white").pack()
    prod5=Label(root6,text=("SELLER-ID:",seller_id),font=("merriweater",20),padx=10,pady=10,bg="white").pack()
    ordernow=Button(root6, text="ORDER NOW",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green", command=proceed).pack()

#SHOW TABLE
def show():
    global tree,ch_prod,root5,root
    root5=Toplevel()
    root5.title("Buyer Homepage")
    root5.state('zoomed')
    global bg
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root5, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    buyer=Label(root5, text="PRODUCTS",font=("Impact",60), fg='forest green',bg='white').pack()
    tree=ttk.Treeview(root5, column=("c1", "c2", "c3","c4"), show='headings')
    tree.column("#1", anchor=CENTER)
    tree.heading("#1", text="PRODUCT ID")
    tree.column("#2", anchor=CENTER)
    tree.heading("#2", text="PRODUCT NAME")
    tree.column("#3", anchor=CENTER)
    tree.heading("#3", text="PRODUCT PRICE")
    tree.column("#4", anchor=CENTER)
    tree.heading("#4", text="CATEGORY")
    tree.pack()
    csor.execute('''SELECT prod_id,prod_name,prod_price, category FROM PRODUCTS WHERE status ="On Sale"''')
    rows=csor.fetchall()
    for r in rows:
        print(r)
        tree.insert("",END, values=r)
    ch_prod=ttk.Entry(root5,width=20,font=('Arial 24',13))
    ch_prod.place(x=580,y=400)
    ch_prod.insert(0, "Enter Product id")
    button2=Button(root5, text="SEARCH",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",13),fg="dark green", command=search).place(x=780, y=380)
    #Category filter - Electronics, Books, Fashion, Furniture, Other
    choice=StringVar()
    drop=OptionMenu(root5, choice, "Electronics", "Books","Furniture","Fashion","Other").place(x=680,y=550)
    filt=Button(root5, text="FILTER",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",13),fg="dark green", command=lambda: functions.filterout(choice.get())).place(x=780,y=530)
