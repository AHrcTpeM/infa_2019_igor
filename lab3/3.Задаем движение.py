from graph import *

canvasSize(400, 400)
brushColor(0, 0, 255)
rectangle(0,0,400,400)

x=200
y= 100
dx=0
dy=0
penColor('yellow')
brushColor('yellow')
obj=rectangle(x, y, x+20, y+20)

def keyPressed(event):
  global dx, dy
  if event.keycode == VK_LEFT:
    dx = -5
    dy = 0
  elif event.keycode == VK_RIGHT:
      dx = 5
      dy = 0
  elif event.keycode == VK_UP:
      dx = 0
      dy = -5
  elif event.keycode == VK_DOWN:
      dx = 0
      dy = 5
  elif event.keycode == VK_SPACE:
      dx = 0
      dy = 0
onKey(keyPressed)

def update():
    moveObjectBy(obj, dx, dy)

onTimer(update, 50)

run()