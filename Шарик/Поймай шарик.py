from tkinter import *
from random import randrange as rnd, choice
import time
WIDTH = 400
HEIGHT = 200

class Ball:
    def __init__(self):
        self.R = randint(20, 50)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = (+2, +3)
        self.ball_id = canvas.create_oval(self.x - self.R,
                                          self.y - self.R,
                                          self.x + self.R,
                                          self.y + self.R, fill="green")



s=0
colors = ['red','orange','yellow','green','blue']
def new_ball():
    canv.delete(ALL)
    global x, y, r, s
    canv.create_text(20, 15, text="Счет: %i" % s,
                     anchor=W, font="Verdana 14")
    x = rnd(100,700)
    y = rnd(100,500)
    r = rnd(30,50)
    ball=canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)

    # def motion():
    #     canv.move(ball, 5, 0)
    #     if canv.coords(ball)[0] < 700:
    #         root.after(50, motion)
    # motion()

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


root = Tk()
root.geometry(str(WIDTH) + "x" + str(HEIGHT))
canv = Canvas(root,bg='white')
canv.pack(fill=BOTH,expand=1)
new_ball()
canv.bind('<Button-1>', click)
mainloop()