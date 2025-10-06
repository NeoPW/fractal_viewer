import math
from fractal_viewer.algorithms.fractal_utils import Line, Point

class Sierpinski:
    def __init__(self, start: list[Line] = None):
        self.start = start
        self.last = None
        self.stepCount = 0
        self.countItems = 3

    def setStartingPointFromSize(self, width: int, height: int):
        A : Point = Point(10, height - 100)
        B : Point = Point(height - 90, height - 100)
        C : Point = Point(None, None)
        C.x = math.floor((B.x + A.x + math.sqrt(3) * (B.y - A.y)) / 2)
        C.y = math.floor((B.y + A.y - math.sqrt(3) * (B.x - A.x)) / 2 )  
        
        # c.x = math.floor((p2.x + p1.x + math.sqrt(3) * (p2.y - p1.y)) / 2)
        # c.y = math.floor((p2.y + p1.y - math.sqrt(3) * (p2.x - p1.x)) / 2)       
        self.start = [Line(A, B), Line(B, C), Line(C, A)]

    def step(self) ->  list[Line]:
        current = []

        if self.last == None:
            self.last = self.start
            return self.start
        
        for i in range(0, len(self.last), 3):
            current = current + self.sierpinski((self.last[i], self.last[i + 1], self.last[i + 2]))

        self.countItems += 3 ** self.stepCount
        self.stepCount += 1
        self.last = current
        return current
  
    def sierpinski(self, triangle: tuple[Line, Line, Line]) -> list[Line]:
        a = Point(None, None)
        a.x = triangle[0].a.x + (triangle[0].b.x - triangle[0].a.x) / 2
        a.y = triangle[0].a.y + (triangle[0].b.y - triangle[0].a.y) / 2

        b = Point(None, None)
        b.x = triangle[1].a.x + (triangle[1].b.x - triangle[1].a.x) / 2
        b.y = triangle[1].a.y + (triangle[1].b.y - triangle[1].a.y) / 2

        c = Point(None, None)
        c.x = triangle[2].a.x + (triangle[2].b.x - triangle[2].a.x) / 2
        c.y = triangle[2].a.y + (triangle[2].b.y - triangle[2].a.y) / 2

        return [Line(triangle[0].a, a), Line(a, c), Line(c, triangle[0].a), Line(triangle[0].b, a), Line(a, b), Line(b, triangle[0].b), Line(triangle[2].a, c), Line(c, b), Line(b, triangle[2].a)]
