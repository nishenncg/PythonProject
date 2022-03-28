from tkinter import *
expression = ""
def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="black")
    gui.title(" Calculator")
    gui.geometry("270x150")
    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

button7=Button(gui,command=lambda:press(7),text="7").grid(row=1,column=0)

button8=Button(gui,command=lambda:press(8),text="8").grid(row=1,column=1)

button9=Button(gui,command=lambda:press(9),text="9").grid(row=1,column=2)

add=Button(gui,command=lambda:press('+'),text="+").grid(row=1,column=3)

button4=Button(gui,command=lambda:press(4),text="4").grid(row=2,column=0)

button5=Button(gui,command=lambda:press(5),text="5").grid(row=2,column=1)

button6=Button(gui,command=lambda:press(6),text="6",).grid(row=2,column=2)

sub=Button(gui,command=lambda:press('-'),text="-").grid(row=2,column=3)

button1=Button(gui,command=lambda:press(1),text="1").grid(row=3,column=0)

button2=Button(gui,command=lambda:press(2),text="2").grid(row=3,column=1)

button3=Button(gui,command=lambda:press(3),text="3").grid(row=3,column=2)

mul=Button(gui,command=lambda:press('*'),text="*").grid(row=3,column=3)

button0=Button(gui,command=lambda:press(0),text="0").grid(row=4,column=0)

buttonC=Button(gui,command=clear,text="C").grid(row=4,column=1)

eql=Button(gui,command=equalpress,text="=").grid(row=4,column=2)

div=Button(gui,command=lambda:press('/'),text="/").grid(row=4,column=3)

gui.mainloop()