from graph import *

windowSize(1000, 600)
canvasSize(1000, 600)

brushColor(0, 100, 200)
rectangle(0,0,1000,300)
brushColor(100, 200, 100)
rectangle(0,300,1000,600)

def man(x):
    brushColor('grey')
    oval(x, 190, (x+120), 410)
    line(x+33, 400, x-5, 550)
    line(x-5, 550, x-30, 550)
    line(x+85, 400, x+130, 550)
    line(x+130, 550, x+155, 550)
    brushColor('white')
    circle(x+60, 170, 40)
    line(x+18, 225, x-40, 330)
    line(x+104, 225, x+158, 330)
man(140)
man(525)

def woman(x):
    brushColor('red')
    polygon([(x, 190), (x+40, 190), (x+90, 410), (x-50, 410), (x, 190)])
    line(x-7, 410, x-45, 550)
    line(x-45, 550, x-70, 550)
    line(x+45, 410, x+90, 550)
    line(x+90, 550, x+115, 550)
    brushColor('white')
    circle(x+20, 170, 40)
    line(x-10, 225, x-82, 330)
    line(x+50, 225, x+105, 330)
woman(380)
woman(765)

line(105,330,70,180)
penColor(200,2,2)
brushColor(200,2,2)
circle(45, 97, 25)
circle(85, 93, 25)
polygon([(70, 180), (20, 100), (110, 90), (70, 180)])


run()
