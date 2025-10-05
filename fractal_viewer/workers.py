from PySide6.QtCore import QRunnable, QObject, Signal
from PySide6.QtGui import QImage
from .algorithms import mandelbrot
from .algorithms.fractal_utils import Fractals

class RenderSignals(QObject):
    finished = Signal(QImage)

class FractalWorker(QRunnable):
    """Compute a fractal image off the main thread."""

    def __init__(self, width, height, fractal_type, max_iter):
        super().__init__()
        self.width = width
        self.height = height
        self.fractal_type = fractal_type
        self.max_iter = max_iter
        self.signals = RenderSignals()

    def run(self):
        if self.fractal_type == Fractals.MANDELBROT.value:
            qimg = mandelbrot.compute(self.width, self.height, self.max_iter)
        else:
            # placeholder: Mandelbrot for now
            qimg = mandelbrot.compute(self.width, self.height, self.max_iter)

        self.signals.finished.emit(qimg)
