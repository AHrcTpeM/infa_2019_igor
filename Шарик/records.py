from tkinter import *
from random import randrange as rnd

#def record():
def nik():
    global i, s
    e1 = e.get()
    d = rnd(500, 1000)
    records = ('{0}. {1} = {2}\n'.format(i, e1, d))
    i += 1
    f = open('рекорды.txt', 'a')
    f.write(records)
    f.close()

root1 = Tk()
l = Label(root1, text="Введи свой ник герой!", width=20)
e = Entry(root1, width=20)
b = Button(root1, text="OK", command=nik)
i = 1
l.pack()
e.pack()
b.pack()
root1.mainloop() 
