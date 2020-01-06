from tkinter import *

def Open():
    s = Entry.get()
    f = open(s)
    text.insert(1.0, f.read())

def Save():
    s = Entry.get()
    s2 = text.get(1.0, END)
    f2 = open(s, 'w')
    f2.write(s2)

root = Tk()
frame = Frame()
frame.pack()

Entry = Entry(frame, width=25)
Entry.pack(pady=5, side=LEFT)

a = Button(frame, width=10, text="Открыть", command=Open)
a.pack(side=LEFT)

b = Button(frame, width=10, text="Сохранить", command=Save)
b.pack(side=LEFT)

text = Text(width=40, height=15)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

root.mainloop()