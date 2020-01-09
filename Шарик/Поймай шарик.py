from tkinter import *
from random import randrange as rnd, choice
import time
WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self):
        self.R = rnd(20, 50)
        self.x = rnd(self.R, WIDTH - self.R)
        self.y = rnd(self.R, HEIGHT - self.R)
        self.dx, self.dy = (choice([-2,2]), choice([-3,3]))
        self.ball_id = canvas.create_oval(self.x - self.R, self.y - self.R,
                                          self.x + self.R, self.y + self.R,
                                          fill=choice(['red','orange','yellow','green','blue']))

    def __del__(self):
        pass

    def move(self):
        global  s, screen
        self.x += self.dx
        self.y += self.dy
        if self.x + self.R > WIDTH or self.x - self.R <= 0:
            self.dx = -self.dx
            if rnd(1,3)==1:
                self.dy = self.dy*2
            else:
                self.dy = -self.dy*2
        if self.y + self.R > HEIGHT or self.y - self.R <= 0:
            s -= 1
            canvas.itemconfig(screen, text="Счет: %i" % s)
            self.dy = -self.dy
            if rnd(1,3)==1:
                self.dx = self.dx
            else:
                self.dx = -self.dx

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

    def show(self):
        canvas.move(self.ball_id, self.dx, self.dy)

def tick():
    for ball in balls:
        ball.move()
        ball.show()
    root.after(30, tick)

s=0
def click(event):
    global s, screen, balls
    for ball in balls:
        r = ((ball.x - event.x) ** 2 + (ball.y - event.y) ** 2) ** 0.5
        if r < ball.R:
            s += 2
            canvas.itemconfig(screen, text="Счет: %i" % s)
            canvas.delete(ball.ball_id)
            balls.remove(ball)
            balls.append(Ball())
    s -= 1
    canvas.itemconfig(screen, text="Счет: %i" % s)

root = Tk()
root.geometry(str(WIDTH) + "x" + str(HEIGHT))
canvas = Canvas(root, bg='white')
canvas.pack(fill=BOTH, expand=1)
screen = canvas.create_text(20, 15, text="Счет: %i" % s,
                       anchor=W, font="Verdana 14")
balls = [Ball() for i in range(5)]
tick()
canvas.bind('<Button-1>', click)
mainloop()