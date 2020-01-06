from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

print("Lesson1")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 600, 300)
    win.setWindowTitle("Tech With Sheldon")

    label = QtWidgets.QLabel(win)
    label.setText("my first label")
    label.move(50, 50)
    win.show()
    sys.exit(app.exec_())


window()