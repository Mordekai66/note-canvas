from PySide6.QtWidgets import QGraphicsTextItem, QGraphicsPixmapItem, QGraphicsItem
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt

from notebook.resize import ResizeMixin


class TextItem(ResizeMixin, QGraphicsTextItem):

    def __init__(self):
        super().__init__()

        self.setHtml("<b>Double Click To Edit</b>")
        self.setFont(QFont("Arial", 14))
        self.setDefaultTextColor(QColor("black"))
        self.setTextWidth(250)

        self.setTextInteractionFlags(Qt.NoTextInteraction)

        self.setFlags(
            QGraphicsItem.ItemIsMovable |
            QGraphicsItem.ItemIsSelectable |
            QGraphicsItem.ItemIsFocusable
        )

        self.init_resize()

    def rect_real(self):
        return super().boundingRect()

    def boundingRect(self):
        r = super().boundingRect()
        return r.adjusted(-10, -10, 10, 10)

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        self.draw_handles(painter)

    def mouseDoubleClickEvent(self, event):
        self.setTextInteractionFlags(Qt.TextEditorInteraction)
        self.setFocus()
        super().mouseDoubleClickEvent(event)

    def focusOutEvent(self, event):
        self.setTextInteractionFlags(Qt.NoTextInteraction)
        super().focusOutEvent(event)

    def mouseMoveEvent(self, event):
        scene_rect = self.scene().sceneRect()

        if self.resizing:
            diff = event.pos() - self.start_pos

            width = max(80, self.textWidth() + diff.x())

            max_width = scene_rect.right() - self.pos().x()

            width = min(width, max_width)

            self.setTextWidth(width)

            self.start_pos = event.pos()

            self.update()
            return

        super().mouseMoveEvent(event)

        rect = self.rect_real()

        x = min(max(self.x(), scene_rect.left()),
                scene_rect.right() - rect.width())

        y = min(max(self.y(), scene_rect.top()),
                scene_rect.bottom() - rect.height())

        self.setPos(x, y)


class ImageItem(ResizeMixin, QGraphicsPixmapItem):

    def __init__(self, pixmap):
        super().__init__(pixmap)

        self.original = pixmap

        self.setFlags(
            QGraphicsItem.ItemIsMovable |
            QGraphicsItem.ItemIsSelectable
        )

        self.init_resize()

    def rect_real(self):
        return super().boundingRect()

    def boundingRect(self):
        r = super().boundingRect()
        return r.adjusted(-10, -10, 10, 10)

    def paint(self, painter, option, widget):
        super().paint(painter, option, widget)
        self.draw_handles(painter)

    def mouseMoveEvent(self, event):
        scene_rect = self.scene().sceneRect()

        if self.resizing:
            rect = self.rect_real()
            diff = event.pos() - self.start_pos

            width = max(40, rect.width() + diff.x())
            height = max(40, rect.height() + diff.y())

            max_width = scene_rect.right() - self.pos().x()
            max_height = scene_rect.bottom() - self.pos().y()

            width = min(width, max_width)
            height = min(height, max_height)

            scaled = self.original.scaled(
                width,
                height,
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )

            self.setPixmap(scaled)

            self.start_pos = event.pos()

            self.update()
            return

        super().mouseMoveEvent(event)

        rect = self.rect_real()

        x = min(max(self.x(), scene_rect.left()),
                scene_rect.right() - rect.width())

        y = min(max(self.y(), scene_rect.top()),
                scene_rect.bottom() - rect.height())

        self.setPos(x, y)