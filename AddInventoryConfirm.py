import sys
from PyQt5 import QtWidgets,QtCore


class AddInventoryConfirm(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Add Inventory")
        self.init_ui()

    def init_ui(self):
        #Create Widgets
        self.lInvoice_Details = QtWidgets.QLabel("INVENTORY")
        self.lInvoice_Details.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')


        self.lProduct_Table = QtWidgets.QLabel("PRODUCTS")
        self.lProduct_Table.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')        
		#Product Table#
        self.tProduct_Table = QtWidgets.QTableWidget()
        self.tProduct_Table.setRowCount(5)
        self.tProduct_Table.setColumnCount(5)
        self.tProduct_Table.setHorizontalHeaderLabels(["Quantity", "Unit", "Articles", "Unit Price", "Amount"])
        self.tProduct_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        tablewidth = self.tProduct_Table.width() + 5
        self.tProduct_Table.setColumnWidth(0, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(1, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(2, tablewidth / 2)
        self.tProduct_Table.setColumnWidth(3, tablewidth / 6)		
        self.tProduct_Table.setColumnWidth(4, tablewidth / 6)
        self.tProduct_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)			


        self.lConfirmation = QtWidgets.QLabel("Please confirm if these values are correct")
        self.lConfirmation.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')


        self.bBack = QtWidgets.QPushButton("Go back")
        self.bBack.setStyleSheet('QPushButton { font-size: 14px; border-radius:10px ;padding: 10px;}')
        self.bBack.setFixedWidth(80)
        
        self.bAddInventory = QtWidgets.QPushButton("Confirm")
        self.bAddInventory.setStyleSheet('QPushButton {color: white;background-color: #47c468;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bAddInventory.setFixedWidth(200)


        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(13,1)

        #Add Widgets
        
        self.addWidget(self.lInvoice_Details, 0, 2, 1, 1)

        self.addWidget(self.lProduct_Table, 4, 2, 1, 1)	        
        self.addWidget(self.tProduct_Table, 5, 2, 3, 3)

        self.addWidget(self.lConfirmation, 14, 2, 1, 1)
        
        self.addWidget(self.bBack, 15, 2, 1, 1)
        
        self.addWidget(self.bAddInventory, 15, 3, 1, 1)        
        