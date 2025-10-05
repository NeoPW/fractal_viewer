from .fractal_utils import Line, Point
import math

class Koch():
    def __init__(self, start: list[Line] = None):
        self.last = start

    def step(self) ->  list[Line]:
        print("inside koch generator")
        current = []

        if self.last == None:
            current = [Line(Point(100, 200), Point(300, 200))]
            self.last = current
            return current

        for line in self.last:
            current = current + self.koch(line)
        
        self.last = current
        return current
  
    def koch(self, line: Line) -> list[Line]:
        koch_lines = []
        p1 : Point = Point(None, None)
        p1.x = math.floor(1 / 3 * line.b.x + 2 / 3 * line.a.x)
        p1.y = math.floor(1 / 3 * line.b.y + 2 / 3 * line.a.y)
        koch_lines.append(Line(line.a, p1))
        
        p2 : Point = Point(None, None)
        p2.x = math.floor(1 / 3 * line.a.x + 2 / 3 * line.b.x)
        p2.y = math.floor(1 / 3 * line.a.y + 2 / 3 * line.b.y)
        koch_lines.append(Line(p2, line.b))

        c : Point = Point(None, None)
        c.x = math.floor((p2.x + p1.x + math.sqrt(3) * (p2.y - p1.y)) / 2)
        c.y = math.floor((p2.y + p1.y - math.sqrt(3) * (p2.x - p1.x)) / 2)
        koch_lines.append(Line(p1, c))
        koch_lines.append(Line(c, p2))

        return koch_lines
