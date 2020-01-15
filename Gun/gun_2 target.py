from random import randrange as rnd, choice
import tkinter as tk
import math
import time


# print (dir(math))

class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canvas.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        if self.x > 800 or self.y > 600 or self.y < 0:
            canvas.delete(self.id)
            balls.remove(self)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        for t in targ:
            r = ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2) ** 0.5
            if r < self.r + t.r:
                canvas.coords(self.id, -10, -10, -10, -10)
                # t1.hit()
                # t1.new_target()
                return True


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canvas.create_line(20, 450, 50, 420, width=7, fill='black')  # FIXME: don't know how to set it...

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        x = 20 + max(self.f2_power, 20) * math.cos(self.an)
        y = 450 + max(self.f2_power, 20) * math.sin(self.an)
        new_ball = ball(x, y)
        new_ball.r += 5
        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y - 450) / (event.x - 20))
        if self.f2_on:
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')
        canvas.coords(self.id, 20, 450,
                      20 + max(self.f2_power, 20) * math.cos(self.an),
                      450 + max(self.f2_power, 20) * math.sin(self.an)
                      )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canvas.itemconfig(self.id, fill='orange')
        else:
            canvas.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.live = 1
        self.vx = 0
        self.vy = 4
        # FIXME: don't work!!! How to call this functions when object is created?
        self.id = canvas.create_oval(0, 0, 0, 0)
        self.id_points = canvas.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(300, 550)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canvas.coords(self.id, x - r, y - r, x + r, y + r)
        canvas.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canvas.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canvas.itemconfig(self.id_points, text=self.points)
        self.x = -100
        self.y = -100

    def move(self):
        self.x += self.vx
        self.y -= self.vy
        if self.y - self.r <= 0 or self.y + self.r >= 600:
            self.vy = -self.vy
        canvas.coords(self.id, self.x - self.r, self.y - self.r,
                      self.x + self.r, self.y + self.r)


def new_game(event=''):
    global gun, t1, screen1, balls, bullet, targ
    targ = [target() for i in range(2)]
    canvas.itemconfig(screen1, text='')
    bullet = 0
    balls = []
    canvas.bind('<Button-1>', g1.fire2_start)
    canvas.bind('<ButtonRelease-1>', g1.fire2_end)
    canvas.bind('<Motion>', g1.targetting)

    for t in targ:
        t.live = 1
    while len(targ) != 0 or balls:
        for t in targ:
            t.move()
        for b in balls:
            b.move()
            for t in targ:
                if b.hittest(t) and t.live:
                    t.live = 0
                    t.hit()
                    targ.remove(t)
        if len(targ) == 0:
            canvas.bind('<Button-1>', '')
            canvas.bind('<ButtonRelease-1>', '')
            canvas.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canvas.update()
        time.sleep(0.03)
        g1.targetting()
        g1.power_up()
    canvas.delete(g1)
    print(1)
    canvas.bind('<Button-3>', new_game)
    # root.after(750, new_game)


root = tk.Tk()
fr = tk.Frame(root)
root.geometry('800x600')
canvas = tk.Canvas(root, bg='white')
canvas.pack(fill=tk.BOTH, expand=1)

screen1 = canvas.create_text(400, 300, text='', font='28')
g1 = gun()
bullet = 0
balls = []

new_game()

tk.mainloop()
