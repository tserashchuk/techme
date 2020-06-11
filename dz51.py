import modulefive
from time import time, sleep
from abc import abstractmethod
import random
window = modulefive.Window(0, 0, 405, 405)
fps = 60


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
        super().__init__(x, y, self.size, self.size)



    def draw(self):
        window.draw_rectangle((self.x, self.y), (self.size, self.size), color='black')


class Circle(Shape):  # круг
    def __init__(self, x, y, radius):
        super().__init__(x,y)
        self.radius = radius

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


class Triangle(Shape):  # равносторонний треугольник
    def __init__(self, x, y, height):
        super().__init__(x, y)
        self.height = height

    def draw(self):
        window.draw_polygon((self.x, self.y), color='black')

    def top(self) -> float:
        return self.y

    def bottom(self) -> float:
        return self.y + self.height

    def left(self) -> float:
        return self.x

    def right(self) -> float:
        return self.x + self.height

figure = Triangle(0,0,120)
speed_horisontal = random.randint(1,10) * -1
speed_vertical = random.randint(1,10) * -1
while not window.close():
    start = time()
    window.clear()


    if figure.right() >= window.width:
        speed_horisontal = speed_horisontal * -1
    elif figure.left() == 0:
        speed_horisontal = speed_horisontal * -1

    if figure.bottom() >= window.height:
        speed_vertical = speed_vertical * -1
    elif figure.top() == 0:
        speed_vertical = speed_vertical * -1


    figure.x += speed_horisontal
    figure.y += speed_vertical

    a = figure.right()
    b = figure.left()

    figure.draw()

    window.update()
    pause = 1/fps - (time() - start)
    if pause > 0:
        sleep(pause)