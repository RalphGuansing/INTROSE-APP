import sys
import datetime
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class Accounting_HomeView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.init_ui()   

    def account_receivable_box(self):
        self.areceivable_Box = QtWidgets.QGroupBox("")
        self.areceivable_Box.setStyleSheet("QGroupBox{border:0; background-color:#dc8989;}")
        Grid = QtWidgets.QGridLayout()
        Grid.setContentsMargins(0, 0, 0, 0)
        
        self.lAReceivable = QtWidgets.QLabel("Accounts Receivable".upper())
        self.lAReceivable.setAlignment(QtCore.Qt.AlignCenter)
        self.lAReceivable.setStyleSheet(self.labelStyle)
        
        self.bView_AReceivable = QtWidgets.QPushButton("View")
        self.bView_AReceivable.setStyleSheet(self.buttonStyle)
        self.bAdd_AReceivable = QtWidgets.QPushButton("Add")
        self.bAdd_AReceivable.setStyleSheet(self.buttonStyle)
        
        Grid.setRowStretch(3,1)
        self.inner_box = QtWidgets.QGroupBox("")
        innerGrid = QtWidgets.QGridLayout()
        self.inner_box.setLayout(innerGrid)
        
        Grid.addWidget(self.lAReceivable,1,1)
        Grid.addWidget(self.inner_box,2,1)
        
#        Grid.addWidget(self.lAReceivable,1,1)
        innerGrid.addWidget(self.bView_AReceivable,2,1)
#        Grid.addWidget(self.bAdd_AReceivable,3,1)
        
        self.areceivable_Box.setLayout(Grid)
        
    def account_payable_box(self):
        self.apayable_Box = QtWidgets.QGroupBox("")
        self.apayable_Box.setStyleSheet("QGroupBox{border:0; background-color:#dc8989; }")
        Grid = QtWidgets.QGridLayout()
        
        #Grid.setSpacing(0)
        Grid.setContentsMargins(0, 0, 0, 0)
        
        self.lAPayable = QtWidgets.QLabel("Accounts Payable".upper())
        self.lAPayable.setAlignment(QtCore.Qt.AlignCenter)
        self.lAPayable.setStyleSheet(self.labelStyle)
        
        self.bView_APayable = QtWidgets.QPushButton("View")
        self.bView_APayable.setStyleSheet(self.buttonStyle)
        self.bAdd_APayable = QtWidgets.QPushButton("Add")
        self.bAdd_APayable.setStyleSheet(self.buttonStyle)
        
        Grid.setRowStretch(4,1)
        self.inner_box = QtWidgets.QGroupBox("")
        innerGrid = QtWidgets.QGridLayout()
        self.inner_box.setLayout(innerGrid)
        
        Grid.addWidget(self.lAPayable,1,1)
        Grid.addWidget(self.inner_box,2,1)
        
        innerGrid.addWidget(self.bView_APayable,2,1)
        innerGrid.addWidget(self.bAdd_APayable,3,1)
        
        self.apayable_Box.setLayout(Grid)
        
    def init_ui(self):
        
        self.labelStyle = """QLabel { font-size: 14pt; padding: 7px;color:lightgray;  background-color:#d06262; }"""
        self.buttonStyle = """
        QPushButton { font-size: 14pt; padding: 8px; color: white; 
        background-color: darkgray;
        border-color: darkgray;
                                            border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: gray; border-color: gray;}
                         
        """
        
        self.account_receivable_box()
        self.account_payable_box()
        
        self.addWidget(self.areceivable_Box,1,1)
        self.addWidget(self.apayable_Box,1,2)
        
        self.setRowStretch(11,1)
        

#        self.addWidget(self.logoLabel, 2, 1, 1, 2)
#        #self.addWidget(self.lUsername, 3, 1, 1, 1)
#        self.addWidget(self.tUsername, 3, 1, 1, 2)
#        #self.addWidget(self.lPassword, 4, 1, 1, 1)
#        self.addWidget(self.tPassword, 4, 1, 1, 2)
#        self.addWidget(self.bLogin, 8, 1, 1, 2)
        