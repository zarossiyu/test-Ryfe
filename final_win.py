
#! Третье окно

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QLineEdit, QListWidget
from instr import *

class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.show()
    def set_appear(self):
        self.finalwin = QWidget()
        self.finalwin.setWindowTitle(txt_finalwin)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.result = QLabel(txt_index)
        self.result2 = QLabel(txt_workheart)
        self.line = QVBoxLayout()
        self.line.addWidget(self.result, alignment = Qt.AlignCenter)
        self.line.addWidget(self.result2, alignment = Qt.AlignCenter)
        self.setLayout(self.line)
app = QApplication([])
final_win = FinalWin()
app.exec_()