from graph import *

canvasSize(400, 400)
brushColor(0, 0, 255)
rectangle(0,0,400,400)

x=200
y= 100
penColor('yellow')
brushColor('yellow')
obj=rectangle(x, y, x+20, y+20)

def keyPressed(event):
  if event.keycode == VK_LEFT:
      moveObjectBy(obj, -5, 0)
  elif event.keycode == VK_RIGHT:
      moveObjectBy(obj, 5, 0)
  elif event.keycode == VK_UP:
      moveObjectBy(obj, 0, -5)
  elif event.keycode == VK_DOWN:
      moveObjectBy(obj, 0, 5)
  elif event.keycode == VK_ESCAPE:
      close()
onKey(keyPressed)

run()