import modulefive
from time import time, sleep
from abc import abstractmethod
import random
window = modulefive.Window(0, 0, 405, 405)
fps = 10
figures = []

class Shape(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self): ...

    @abstractmethod
    def top(self) -> float: ...

    @abstractmethod
    def bottom(self) -> float: ...

    @abstractmethod
    def left(self) -> float: ...

    @abstractmethod
    def right(self) -> float: ...

class Rectangle(Shape):  # прямоугольник
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def draw(self):
        window.draw_rectangle((self.x, self.y), (self.width, self.height), color='black')

    def top(self) -> float:
        return self.y

    def bottom(self) -> float:
        return self.y + self.height

    def left(self) -> float:
        return self.x

    def right(self) -> float:
        return self.x + self.width



class Square(Rectangle):  # квадрат
    def __init__(self, x, y, size):
        self.size = size
        self.speed_horisontal = random.randint(1, 10) * -1
        self.speed_vertical = random.randint(1, 10) * -1
        super().__init__(x, y, self.size, self.size)



    def draw(self):
        window.draw_rectangle((self.x, self.y), (self.size, self.size), color='black')


class Circle(Shape):  # круг
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius
        self.speed_horisontal = random.randint(1, 10) * -1
        self.speed_vertical = random.randint(1, 10) * -1

    def draw(self):
        window.draw_ellipse((self.x,self.y), (self.radius,self.radius), color='black')

    def top(self) -> float:
        return self.y

    def bottom(self) -> float:
        return self.y + self.radius

    def left(self) -> float:
        return self.x

    def right(self) -> float:
        return self.x + self.radius


# class Triangle(Shape):  # равносторонний треугольник
#     def __init__(self, x, y, height):
#         super().__init__(x, y)
#         self.height = height
#
#     def draw(self):
#         window.draw_polygon(, color='black')
#
#     def top(self) -> float:
#         return self.y
#
#     def bottom(self) -> float:
#         return self.y + self.height
#
#     def left(self) -> float:
#         return self.x
#
#     def right(self) -> float:
#         return self.x + self.height




# n = int(input('введите количество фигур\n'))
n = 5

for i in range(n):
    figures.append(Square(random.randint(0,400), random.randint(0,400), 20))

while not window.close():
    start = time()
    window.clear()

    for figure in figures:
        if figure.right() >= window.width:
            figure.speed_horisontal = figure.speed_horisontal * -1
        elif figure.left() <= 0:
            figure.speed_horisontal = figure.speed_horisontal * -1

        if figure.bottom() >= window.height:
            figure.speed_vertical = figure.speed_vertical * -1
        elif figure.top() <= 0:
            figure.speed_vertical = figure.speed_vertical * -1


        figure.x += figure.speed_horisontal
        figure.y += figure.speed_vertical

        figure.draw()

    window.update()
    pause = 1/fps - (time() - start)
    if pause > 0:
        sleep(pause)