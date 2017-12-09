import sys
from PyQt5 import QtWidgets,QtCore


class HomeInvoice(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.init_ui()

    def init_ui(self):

        self.bAddInvoice = QtWidgets.QPushButton("Add Invoice")
        self.bAddInvoice.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bAddInvoice.setFixedWidth(200)
        
        self.bViewInvoice = QtWidgets.QPushButton("View Invoice")
        self.bViewInvoice.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bViewInvoice.setFixedWidth(200) 

        self.bInvoiceList = QtWidgets.QPushButton("View Invoice List")
        self.bInvoiceList.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bInvoiceList.setFixedWidth(200)      
        
        self.setColumnStretch(4,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(16,1)

        #Add Widgets
        self.addWidget(self.bAddInvoice, 1, 2, 1, 1)           
        self.addWidget(self.bViewInvoice, 3, 2, 1, 1)     
        self.addWidget(self.bInvoiceList, 4, 2, 1, 1)          