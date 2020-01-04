from tkinter import *
from random import randrange as rnd, choice
import time
root = Tk()
root.geometry('800x600')

canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)

colors = ['red','orange','yellow','green','blue']
def new_ball():
    canv.delete(ALL)
    global x, y, r, s
    canv.create_text(20, 15, text="Счет: %i" % s,
                     anchor=W, font="Verdana 14")
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    root.after(1000,new_ball)

def click(event):
    global s
    print(x,y,r)
    print(event.x, event.y)
    R=((x-event.x)**2+(y-event.y)**2)**0.5
    if R<r:
        s+=1
    else:
        s-=1
s=0


new_ball()
canv.bind('<Button-1>', click)
mainloop()