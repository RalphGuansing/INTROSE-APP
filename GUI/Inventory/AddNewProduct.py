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
		self.tName.setFixedWidth(100)

		self.lSupplier = QtWidgets.QLabel("Supplier: ")
		self.lSupplier.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tSupplier = QtWidgets.QComboBox(self.frame)
		self.tSupplier.setFixedWidth(100)	

		self.lUnit = QtWidgets.QLabel("Unit:")
		self.lUnit.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tUnit = QtWidgets.QLineEdit(self.frame)
		self.tUnit.setFixedWidth(100)

		self.lUnitPrice = QtWidgets.QLabel("Unit Price: ")
		self.lUnitPrice.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tUnitPrice = QtWidgets.QLineEdit(self.frame)
		self.tUnitPrice.setFixedWidth(100)

		self.addWidget(self.lName,0,0,1,1)
		self.addWidget(self.tName,0,1,1,1)
		self.addWidget(self.lSupplier,1,0,1,1)
		self.addWidget(self.tSupplier,1,1,1,1)
		self.addWidget(self.lUnit,2,0,1,1)
		self.addWidget(self.tUnit,2,1,1,1)
		self.addWidget(self.lUnitPrice,3,0,1,1)
		self.addWidget(self.tUnitPrice,3,1,1,1)