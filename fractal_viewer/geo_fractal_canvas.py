from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QPen
from .canvas import FractalCanvas

class GeoFractalCanvas(FractalCanvas):
    def __init__(self, generator=None, max_depth=5, step_delay=1000):
        
        super().__init__()
        self.setGenerator(generator)
        self.max_depth = max_depth
        self.step_delay = step_delay
        self.current_step = 0
        self.lines = []

        self.color = Qt.GlobalColor.white

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._animate)

    def setGenerator(self, generator):
        self.generator = generator
        self.generator.setStartingPointFromSize(self.size().width(), self.size().height())

    def setDepth(self, depth):
        self.max_depth = depth

    def startRendering(self):
        self.timer.start(self.step_delay)
        print(self.size().height())
        print(self.size().width())

    def stopRendering(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.current_step = 0
        # reset generator

    def _animate(self):

        if self.current_step < self.max_depth:
            self.current_step += 1
            print(self.current_step)
            self.lines = self.generator.step()
            self.update()
        else:
            self.timer.stop()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(self.color, 2))

        for line in self.lines:
            painter.drawLine(line.a.x, line.a.y, line.b.x, line.b.y)