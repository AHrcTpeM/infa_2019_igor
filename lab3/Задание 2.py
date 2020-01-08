from graph import *

<<<<<<< HEAD
windowSize(600, 600)
brushColor(200, 100, 100)
rectangle(0,0,600,300)
brushColor(100, 200, 100)
rectangle(0,300,600,600)

brushColor('grey')
oval(140,190,260,410)
line(173,400,135,550)
line(135,550,110,550)
line(225,400,270,550)
line(270,550,295,550)
brushColor('white')
circle(200,170,40)
line(158,225,100,330)
line(244,225,298,330)

brushColor('red')
polygon([(380,190),(420,190),(470,410), (320,410), (380,190)])
line(173+200,410,135+200,550)
line(135+200,550,110+200,550)
line(225+200,410,270+200,550)
line(270+200,550,295+200,550)
brushColor('white')
circle(200+200,170,40)
line(370,225,298,330)
line(430,225,285+200,330)
=======
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

>>>>>>> 00f1edf407f45439c32fb2755cd82ee10c81fb01

run()
