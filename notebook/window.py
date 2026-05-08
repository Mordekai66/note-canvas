from PySide6.QtWidgets import (
    QMainWindow,
    QGraphicsScene,
    QFileDialog,
    QToolBar,
    QDockWidget,
    QWidget,
    QFormLayout,
    QSpinBox,
    QTextEdit
)
from PySide6.QtGui import (
    QAction,
    QColor,
    QPen,
    QBrush,
    QPixmap,
    QImage,
    QPainter,
    QPdfWriter,
    QPageSize,
    QKeySequence, 
    QShortcut
)

from PySide6.QtCore import Qt

from notebook.view import NotebookView
from notebook.items import TextItem, ImageItem


class DigitalNotebook(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Digital Notebook")
        self.resize(1400, 900)

        self.current_item = None

        self.scene = QGraphicsScene()
        self.scene.setSceneRect(0, 0, 800, 1000)
        self.scene.setBackgroundBrush(QColor("#cccccc"))

        self.view = NotebookView(self.scene)

        self.setCentralWidget(self.view)

        self.draw_page()
        self.create_toolbar()
        self.create_sidebar()
        self.create_shortcuts()

        self.scene.selectionChanged.connect(self.update_sidebar)

    def draw_page(self):
        self.scene.addRect(
            0,
            0,
            800,
            1000,
            QPen(Qt.black),
            QBrush(Qt.white)
        )

        pen = QPen(QColor("#dddddd"))

        for y in range(0, 1000, 25):
            self.scene.addLine(0, y, 800, y, pen)

    def create_toolbar(self):
        toolbar = QToolBar()

        self.addToolBar(toolbar)

        actions = [
            ("Add Text", self.add_text),
            ("Add Image", self.add_image),
            ("Save Image", self.save_image),
            ("Save PDF", self.save_pdf),
            ("Delete", self.delete_selected),
        ]

        for name, func in actions:
            action = QAction(name, self)
            action.triggered.connect(func)
            toolbar.addAction(action)

    def create_sidebar(self):
        dock = QDockWidget("Properties", self)

        widget = QWidget()

        layout = QFormLayout()

        self.x_spin = QSpinBox()
        self.y_spin = QSpinBox()
        self.w_spin = QSpinBox()
        self.h_spin = QSpinBox()

        self.text_edit = QTextEdit()

        for spin in [
            self.x_spin,
            self.y_spin,
            self.w_spin,
            self.h_spin
        ]:
            spin.setRange(-5000, 5000)

        layout.addRow("X", self.x_spin)
        layout.addRow("Y", self.y_spin)
        layout.addRow("Width", self.w_spin)
        layout.addRow("Height", self.h_spin)
        layout.addRow("Text", self.text_edit)

        widget.setLayout(layout)

        dock.setWidget(widget)

        self.addDockWidget(Qt.RightDockWidgetArea, dock)

        self.x_spin.valueChanged.connect(self.update_position)
        self.y_spin.valueChanged.connect(self.update_position)

        self.w_spin.valueChanged.connect(self.update_size)
        self.h_spin.valueChanged.connect(self.update_size)

        self.text_edit.textChanged.connect(self.update_text)

    def create_shortcuts(self):
        QShortcut(
            QKeySequence("Ctrl+T"),
            self,
            activated=self.add_text
        )

        QShortcut(
            QKeySequence("Ctrl+I"),
            self,
            activated=self.add_image
        )

        QShortcut(
            QKeySequence("Ctrl+S"),
            self,
            activated=self.save_image
        )

        QShortcut(
            QKeySequence("Ctrl+Shift+S"),
            self,
            activated=self.save_pdf
        )

        QShortcut(
            QKeySequence(Qt.Key_Delete),
            self,
            activated=self.delete_selected
        )

    def add_text(self):
        item = TextItem()

        item.setPos(100, 100)

        self.scene.addItem(item)

    def add_image(self):
        file, _ = QFileDialog.getOpenFileName(
            self,
            "Open Image",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )

        if not file:
            return

        pixmap = QPixmap(file)

        pixmap = pixmap.scaled(
            250,
            250,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        item = ImageItem(pixmap)

        item.setPos(100, 100)

        self.scene.addItem(item)

    def update_sidebar(self):
        items = self.scene.selectedItems()

        if not items:
            self.current_item = None
            return

        item = items[0]

        self.current_item = item

        self.blockSignals(True)

        self.x_spin.setValue(int(item.x()))
        self.y_spin.setValue(int(item.y()))

        rect = item.rect_real()

        self.w_spin.setValue(int(rect.width()))
        self.h_spin.setValue(int(rect.height()))

        if isinstance(item, TextItem):
            self.text_edit.setHtml(item.toHtml())
        else:
            self.text_edit.clear()

        self.blockSignals(False)

    def blockSignals(self, value):
        for w in [
            self.x_spin,
            self.y_spin,
            self.w_spin,
            self.h_spin,
            self.text_edit
        ]:
            w.blockSignals(value)

    def update_position(self):
        if not self.current_item:
            return

        self.current_item.setPos(
            self.x_spin.value(),
            self.y_spin.value()
        )

    def update_size(self):
        if not self.current_item:
            return

        width = self.w_spin.value()
        height = self.h_spin.value()

        if isinstance(self.current_item, ImageItem):
            scaled = self.current_item.original.scaled(
                width,
                height,
                Qt.IgnoreAspectRatio,
                Qt.SmoothTransformation
            )

            self.current_item.setPixmap(scaled)

        elif isinstance(self.current_item, TextItem):
            self.current_item.setTextWidth(width)

    def update_text(self):
        if isinstance(self.current_item, TextItem):
            self.current_item.setHtml(
                self.text_edit.toHtml()
            )

    def delete_selected(self):
        for item in self.scene.selectedItems():
            self.scene.removeItem(item)

    def save_image(self):
        file, _ = QFileDialog.getSaveFileName(
            self,
            "Save Image",
            "image",
            "PNG (*.png)"
        )

        if not file:
            return

        rect = self.scene.sceneRect()

        image = QImage(
            rect.width(),
            rect.height(),
            QImage.Format_ARGB32
        )

        image.fill(Qt.white)

        painter = QPainter(image)

        self.scene.render(painter)

        painter.end()

        image.save(file)

    def save_pdf(self):
        file, _ = QFileDialog.getSaveFileName(
            self,
            "Save PDF",
            "image",
            "PDF (*.pdf)"
        )

        if not file:
            return

        pdf = QPdfWriter(file)

        pdf.setPageSize(QPageSize(QPageSize.A4))

        painter = QPainter(pdf)

        self.scene.render(painter)

        painter.end()