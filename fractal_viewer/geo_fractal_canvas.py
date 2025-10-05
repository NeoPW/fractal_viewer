from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QPainter, QPen

class GeoFractalCanvas(QWidget):
    def __init__(self, generator=None, max_depth=5, step_delay=1000):
        
        super().__init__()
        self.generator = generator
        self.max_depth = max_depth
        self.step_delay = step_delay
        self.current_step = 0
        self.lines = []

        self.color = Qt.GlobalColor.blue

        self.timer = QTimer(self)
        self.timer.timeout.connect(self._animate)
        self.timer.start(self.step_delay)

    def setGenerator(self, generator):
        self.generator = generator

    def _animate(self):

        if self.current_step < self.max_depth:
            self.current_step += 1
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