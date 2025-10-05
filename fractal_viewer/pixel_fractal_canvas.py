    # def start_render(self):
        # self.pool = QThreadPool.globalInstance()
    #     fractal_type = self.controls.fractal_combo.currentText()
    #     iterations = self.controls.iter_slider.value()
    #     width = max(320, self.canvas.width())
    #     height = max(240, self.canvas.height())

    #     self.controls.render_btn.setEnabled(False)
    #     self.controls.render_btn.setText("Rendering...")

    #     worker = FractalWorker(width, height, fractal_type, iterations)
    #     worker.signals.finished.connect(self._on_render_finished)
    #     self.pool.start(worker)

from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage

class PointBasedCanvas(QLabel):
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
