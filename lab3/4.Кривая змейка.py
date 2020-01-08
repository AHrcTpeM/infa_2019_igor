from graph import *

canvasSize(400, 400)
brushColor(0, 0, 255)
rectangle(0,0,400,400)

x=200
y=50
a=10
N=10
dx=0
dy=0
snake = []
penColor("yellow")
brushColor("yellow")
for i in range(N):
  obj = rectangle(x+i*a, y, x+i*a+a, y+a)
  snake.append( obj )
  brushColor("green")

def moveSnake(xNew, yNew):
  global x, y
  for k in range(len(snake)-1,0,-1):
    newCoord = coords(snake[k-1])
    moveObjectTo(snake[k], newCoord[0],
                           newCoord[1])
  moveObjectTo(snake[0], xNew, yNew)
  x = xNew
  y = yNew

def keyPressed(event):
  global dx, dy
  if event.keycode == VK_LEFT:
    dx = -1
    dy = 0
  elif event.keycode == VK_RIGHT:
    dx = 1
    dy = 0
  elif event.keycode == VK_UP:
      dx = 0
      dy = -1
  elif event.keycode == VK_DOWN:
      dx = 0
      dy = 1
  elif event.keycode == VK_SPACE:
      dx = 0
      dy = 0
onKey(keyPressed)

def update():
  if dx or dy:
    moveSnake( x + dx*a , y + dy*a )
onTimer(update, 50)
run()