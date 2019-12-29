from graph import *

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

man(100)
man(300)

# brushColor('green')
# oval(140,190,260,410)
# line(173,400,135,550)
# line(135,550,110,550)
# line(225,400,270,550)
# line(270,550,295,550)
# brushColor('white')
# circle(200,170,40)
# line(158,225,100,330)
# line(244,225,298,330)

run()

# brushColor('grey')
# oval(140,190,260,410)
# line(173,400,135,550)
# line(135,550,110,550)
# line(225,400,270,550)
# line(270,550,295,550)
# brushColor('white')
# circle(200,170,40)
# line(158,225,100,330)
# line(244,225,298,330)

# brushColor('red')
# polygon([(380,190),(420,190),(470,410), (330,410), (380,190)])
# line(173+200,410,135+200,550)
# line(135+200,550,110+200,550)
# line(225+200,410,270+200,550)
# line(270+200,550,295+200,550)
# brushColor('white')
# circle(200+200,170,40)
# line(370,225,298,330)
# line(430,225,285+200,330)

def update():
    if penColor()=='yellow':
        moveObjectBy(obj, 5, 0)
    else:
        moveObjectBy(obj, -5, 0)
    if xCoord(obj) > 380:
        penColor('green')
    if xCoord(obj) < 1:
        penColor('yellow')