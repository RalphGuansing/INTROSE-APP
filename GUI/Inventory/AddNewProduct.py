import sys
from PyQt5 import QtWidgets,QtCore,QtGui,Qt
from Inventory.InventoryView import *
from Inventory.AddInventoryConfirm import ConfirmWindow
from Accounting.AccountingView import *
import datetime

class AddNewProduct(QtWidgets.QGridLayout):
	def __init__(self, frame):
		super().__init__()
		self.frame = frame
		self.init_ui()


	def init_ui(self):

		self.lName = QtWidgets.QLabel("Name: ")
		self.lName.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tName = QtWidgets.QLineEdit(self.frame)
		self.tName.setFixedWidth(200)

		self.lSupplier = QtWidgets.QLabel("Supplier: ")
		self.lSupplier.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tSupplier = QtWidgets.QComboBox(self.frame)
		self.tSupplier.setFixedWidth(200)	

		self.lUnit = QtWidgets.QLabel("Unit:")
		self.lUnit.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tUnit = QtWidgets.QLineEdit(self.frame)
		self.tUnit.setFixedWidth(200)

		self.lUnitPrice = QtWidgets.QLabel("Unit Price: ")
		self.lUnitPrice.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tUnitPrice = QtWidgets.QLineEdit(self.frame)
		self.tUnitPrice.setFixedWidth(200)

		self.setColumnStretch(7,1)
		self.setColumnStretch(1,1)
		self.setRowStretch(11,1)

		self.addWidget(self.lName,0,3,1,1)
		self.addWidget(self.tName,0,4,1,1)
		self.addWidget(self.lSupplier,1,3,1,1)
		self.addWidget(self.tSupplier,1,4,1,1)
		self.addWidget(self.lUnit,2,3,1,1)
		self.addWidget(self.tUnit,2,4,1,1)
		self.addWidget(self.lUnitPrice,3,3,1,1)
		self.addWidget(self.tUnitPrice,3,4,1,1)