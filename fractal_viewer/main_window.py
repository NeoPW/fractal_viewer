from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from .canvas import FractalCanvas
from .controls import ControlsWidget
from .workers import FractalWorker
from PySide6.QtCore import QThreadPool
from .algorithms.fractal_utils import Fractals

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fractal Explorer")

        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        self.__add_ui_components__(self, layout)

        self.pool = QThreadPool.globalInstance()

        self.__connect_buttons__()

    def start_render(self):
        fractal_type = self.controls.fractal_combo.currentText()
        iterations = self.controls.iter_slider.value()
        width = max(320, self.canvas.width())
        height = max(240, self.canvas.height())

        self.controls.render_btn.setEnabled(False)
        self.controls.render_btn.setText("Rendering...")

        worker = FractalWorker(width, height, fractal_type, iterations)
        worker.signals.finished.connect(self._on_render_finished)
        self.pool.start(worker)

    def _on_render_finished(self, qimage):
        self.canvas.set_image(qimage)
        self.controls.render_btn.setEnabled(True)
        self.controls.render_btn.setText("Render")

    def __add_ui_components__(self, layout: QVBoxLayout):
        self.controls = ControlsWidget()
        self.canvas = FractalCanvas()

        layout.addWidget(self.controls)
        layout.addWidget(self.canvas)

    def __connect_buttons__(self):
        self.controls.render_btn.clicked.connect(self.start_render)
