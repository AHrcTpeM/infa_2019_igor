from tkinter import *

root = Tk()
frame1=Frame(root)
e1 = Entry(width=20)
e2 = Entry(width=20)
b1 = Button(text="+", width=4)
b2 = Button(text="-", width=4)
b3 = Button(text="/", width=4)
b4 = Button(text="*", width=4)
l = Label(text="-", bg='black', fg='white', width=20)

def Suma(event):
    try:
        s1 = e1.get()
        s2 = e2.get()
        s = str(round(float(s1)+float(s2), 4))
    except ValueError:
        l['text'] = 'Ошибка'
    l['text'] = s
def Minus(event):
    try:
        s1 = e1.get()
        s2 = e2.get()
        s = str(round(float(s1)-float(s2), 4))
    except ValueError:
        l['text'] = 'Ошибка'
    l['text'] = ''.join(s)
def Delim(event):
    try:
        s1 = e1.get()
        s2 = e2.get()
        s = str(round(float(s1)/float(s2), 4))
    except ValueError:
        l['text'] = 'Ошибка'
    except ZeroDivisionError:
        l['text'] = 'Деление на 0 невозможно'
    l['text'] = ''.join(s)
def Mnojim(event):
    try:
        s1 = e1.get()
        s2 = e2.get()
        s = str(round(float(s1)*float(s2), 4))
    except ValueError:
        l['text'] = 'Ошибка'
    l['text'] = ''.join(s)

b1.bind('<Button-1>', Suma)
b2.bind('<Button-1>', Minus)
b3.bind('<Button-1>', Delim)
b4.bind('<Button-1>', Mnojim)

e1.grid(row=0,column=0,columnspan=4)
e2.grid(row=1,column=0,columnspan=4)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)
b4.grid(row=2,column=3)
l.grid(row=3,column=0,columnspan=4)

root.title("Калькулятор")
root.mainloop()