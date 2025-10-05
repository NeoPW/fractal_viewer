from .fractal_utils import Line, Point
import math

class Koch():
    def __init__(self, start: list[Line] = None):
        self.start = start
        self.last = None
        self.ROT_ANGLE = math.radians(-60)

    def setStartingPointFromSize(self, width: int, height: int):
        self.start = [Line(Point(0, height-100), Point(width, height-100))]

    def step(self) ->  list[Line]:
        current = []

        if self.last == None:
            self.last = self.start
            return self.start

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
        c.x = p1.x + (p2.x - p1.x) * math.cos(self.ROT_ANGLE) - (p2.y - p1.y) * math.sin(self.ROT_ANGLE)
        c.y = p1.y + (p2.x - p1.x) * math.sin(self.ROT_ANGLE) + (p2.y - p1.y) * math.cos(self.ROT_ANGLE)
        koch_lines.append(Line(p1, c))
        koch_lines.append(Line(c, p2))

        return koch_lines
