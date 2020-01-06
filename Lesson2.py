from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

print("Lesson2")

class MyWindow(QMainWindow):
    
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 600, 300)
        self.setWindowTitle("Tech With Sheldon")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.move(50, 50)
        self.label.setText("my first label")
        self.update()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()