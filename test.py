import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PenWidthDlg(QDialog):
    def __init__(self, parent=None):
        super(PenWidthDlg, self).__init__(parent)

        widthLabel = QLabel("Width")
        self.widthSpinBox = QSpinBox()

        widthLabel.setBuddy(self.widthSpinBox)
        self.widthSpinBox.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.widthSpinBox.setRange(0, 500)

        okButton = QPushButton("ok")
        cancelButton = QPushButton("cancel")

        layout = QGridLayout()
        layout.addWidget(widthLabel, 0, 0)
        layout.addWidget(self.widthSpinBox, 0, 1)
        layout.addWidget(okButton, 1, 0)
        layout.addWidget(cancelButton, 1, 1)

        self.setLayout(layout)

        self.setWindowTitle("Width Setting")

        okButton.clicked.connect(self.accept)
        cancelButton.clicked.connect(self.reject)


class myMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("draw")
        self.pix = QPixmap()
        self.lastPoint = QPoint()
        self.endPoint = QPoint()

        self.initData()
        self.initView()

        self.Menu = self.menuBar().addMenu("&Menu")

        self.ClearAction = QAction(QIcon("images/clear.png"), "Clear", self)
        self.ClearAction.triggered.connect(self.initView)
        self.Menu.addAction(self.ClearAction)

        self.changeWidth = QAction(QIcon("images/width.png"), "Width", self)
        self.changeWidth.triggered.connect(self.showWidthDialog)
        self.Menu.addAction(self.changeWidth)

        self.fileSaveAction = QAction(QIcon("images/filesave.png"), "&Save", self)
        self.fileSaveAction.setShortcut(QKeySequence.Save)
        self.fileSaveAction.triggered.connect(self.fileSaveAs)
        self.Menu.addAction(self.fileSaveAction)

    def initData(self):
        self.size = QSize(1120, 1120)
        self.pixmap = QPixmap(self.size)

        self.dirty = False
        self.filename = None
        self.recentFiles = []

        self.width = 100
        self.color = QColor("black")

        self.pen = QPen()
        self.pen.setColor(self.color)
        self.pen = QPen(Qt.SolidLine)
        self.pen.setWidth(self.width)

        self.painter = QPainter(self.pixmap)
        self.painter.setPen(self.pen)

        self._lastPos = QPoint(0, 0)
        self._currentPos = QPoint(0, 0)

        self.image = QImage()

    def initView(self):
        self.Clear()
        self.imageLabel = QLabel()
        self.imageLabel.setPixmap(self.pixmap)
        self.setCentralWidget(self.imageLabel)

    def Clear(self):
        self.pixmap.fill(Qt.white)
        self.update()
        self.dirty = False

    def mousePressEvent(self, event):
        pointX = event.globalX()
        pointY = event.globalY()

        self._currentPos = QPoint(pointX, pointY)
        self.dirty = True

        self._currentPos = event.pos()
        self._lastPos = self._currentPos

    def mouseMoveEvent(self, event):
        self._currentPos = event.pos()

        self.painter.begin(self.pixmap)
        self.painter.setPen(self.pen)
        self.painter.drawLine(self._lastPos, self._currentPos)

        self._lastPos = self._currentPos
        self.painter.end()

        self.update()
        self.imageLabel.setPixmap(self.pixmap)

    def updateWidth(self):
        self.pen.setWidth(self.width)
        self.painter.setPen(self.pen)

    def showWidthDialog(self):
        dialog = PenWidthDlg(self)
        dialog.widthSpinBox.setValue(self.width)

        if dialog.exec_():
            self.width = dialog.widthSpinBox.value()
            self.updateWidth()

    def fileSaveAs(self):
        savePath = QFileDialog.getSaveFileName(
            self,
            "Save Your Paint",
            ".\\",
            "*.png"
        )

        print(savePath)

        if savePath[0] == "":
            print("Save cancel")
            return

        image = self.pixmap

        print("save...")
        image = image.scaled(28, 28)
        image.save(savePath[0])


app = QApplication(sys.argv)

form = myMainWindow()

form.setMinimumSize(1120, 1120)
form.show()

app.exec_()