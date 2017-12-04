import sys
import datetime
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QHeaderView


class LoginView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.init_ui()   

    def init_ui(self):
        
        self.logoLabel = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap('test4.png')
        self.logoLabel.setPixmap(pixmap.scaled(480, 480, QtCore.Qt.KeepAspectRatio))
        
        #textboxSize = 350
        labelStyle = 'QLabel { font-size: 12pt; padding: 10px; font-weight: bold; font-family: FreeMono; }'
        textboxStyle = 'QLineEdit { font-size: 12pt; padding: 7px; border-radius:5px;}'
        
        self.lUsername = QtWidgets.QLabel("Username:")
        #self.lName.setAlignment(QtCore.Qt.AlignRight)
        self.lUsername.setStyleSheet(labelStyle)
        self.tUsername = QtWidgets.QLineEdit(self.frame)
        self.tUsername.setStyleSheet(textboxStyle)
        self.tUsername.setPlaceholderText("Username")
        #self.tName.textChanged.connect(self.preview_items)
        #self.tUsername.setFixedWidth(textboxSize)
        
        self.lPassword = QtWidgets.QLabel("Password:")
        #self.lId.setAlignment(QtCore.Qt.AlignRight)
        self.lPassword.setStyleSheet(labelStyle)
        self.tPassword = QtWidgets.QLineEdit(self.frame)
        self.tPassword.setStyleSheet(textboxStyle)
        self.tPassword.setPlaceholderText("Password")
        self.tPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        #self.tId.textChanged.connect(self.preview_items)
        #self.tPassword.setFixedWidth(textboxSize)
        
        
        self.bLogin = QtWidgets.QPushButton("LOG IN")
        self.bLogin.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; background-color: #5cb85c; border-color: #4cae4c;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #4baa4b; border-color: #409140;}""")
        
        self.setColumnStretch(11,1)
        self.setColumnStretch(0,1)
        self.setRowStretch(11,1)
        

        self.addWidget(self.logoLabel, 2, 1, 1, 2)
        #self.addWidget(self.lUsername, 3, 1, 1, 1)
        self.addWidget(self.tUsername, 3, 1, 1, 2)
        #self.addWidget(self.lPassword, 4, 1, 1, 1)
        self.addWidget(self.tPassword, 4, 1, 1, 2)
        self.addWidget(self.bLogin, 8, 1, 1, 2)
        
        
        
        
        
        