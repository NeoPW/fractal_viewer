from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from .canvas import FractalCanvas
from .controls import ControlsWidget
from .workers import FractalWorker
from PySide6.QtCore import QThreadPool
from .algorithms.fractal_utils import Fractals
from .geo_fractal_canvas import GeoFractalCanvas
from .algorithms.koch import Koch
from .fractal_factory import create_fractal

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fractal Explorer")

        central = QWidget()
        self.setCentralWidget(central)
        self.layout = QVBoxLayout(central)
        self.canvas: FractalCanvas = FractalCanvas()

        self.__add_ui_components__()
        self.__connect_buttons__()

    def start(self):
        self.canvas.startRendering()
        self.controls.startButton.setEnabled(False)
        self.controls.stopButton.setEnabled(True)
        self.controls.resetButton.setEnabled(False)
        self.controls.iter_slider.setEnabled(False)

    def stop(self):
        self.canvas.stopRendering()
        self.controls.startButton.setEnabled(True)
        self.controls.stopButton.setEnabled(False)
        self.controls.resetButton.setEnabled(True)
        self.controls.iter_slider.setEnabled(True)

    def reset(self):
        self.canvas.reset()

    def setDepth(self):
        self.canvas.setDepth(self.controls.iter_slider.value())

    def __add_ui_components__(self):
        self.controls = ControlsWidget()
        self.controls.fractal_combo.currentTextChanged.connect(self.__on_fractal_change__)
        self.canvas = None
        self.__on_fractal_change__(Fractals.KOCH.value)

        self.layout.addWidget(self.controls)
        self.layout.addWidget(self.canvas)

    def __on_fractal_change__(self, name: str):
        if self.canvas:
            self.canvas.setParent(None)
            self.canvas.deleteLater()

        self.canvas = create_fractal(name, self.controls.iter_slider.value())

        self.layout.addWidget(self.canvas)
        self.canvas.show()

    def __connect_buttons__(self):
        self.controls.startButton.clicked.connect(self.start)
        self.controls.stopButton.clicked.connect(self.stop)
        self.controls.resetButton.clicked.connect(self.reset)
        self.controls.startButton.setEnabled(True)
        self.controls.stopButton.setEnabled(False)
        self.controls.resetButton.setEnabled(True)

        self.controls.iter_slider.setEnabled(True)
        self.controls.iter_slider.valueChanged.connect(self.setDepth)