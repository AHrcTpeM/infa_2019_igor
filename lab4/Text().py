from tkinter import *
root = Tk()
frame = Frame()
frame.pack()

e = Entry(frame, width=25)
e.pack(pady=5, side=LEFT)

a = Button(frame, width=10, text="Открыть")
a.pack(side=LEFT)

b = Button(frame, width=10, text="Сохранить")
b.pack(side=LEFT)

text = Text(width=40, height=15)
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

root.mainloop()