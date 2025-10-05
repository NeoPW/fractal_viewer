from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage

class FractalCanvas(QLabel):
    """A QLabel that displays the fractal image."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(Qt.AlignCenter)
        self.setMinimumSize(640, 480)
        self.setText("Press Render to compute fractal")

    def set_image(self, qimage: QImage):
        pix = QPixmap.fromImage(qimage)
        self.setPixmap(pix.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def resizeEvent(self, event):
        if self.pixmap():
            self.setPixmap(
                self.pixmap().scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
        super().resizeEvent(event)
