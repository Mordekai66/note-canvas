import sys
from PySide6.QtWidgets import QApplication

from notebook.window import DigitalNotebook


def main():
    app = QApplication(sys.argv)

    window = DigitalNotebook()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()