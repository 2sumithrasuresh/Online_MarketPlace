#Imports
import functions
from tkinter import *
from tkinter import ttk
import mysql.connector as mys

db=mys.connect(host="localhost", user="root", passwd="sql123", database="online_shopping")
if db.is_connected():
    print("Connection Successful")
cursor=db.cursor()

def seller(uid):
    root=Toplevel()
    root.title("Seller Homepage")
    root.state('zoomed')
    bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/Seller.png")
    my_label=Label(root, image=bg)
    my_label.place(x=0,y=0, relwidth=1,relheight=1)
    intro=Label(root, text=("Welcome",uid),font=("Impact",60), fg='forest green',bg='white')
    intro.pack()
    cursor.execute("select * from products where seller_id=(%s)",(uid,))
    data=cursor.fetchall()
    print(data)
    tree = ttk.Treeview(root, column=("c1", "c2", "c3","c4","c5"), show='headings')
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="PRODUCT ID")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="PRODUCT")
    tree.column("# 3", anchor=CENTER)
    tree.heading("# 3", text="PRICE")
    tree.column("#4",anchor=CENTER)
    tree.heading("#4",text="CATEGORY")
    tree.column("#5",anchor=CENTER)
    tree.heading("#5",text="STATUS")
    productlist=[]
    for i in data:
        productlist.append((i[0],i[1],i[3],i[6],i[5]))
    print (productlist)
    for i in productlist:
        tree.insert('', 'end', values=i)
    tree.place(x=250, y=200)
    remove=Button(root, text="REMOVE",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green", command=lambda: functions.remove(data))
    remove.place(x=250, y=500)
    add=Button(root, text="ADD",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green", command=lambda: functions.add(uid))
    add.place(x=680, y=500)
    sold=Button(root, text="SOLD",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green", command=lambda: functions.sold(data))
    sold.place(x=1110, y=500)
    mainloop()
