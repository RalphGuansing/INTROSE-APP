import sys
from PyQt5 import QtWidgets,QtCore,QtGui,Qt
from Inventory.InventoryView import *
from Inventory.AddNewConfirm import ConfirmWindow
from Accounting.AccountingView import *
import datetime

class EditProduct(QtWidgets.QGridLayout):
	def __init__(self, frame):
		super().__init__()
		self.frame = frame
		self.init_ui()

	def error_message(self, message):
		infoBox = QtWidgets.QMessageBox()
		infoBox.setIcon(QtWidgets.QMessageBox.Warning)
		infoBox.setWindowTitle('Error')
		infoBox.setText(message)
		infoBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		infoBox.setEscapeButton(QtWidgets.QMessageBox.Close) 
		infoBox.exec_()

	def add_product(self):
		if self.isVatable.isChecked():
			vatable = 1
		else:
			vatable = 0
		db_inventory = InventoryDatabase()
		db_inventory.add_product(self.tName.text(),self.suppliers[self.tSupplier.currentIndex()],self.unit_list[self.tUnit.currentIndex()],
			self.tUnitPrice.value(),self.tRetailPrice.value(),0,vatable)
		db_inventory.close_connection()
		self.tName.setText('')
		self.tUnitPrice.setValue(0)
		self.tRetailPrice.setValue(0)
		self.confirm_window.close()

	def set_confirm_table(self):
		if self.isVatable.isChecked():
			vatable = 'Yes'
		else:
			vatable = 'No'
		self.confirm_window.layout.layout.add_to_table(0,0,self.tName.text())
		self.confirm_window.layout.layout.add_to_table(0,1,self.suppliers[self.tSupplier.currentIndex()])
		self.confirm_window.layout.layout.add_to_table(0,2,self.unit_list[self.tUnit.currentIndex()])
		self.confirm_window.layout.layout.add_to_table(0,3,str(self.tUnitPrice.value()))
		self.confirm_window.layout.layout.add_to_table(0,4,str(self.tRetailPrice.value()))
		self.confirm_window.layout.layout.add_to_table(0,5,vatable)

	def confirm_add_product(self):
		if self.tName.text() != '': 
			self.confirm_window = ConfirmWindow()
			self.confirm_window.show()
			self.confirm_window.layout.layout.bConfirm.clicked.connect(self.add_product)
			self.set_confirm_table()
		else:
			self.error_message('Please fill up all necessary information.')

	def add_supplier_list(self):
		self.suppliers = ['nestle','coca-cola','nuka-cola']
		for supplier in self.suppliers:
			self.tSupplier.addItem(supplier)

	def add_id_list(self):
		db_inventory = InventoryDatabase()
		self.product_list = db_inventory.get_product_list()
		self.id_list = [x.id for x in self.product_list]
		for x in self.id_list:
			self.tProduct_id.addItem(str(x))
		db_inventory.close_connection()

	def add_product_unit(self):
		self.unit_list = ['plastic','bottle','tetrapack','yakult-sized']
		for unit in self.unit_list:
			self.tUnit.addItem(unit)

	def init_ui(self):

		self.lProduct_id = QtWidgets.QLabel("Inventory ID: ") 
		self.lProduct_id.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tProduct_id = QtWidgets.QComboBox(self.frame)
		self.tProduct_id.setFixedWidth(200)
		self.add_id_list()

		self.lName = QtWidgets.QLabel("Name: ")
		self.lName.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tName = QtWidgets.QLineEdit(self.frame)
		self.tName.setFixedWidth(200)

		self.lSupplier = QtWidgets.QLabel("Supplier: ")
		self.lSupplier.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tSupplier = QtWidgets.QComboBox(self.frame)
		self.tSupplier.setFixedWidth(200)
		self.add_supplier_list()

		self.lUnit = QtWidgets.QLabel("Unit:")
		self.lUnit.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tUnit = QtWidgets.QComboBox(self.frame)
		self.tUnit.setFixedWidth(200)
		self.add_product_unit()

		self.lUnitPrice = QtWidgets.QLabel("Unit Price: ")
		self.lUnitPrice.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tUnitPrice = QtWidgets.QSpinBox(self.frame)
		self.tUnitPrice.setFixedWidth(200)
		self.tUnitPrice.setMinimum(1)

		self.lRetailPrice = QtWidgets.QLabel("Retail Price: ")
		self.lRetailPrice.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tRetailPrice = QtWidgets.QSpinBox(self.frame)
		self.tRetailPrice.setFixedWidth(200)
		self.tRetailPrice.setMinimum(1)

		self.isVatable = QtWidgets.QCheckBox('Is Vatable',self.frame)

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
		self.addWidget(self.bAdd,8,3,1,2,QtCore.Qt.AlignCenter)