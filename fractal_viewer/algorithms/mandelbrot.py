import numpy as np
from PySide6.QtGui import QImage

def compute(width, height, max_iter):

    rgb = np.zeros((height, width, 3), dtype=np.uint8)

    bytes_per_line = 3 * width
    return QImage(rgb.data, width, height, bytes_per_line, QImage.Format_RGB888).copy()
