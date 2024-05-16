from tkinter import*
import math
mansLogs=Tk()
mansLogs.title("Kalkulators")

def btnClick(number):
    current=e.get()#nolasa skaitli
    e.delete(0,END)#nodzēš
    newNumber=str(current)+str(number)
    e.insert(0,newNumber)#ievieto displejā
    return 0

def btnCommand(command):
    global number
    global num1#Jāiegaumē skaitlis, darbība
    global mathOp#matemātiskais operators
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0

def Vienads():
    num2=int(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="/":
        result=num1/num2
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def notirit():
    e.delete(0,END)
    num1=0
    mathOp="C"
    return 0


e=Entry(mansLogs,width=15,bd=20,font=("Ariel Black",30),justify="right")#Izveido logu



btn0=Button(mansLogs,text="0",padx="40",pady="20",bg="red",command=lambda:btnClick(0))
btn1=Button(mansLogs,text="1",padx="40",pady="20",bg="red",command=lambda:btnClick(1))
btn2=Button(mansLogs,text="2",padx="40",pady="20",command=lambda:btnClick(2))
btn3=Button(mansLogs,text="3",padx="40",pady="20",command=lambda:btnClick(3))
btn4=Button(mansLogs,text="4",padx="40",pady="20",bg="red",command=lambda:btnClick(4))
btn5=Button(mansLogs,text="5",padx="40",pady="20",command=lambda:btnClick(5))
btn6=Button(mansLogs,text="6",padx="40",pady="20",command=lambda:btnClick(6))
btn7=Button(mansLogs,text="7",padx="40",pady="20",bg="red",command=lambda:btnClick(7))
btn8=Button(mansLogs,text="8",padx="40",pady="20",command=lambda:btnClick(8))
btn9=Button(mansLogs,text="9",padx="40",pady="20",command=lambda:btnClick(9))

btnSask=Button(mansLogs,text='+',padx='40',pady="20",bg="red",command=lambda:btnCommand("+"))
btnAtn=Button(mansLogs,text='-',padx='40',pady="20",bg="red",command=lambda:btnCommand("-"))
btnReiz=Button(mansLogs,text='*',padx='40',pady="20",bg="red",command=lambda:btnCommand("*"))
btnDal=Button(mansLogs,text='/',padx='40',pady="20",bg="red",command=lambda:btnCommand("/"))
btnIr=Button(mansLogs,text='=',padx='40',pady="20",command=Vienads)
btnC=Button(mansLogs,text='C',padx='40',pady="20",command=notirit)


btnSask.grid(row=1,column=3)
btnAtn.grid(row=2,column=3)
btnReiz.grid(row=3,column=3)
btnDal.grid(row=4,column=3)
btnIr.grid(row=4,column=2)
btnC.grid(row=4,column=1)

btn7.grid(row=1,column=0)
btn8.grid(row=1,column=1)
btn9.grid(row=1,column=2)

btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row=2,column=2)

btn1.grid(row=3,column=0)
btn2.grid(row=3,column=1)
btn3.grid(row=3,column=2)

btn0.grid(row=4,column=0)

e.grid(row=0,column=0,columnspan=4)#Atrašanās vieta



































mansLogs.mainloop()