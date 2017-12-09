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
        #self.bAddInventory.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bAddInventory.setStyleSheet('QPushButton {color: white;background-color: #1db6d1;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 12px;min-width: 10em;padding: 4px;}')
        self.bAddInventory.setFixedWidth(200)
        
        
        self.bViewInventory = QtWidgets.QPushButton("View Inventory")
        #self.bViewInventory.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bViewInventory.setStyleSheet('QPushButton {color: white;background-color: #1db6d1;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 12px;min-width: 10em;padding: 4px;}')
        self.bViewInventory.setFixedWidth(200)
        

        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(16,1)

        #Add Widgets
        self.addWidget(self.lInvoice_Details, 0, 1, 1, 1)
        
        self.addWidget(self.bAddInventory, 2, 1, 1, 1, QtCore.Qt.AlignCenter)  
        self.addWidget(self.bViewInventory, 3, 1, 1, 1, QtCore.Qt.AlignCenter) 
        