import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from qt_material import apply_stylesheet
from fractal_viewer import MainWindow

if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app = QApplication(sys.argv)

    apply_stylesheet(app, theme="dark_teal.xml")

    window = MainWindow()
    window.resize(1280, 720)
    window.show()

    sys.exit(app.exec())
