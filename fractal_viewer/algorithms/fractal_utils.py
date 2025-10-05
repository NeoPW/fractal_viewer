from enum import Enum

class Fractals(Enum):
    MANDELBROT = 'Mandelbrot'
    KOCH = 'Koch'
    JULIA = 'Julia'

class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line():
    def __init__(self, a: Point, b: Point):

        # order points left to right
        if(a.x < b.x or (a.x == b.x and a.y < b.y) ):
            self.a = a
            self.b = b
        else:
            self.a = b
            self.b = a