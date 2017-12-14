import sys
from PyQt5 import QtWidgets,QtCore,QtGui,Qt

class ConfirmChange(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Confirmation")
        self.init_ui()

    def init_ui(self):
        #Create Widgets

        self.lConfirmation = QtWidgets.QLabel("Are you sure you want to leave this page?\nProgress will be lost once you leave.")
        self.lConfirmation.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')
        self.lConfirmation2 = QtWidgets.QLabel("Progress will be lost once you leave.")
        self.lConfirmation2.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.bConfirm = QtWidgets.QPushButton("Confirm")
        self.bConfirm.setStyleSheet('QPushButton {color: white;background-color: #47c468;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bConfirm.setFixedWidth(200)

        self.bBack = QtWidgets.QPushButton("Cancel")
        self.bBack.setStyleSheet('QPushButton {color: white;background-color: #ff0000;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 4px;}')
        self.bBack.setFixedWidth(80)
        
        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(13,1)

        self.addWidget(self.lConfirmation, 1, 2, 1, 3, QtCore.Qt.AlignCenter)
        #self.addWidget(self.lConfirmation2, 2, 2, 1, 3, QtCore.Qt.AlignCenter)   
        self.addWidget(self.bConfirm, 11, 2, 1, 2, QtCore.Qt.AlignCenter)
        self.addWidget(self.bBack, 11, 4, 1, 2, QtCore.Qt.AlignCenter)        

        
class WindowFrame(QtWidgets.QWidget):
    def __init__(self, layout):
        super().__init__()
        self.setWindowTitle("Confirmation")
        self.layout = layout(self)
        self.setLayout(self.layout)

class ConfirmChangeWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ConfirmChangeWindow, self).__init__(parent)
        self.resize(600,100)
        self.layout = WindowFrame(ConfirmChange)
        self.setWindowTitle("Confirmation")
        self.setCentralWidget(self.layout)