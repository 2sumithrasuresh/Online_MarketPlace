#Main Program
import functions
from tkinter import *
import Logregad_module
import adminmod

root=Tk()
root.title("Home Page")
root.state('zoomed')

bg=PhotoImage(file="D:/Sumithra_Personal_Folders/Sumithra/Mini Project - Python/bg/HomeScreen.png")

my_label=Label(root, image=bg)
my_label.place(x=0,y=0, relwidth=1,relheight=1)
              

name=Label(root, text="BECHO BAZAAR",fg="forest green",font=("Impact",60), bg="white")
name.place(x=150,y=20)
tagline=Label(root, text="Where Buying meets Selling",fg="sea green",font=("Times New Roman",25,"bold italic"), bg="white")
tagline.place(x=150, y=700)
login=Button(root, text="LOGIN",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green",command=Logregad_module.loginpage)
register=Button(root, text="REGISTER",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green",command=Logregad_module.registerpage)
admin=Button(root, text="ADMIN",height=2,width=10,bg="DarkSeaGreen2",font=("Helvetica",19),fg="dark green",command=adminmod.admin)
login.place(x=1100,y=200)
register.place(x=1100, y=400)
admin.place(x=1100, y=600)

mainloop()

