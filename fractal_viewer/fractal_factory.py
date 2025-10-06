

from .algorithms.koch import Koch
from .algorithms.sierpinski import Sierpinski
from .geo_fractal_canvas import GeoFractalCanvas
from .canvas import FractalCanvas
from .algorithms.fractal_utils import Fractals


def create_fractal(name: str, depth: int) -> FractalCanvas:
    match name:
        case Fractals.MANDELBROT.value:
            return GeoFractalCanvas()
        case Fractals.KOCH.value:
            return GeoFractalCanvas(Koch(), max_depth=depth)
        case Fractals.SIERPINSKI.value:
            return GeoFractalCanvas(Sierpinski(), max_depth=depth)
        case _:
            print("fractal not implemented")