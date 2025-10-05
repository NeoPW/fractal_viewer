# marks the folder as a package and exposes top-level classes
from .main_window import MainWindow
from .canvas import FractalCanvas
from .controls import ControlsWidget

__all__ = ["MainWindow", "FractalCanvas", "ControlsWidget"]
