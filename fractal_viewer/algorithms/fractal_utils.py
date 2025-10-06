from enum import Enum

class Fractals(Enum):
    MANDELBROT = 'Mandelbrot'
    KOCH = 'Koch'
    JULIA = 'Julia'
    SIERPINSKI = 'Sierpinski'

class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # def __add__(self, other):
    #     return Point(self.x + other.x, self.y + other.y)

    # def __sub__(self, other):
    #     return Point(self.x - other.x, self.y - other.y)
    
    # def __mul__(self, other):
    #     return Point(self.x * other, self.y * other)
    
    # def __truediv__(self, other: int):
    #     return Point(self.x / other, self.y / other)

class Line():
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    # def __truediv__(self, other: int):
    #     return (self.b - self.a) * other

# class Triangle():
#     def __init__(self, A: Point, B: Point, C: Point):
#         self.A = A
#         self.B = B
#         self.C = C
#         self.a = Line(B, C)
#         self.b = Line(C, A)
#         self.c = Line(A, B)

#     def triangle_from_lines(self, a: Line, b: Line, c: Line):
#         self.a = a
#         self.b = b
#         self.c = c
#         self.A = c.a
#         self.B = c.b
#         self.C = a.a