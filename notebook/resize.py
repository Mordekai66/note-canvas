from PySide6.QtCore import QRectF, Qt
from PySide6.QtGui import QBrush


class ResizeMixin:

    HANDLE = 8

    def init_resize(self):
        self.resizing = False
        self.handle = None
        self.setAcceptHoverEvents(True)

    def handles(self):
        r = self.rect_real()
        s = self.HANDLE

        return {
            "tl": QRectF(r.left() - s / 2, r.top() - s / 2, s, s),
            "tr": QRectF(r.right() - s / 2, r.top() - s / 2, s, s),
            "bl": QRectF(r.left() - s / 2, r.bottom() - s / 2, s, s),
            "br": QRectF(r.right() - s / 2, r.bottom() - s / 2, s, s),
        }

    def draw_handles(self, painter):
        if not self.isSelected():
            return

        painter.setBrush(QBrush(Qt.blue))

        for rect in self.handles().values():
            painter.drawRect(rect)

    def hoverMoveEvent(self, event):
        for _, rect in self.handles().items():
            if rect.contains(event.pos()):
                self.setCursor(Qt.SizeFDiagCursor)
                return

        self.setCursor(Qt.ArrowCursor)
        super().hoverMoveEvent(event)

    def mousePressEvent(self, event):
        for name, rect in self.handles().items():
            if rect.contains(event.pos()):
                self.resizing = True
                self.handle = name
                self.start_pos = event.pos()
                return

        self.setCursor(Qt.SizeAllCursor)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.resizing = False
        self.handle = None
        self.setCursor(Qt.ArrowCursor)
        super().mouseReleaseEvent(event)