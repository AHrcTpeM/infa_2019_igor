from graph import *

canvasSize(400, 400)
brushColor(0, 0, 255)
rectangle(0,0,400,400)

x=200
y= 100
penColor('yellow')
brushColor('yellow')
obj=rectangle(x, y, x+20, y+20)

def update():
    if penColor()=='yellow':
        moveObjectBy(obj, 5, 0)
    else:
        moveObjectBy(obj, -5, 0)
    if xCoord(obj) > 380:
        penColor('green')
    if xCoord(obj) < 1:
        penColor('yellow')

onTimer(update, 50)

def keyPressed(event):
  if event.keycode == 0x20:
    close()  # закрыть окно
onKey(keyPressed)


run()