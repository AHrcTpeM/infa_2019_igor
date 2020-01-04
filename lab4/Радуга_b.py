from tkinter import *
root = Tk()

def insert1():
    l['text'] = 'красный'
    e.delete(0, END)
    e.insert(0, '#ff0000')
def insert2():
    l['text'] = 'оранжевый'
    e.delete(0, END)
    e.insert(0, '#ff7d00')
def insert3():
    l['text'] = 'желтый'
    e.delete(0, END)
    e.insert(0, '#ffff00')
def insert4():
    l['text'] = 'зеленый'
    e.delete(0, END)
    e.insert(0, '#00ff00')
def insert5():
    l['text'] = 'голубой'
    e.delete(0, END)
    e.insert(0, '#007dff')
def insert6():
    l['text'] = 'синий'
    e.delete(0, END)
    e.insert(0, '#0000ff')
def insert7():
    l['text'] = 'фиолетовый'
    e.delete(0, END)
    e.insert(0, '#7d00ff')

l = Label(width=16)
e = Entry(width=20, justify=CENTER)

l.pack()
e.pack(pady=5)
b1 = Button(bg='#ff0000', width=2, command=insert1).pack(side=LEFT, padx=1, pady=1)
b2 = Button(bg='#ff7d00', width=2, command=insert2).pack(side=LEFT, padx=1, pady=1)
b3 = Button(bg='#ffff00', width=2, command=insert3).pack(side=LEFT, padx=1, pady=1)
b4 = Button(bg='#00ff00', width=2, command=insert4).pack(side=LEFT, padx=1, pady=1)
b5 = Button(bg='#007dff', width=2, command=insert5).pack(side=LEFT, padx=1, pady=1)
b6 = Button(bg='#0000ff', width=2, command=insert6).pack(side=LEFT, padx=1, pady=1)
b7 = Button(bg='#7d00ff', width=2, command=insert7).pack(side=LEFT, padx=1, pady=1)

root.mainloop()