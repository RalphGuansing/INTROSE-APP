import sys
from PyQt5 import QtWidgets,QtCore
# from InventoryView import *

class AddInventoryView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Edit Invoice")
        self.init_ui()

    def init_ui(self):

        self.lInvoice_Number = QtWidgets.QLabel("Invoice Number: ") 
        self.lInvoice_Number.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tInvoice_Number = QtWidgets.QComboBox(self.frame)
        self.tInvoice_Number.setFixedWidth(200)

        self.lName = QtWidgets.QLabel("Name: ")
        self.lName.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tName = QtWidgets.QLineEdit(self.frame)
        self.tName.setFixedWidth(200)

        self.lBuyer = QtWidgets.QLabel("Buyer: ")
        self.lBuyer.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tBuyer = QtWidgets.QComboBox(self.frame)
        self.tBuyer.setFixedWidth(200)

        self.lSeller = QtWidgets.QLabel("Seller: ")
        self.lSeller.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tSeller = QtWidgets.QComboBox(self.frame)
        self.tSeller.setFixedWidth(200)

        self.lUnit = QtWidgets.QLabel("Unit:")
        self.lUnit.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tUnit = QtWidgets.QComboBox(self.frame)
        self.tUnit.setFixedWidth(200)

        self.lUnitPrice = QtWidgets.QLabel("Unit Price: ")
        self.lUnitPrice.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tUnitPrice = QtWidgets.QSpinBox(self.frame)
        self.tUnitPrice.setFixedWidth(200)
        self.tUnitPrice.setMinimum(1)

        self.bEdit = QtWidgets.QPushButton("Edit")
        self.bEdit.setStyleSheet('QPushButton {color: white;background-color: #1db6d1;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 12px;min-width: 10em;padding: 4px;}')
        self.bEdit.setFixedWidth(200)
        #self.bEdit.clicked.connect(self.confirm_add_product)

        self.setColumnStretch(7,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(11,1)

        self.addWidget(self.lProduct_id,1,3,1,1)
        self.addWidget(self.tProduct_id,1,4,1,1)
        self.addWidget(self.lName,2,3,1,1)
        self.addWidget(self.tName,2,4,1,1)
        self.addWidget(self.lSupplier,3,3,1,1)
        self.addWidget(self.tSupplier,3,4,1,1)
        self.addWidget(self.lUnit,4,3,1,1)
        self.addWidget(self.tUnit,4,4,1,1)
        self.addWidget(self.lUnitPrice,5,3,1,1)
        self.addWidget(self.tUnitPrice,5,4,1,1)
        self.addWidget(self.lRetailPrice,6,3,1,1)
        self.addWidget(self.tRetailPrice,6,4,1,1)
        self.addWidget(self.isVatable,7,3,1,2,QtCore.Qt.AlignCenter)
        self.addWidget(self.bEdit,8,3,1,2,QtCore.Qt.AlignCenter)