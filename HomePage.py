import sys
from PyQt5 import QtWidgets,QtCore


class HomePage(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Home Page")
        self.init_ui()

    def init_ui(self):
        #Create Widgets
        self.lInvoice_Details = QtWidgets.QLabel("<img src='picture.png' />")
        #self.lInvoice_Details.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')	
            
        self.bAddInventory = QtWidgets.QPushButton("Add Inventory")
        self.bAddInventory.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bAddInventory.setFixedWidth(200)
        
        
        self.bDeleteInventory = QtWidgets.QPushButton("Delete Inventory")
        self.bDeleteInventory.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bDeleteInventory.setFixedWidth(200)
        
        self.bViewInventory = QtWidgets.QPushButton("View Inventory")
        self.bViewInventory.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bViewInventory.setFixedWidth(200)
        

        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(16,1)

        #Add Widgets
        self.addWidget(self.lInvoice_Details, 0, 1, 1, 1)
        
        self.addWidget(self.bAddInventory, 2, 1, 1, 1)  
        self.addWidget(self.bDeleteInventory, 3, 1, 1, 1) 
        self.addWidget(self.bViewInventory, 4, 1, 1, 1) 
        