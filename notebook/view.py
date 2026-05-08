from PySide6.QtWidgets import QGraphicsView, QApplication
from PySide6.QtGui import QPainter, QPixmap, QKeySequence
from PySide6.QtCore import Qt

from notebook.items import TextItem, ImageItem


class NotebookView(QGraphicsView):

    def __init__(self, scene):
        super().__init__(scene)

        self.setRenderHint(QPainter.Antialiasing)
        self.setDragMode(QGraphicsView.NoDrag)

    def keyPressEvent(self, event):

        if event.matches(QKeySequence.Paste):
            self.paste_from_clipboard()
            return

        super().keyPressEvent(event)

    def paste_from_clipboard(self):
        clipboard = QApplication.clipboard()

        mime = clipboard.mimeData()

        # صورة
        if mime.hasImage():
            image = clipboard.image()

            pixmap = QPixmap.fromImage(image)

            item = ImageItem(
                pixmap.scaled(
                    250,
                    250,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

            item.setPos(100, 100)

            self.scene().addItem(item)

            return

        # نص
        if mime.hasText():
            text = clipboard.text().strip()

            if not text:
                return

            item = TextItem()

            item.setPlainText(text)

            item.setPos(100, 100)

            self.scene().addItem(item)