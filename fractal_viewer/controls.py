from PySide6.QtWidgets import QWidget, QHBoxLayout, QComboBox, QSlider, QLabel, QPushButton
from PySide6.QtCore import Qt
from .algorithms.fractal_utils import Fractals

class ControlsWidget(QWidget):
    """Controls for fractal selection and iteration depth."""

    def __init__(self):
        super().__init__()
        layout = QHBoxLayout(self)

        self.fractal_combo = QComboBox()
        self.fractal_combo.addItems([e.value for e in Fractals])


        self.iter_slider = QSlider(Qt.Horizontal)
        self.iter_slider.setMinimum(10)
        self.iter_slider.setMaximum(1000)
        self.iter_slider.setValue(14)

        self.iter_label = QLabel(f"Iterations: {self.iter_slider.value()}")
        self.iter_slider.valueChanged.connect(lambda v: self.iter_label.setText(f"Iterations: {v}"))

        self.startButton = QPushButton("Start")
        self.stopButton = QPushButton("Stop")
        self.resetButton = QPushButton("Reset")

        layout.addWidget(self.fractal_combo)
        layout.addWidget(self.iter_label)
        layout.addWidget(self.iter_slider)
        layout.addWidget(self.startButton)
        layout.addWidget(self.stopButton)
        layout.addWidget(self.resetButton)

