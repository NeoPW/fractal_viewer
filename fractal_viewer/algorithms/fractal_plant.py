from .lindemayer_system import LSystemDrawer, LSystem, Rule, Rules
from .fractal_utils import Point, Line
import math
import copy

class SavedPos():
    def __init__(self, p: Point, l: Line, a: int):
        self.pos = p
        self.incoming_line = l
        self.angle = a

class FractalPlant(LSystemDrawer):
    def __init__(self):
        super().__init__()
        self.stack: list[SavedPos] = []
        curr_pos = Point(0, 0)
        last_line = Line(curr_pos, curr_pos)
        self.saved_pos = SavedPos(curr_pos, last_line, 0)
        self.move_dist = 10
        self.lines = []

    def _initSystem(self) -> LSystem:
        r1 = Rule('X', 'F+[[X]-X]-F[-FX]+X')
        r2 = Rule('F', 'FF')
        start = '-X'
        return LSystem(start, Rules([r1, r2]))
    
    def setStartingPointFromSize(self, width: int, height: int):
        self.start_point = Point(5, height + 350)
        self.saved_pos.pos = self.start_point
    
    def step(self) -> list[str]:
        ret = self.ruleExecution(self.system.last[self.pos])
        self.pos += 1
        if self.pos == len(self.system.last):
            print("next iter step")
            self.pos = 0
            self.system.applyAllReplacementRules()
            curr_pos = Point(0, 0)
            last_line = Line(curr_pos, curr_pos)
            self.saved_pos = SavedPos(self.start_point, last_line, 0)
            self.lines = []

        return ret

    def ruleExecution(self, pre: str) -> list[str]:
        # print('rule exec handeling symbol: ', pre)
        match pre:
            case 'F':
                next_pos = SavedPos(None, None, None)

                next_pos.pos = Point(None, None)
                next_pos.pos.x = self.saved_pos.pos.x + self.move_dist * math.cos(math.radians(self.saved_pos.angle))
                next_pos.pos.y = self.saved_pos.pos.y + self.move_dist * math.sin(math.radians(self.saved_pos.angle))
                next_pos.incoming_line = Line(self.saved_pos.pos, next_pos.pos)
                next_pos.angle = self.saved_pos.angle
                
                self.saved_pos = next_pos
                self.lines.append(self.saved_pos.incoming_line)
            case 'X':
                pass
            case '+':
                self.saved_pos.angle += 25
            case '-':
                self.saved_pos.angle -= 25
            case '[':
                self.stack.append(copy.deepcopy(self.saved_pos))
            case ']':
                self.saved_pos = self.stack.pop()
        return self.lines
    
    # def forward(self) -> list[Line]
