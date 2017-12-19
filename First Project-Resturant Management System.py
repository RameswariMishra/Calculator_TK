from Tkinter import *
import random
import time
from PIL import Image, ImageTk

root = Tk()
root.geometry("1600x800+0+0")
root.title("Resturant Management System")
img = ImageTk.PhotoImage(file='/home/rameswari/Dropbox/tk-project/index.ico')
root.tk.call('wm', 'iconphoto', root._w, img)

text_Input = StringVar()
operator = ""

tops = Frame(root,width = 1600,height = 50,bg="yellow",relief=SUNKEN)
tops.pack(side=TOP)

lf = Frame(root,width = 800,height = 700,bg = "yellow",relief = SUNKEN)
lf.pack(side=LEFT)

rf = Frame(root,width = 300,height = 700,bg="yellow",relief=SUNKEN)
rf.pack(side=RIGHT)

heading = Label(tops,font=('arial',50,'bold'),text = "Resturant Management Systems",fg = "black", bd=10, anchor = 'w' )
heading.grid(row=0,column=0)

#-----time----
localtime = time.asctime(time.localtime(time.time()))

#----labelinfo----
lblinfo = Label(tops,font = ('ariel',50,'bold', ), text = "Restaurant Management System",bd =10,fg = "blue", anchor = 'w')
lblinfo.grid(row=0,column=0)
lblinfo = Label(tops,font = ('ariel',20,'bold', ), text = localtime,fg = "blue", bd = 10, anchor = 'w')
lblinfo.grid(row=1,column=0)
#---------calculator----------#
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

def btnEquals():
    global operator
    sumUp = str(eval(operator))
    text_Input.set(sumUp)
    operator = ""

txtDisplay = Entry(rf,font = ('arial',20,'bold' ),textvariable = text_Input, insertwidth = 4, bd = 20, bg = "light pink", justify = "right")
txtDisplay.grid(columnspan = 4)


btn1 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "1", command = lambda:btnClick(1)).grid(row=2,column=0)
btn2 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "2", command = lambda:btnClick(2)).grid(row=2,column=1)
btn3 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "3", command = lambda:btnClick(3)).grid(row=2,column=2)
Addition =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "+", command = lambda:btnClick("+")).grid(row=2,column=3)



btn4 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "4", command = lambda:btnClick(4)).grid(row=3,column=0)
btn5 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "5", command = lambda:btnClick(5)).grid(row=3,column=1)
btn6 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "6", command = lambda:btnClick(6)).grid(row=3,column=2)
Subtraction =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "-", command = lambda:btnClick("-")).grid(row=3,column=3)

btn7 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "7", command = lambda:btnClick(7)).grid(row=4,column=0)
btn8 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "8", command = lambda:btnClick(8)).grid(row=4,column=1)
btn9 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "9", command = lambda:btnClick(9)).grid(row=4,column=2)
Multiplication =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "*", command = lambda:btnClick("*")).grid(row=4,column=3)

btn0 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "0", command = lambda:btnClick(0)).grid(row=5,column=0)
btnClear =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "C", command = btnClear).grid(row=5,column=1)
btnEquals =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "=", command = btnEquals).grid(row=5,column=2)
btnDivision =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "/", command = lambda:btnClick("/")).grid(row=5,column=3)
#btn7 =  Button(rf,padx=16,pady=16,bd = 8,bg = 'light pink',font = ('arial',20,'bold'), text = "7", command = lambda:btnClick(7)).grid(row=4,column=0)

root.mainloop()

