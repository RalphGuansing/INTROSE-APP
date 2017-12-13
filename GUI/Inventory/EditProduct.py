import sys
from PyQt5 import QtWidgets,QtCore,QtGui,Qt
from Inventory.InventoryView import *
from Inventory.AddNewConfirm import ConfirmWindow
from Accounting.AccountingView import *
import datetime

class EditProductConfirm(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Confirmation")
        self.init_ui()

    def add_to_table(self, row, column, text):
        self.tProduct_Table.setItem(row,column,QtWidgets.QTableWidgetItem(str(text)))

    def add_to_edit(self, row, column, text):
        self.tEdit_Table.setItem(row,column,QtWidgets.QTableWidgetItem(str(text)))

    def init_ui(self):
        #Create Widgets

        self.lConfirmation = QtWidgets.QLabel("Edit this product")
        self.lConfirmation.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tProduct_Table = QtWidgets.QTableWidget()
        self.tProduct_Table.setColumnCount(6)
        self.tProduct_Table.setRowCount(1)
        self.tProduct_Table.setHorizontalHeaderLabels(["Articles", "Supplier", "Unit", "Retail Price",
         "Unit Price", "Vatable"])
        self.tProduct_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        tablewidth = self.tProduct_Table.width() + 6
        self.tProduct_Table.setColumnWidth(0, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(1, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(2, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(3, tablewidth / 6)       
        self.tProduct_Table.setColumnWidth(4, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(5, tablewidth / 6)
        self.tProduct_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tProduct_Table.setFixedHeight(50)

        self.lConfirmation2 = QtWidgets.QLabel("to these values?")
        self.lConfirmation2.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tEdit_Table = QtWidgets.QTableWidget()
        self.tEdit_Table.setColumnCount(6)
        self.tEdit_Table.setRowCount(1)
        self.tEdit_Table.setHorizontalHeaderLabels(["Articles", "Supplier", "Unit", "Retail Price",
         "Unit Price", "Vatable"])
        self.tEdit_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        tablewidth = self.tEdit_Table.width() + 6
        self.tEdit_Table.setColumnWidth(0, tablewidth / 6)
        self.tEdit_Table.setColumnWidth(1, tablewidth / 6)
        self.tEdit_Table.setColumnWidth(2, tablewidth / 6)
        self.tEdit_Table.setColumnWidth(3, tablewidth / 6)       
        self.tEdit_Table.setColumnWidth(4, tablewidth / 6)
        self.tEdit_Table.setColumnWidth(5, tablewidth / 6)
        self.tEdit_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tEdit_Table.setFixedHeight(50)

        self.bConfirm = QtWidgets.QPushButton("Confirm")
        self.bConfirm.setStyleSheet('QPushButton {color: white;background-color: #47c468;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bConfirm.setFixedWidth(200)

        self.bBack = QtWidgets.QPushButton("Cancel")
        self.bBack.setStyleSheet('QPushButton {color: white;background-color: #ff0000;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 4px;}')
        self.bBack.setFixedWidth(80)
        
        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(13,1)

        self.addWidget(self.lConfirmation, 1, 2, 1, 3, QtCore.Qt.AlignCenter)
        self.addWidget(self.tProduct_Table, 2, 2, 4, 3, QtCore.Qt.AlignCenter)
        self.addWidget(self.lConfirmation2, 6, 2, 1, 3, QtCore.Qt.AlignCenter)
        self.addWidget(self.tEdit_Table, 7, 2, 4, 3, QtCore.Qt.AlignCenter)   
        self.addWidget(self.bConfirm, 11, 2, 1, 2, QtCore.Qt.AlignCenter)
        self.addWidget(self.bBack, 11, 3, 1, 2, QtCore.Qt.AlignCenter)        

        
class WindowFrame(QtWidgets.QWidget):
    def __init__(self, layout):
        super().__init__()
        self.setWindowTitle("Confirmation")
        self.layout = layout(self)
        self.setLayout(self.layout)

class ConfirmWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ConfirmWindow, self).__init__(parent)
        self.resize(800,300)
        self.layout = WindowFrame(EditProductConfirm)
        self.setWindowTitle("Confirmation")
        self.setCentralWidget(self.layout)

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

	def edit_product(self):
		# if self.isVatable.isChecked():
		# 	vatable = 1
		# else:
		# 	vatable = 0
		# db_inventory = InventoryDatabase()
		# db_inventory.add_product(self.tName.text(),self.suppliers[self.tSupplier.currentIndex()],self.unit_list[self.tUnit.currentIndex()],
		# 	self.tUnitPrice.value(),self.tRetailPrice.value(),0,vatable)
		# db_inventory.close_connection()
		# self.tName.setText('')
		# self.tUnitPrice.setValue(0)
		# self.tRetailPrice.setValue(0)
		self.confirm_window.close()

	def set_confirm_table(self):
		if self.isVatable.isChecked():
			vatable = 'Yes'
		else:
			vatable = 'No'
		product = list(filter(lambda x: x.id == self.id_list[self.tProduct_id.currentIndex()],self.product_list))
		if product[0].vatable == 1:
			vat = 'Yes'
		else:
			vat = 'No'
		self.confirm_window.layout.layout.add_to_table(0,0,product[0].name)
		self.confirm_window.layout.layout.add_to_table(0,1,product[0].supplier)
		self.confirm_window.layout.layout.add_to_table(0,2,product[0].packaging)
		self.confirm_window.layout.layout.add_to_table(0,3,product[0].per_unit_price)
		self.confirm_window.layout.layout.add_to_table(0,4,product[0].retail_price)
		self.confirm_window.layout.layout.add_to_table(0,5,vat)

		self.confirm_window.layout.layout.add_to_edit(0,0,self.tName.text())
		self.confirm_window.layout.layout.add_to_edit(0,1,self.suppliers[self.tSupplier.currentIndex()])
		self.confirm_window.layout.layout.add_to_edit(0,2,self.unit_list[self.tUnit.currentIndex()])
		self.confirm_window.layout.layout.add_to_edit(0,3,str(self.tUnitPrice.value()))
		self.confirm_window.layout.layout.add_to_edit(0,4,str(self.tRetailPrice.value()))
		self.confirm_window.layout.layout.add_to_edit(0,5,vatable)

	def change_information(self):
		product = list(filter(lambda x: x.id == self.id_list[self.tProduct_id.currentIndex()],self.product_list))
		self.tName.setText(product[0].name)
		self.tSupplier.setCurrentIndex(self.tSupplier.findText(product[0].supplier))
		self.tUnit.setCurrentIndex(self.tUnit.findText(product[0].packaging))
		self.tUnitPrice.setValue(int(product[0].per_unit_price))
		self.tRetailPrice.setValue(int(product[0].retail_price))
		if product[0].vatable == 1:
			self.isVatable.setChecked(True)
		else:
			self.isVatable.setChecked(False)

	def confirm_edit_product(self):
		if self.tName.text() != '': 
			self.confirm_window = ConfirmWindow()
			self.confirm_window.show()
			self.confirm_window.layout.layout.bConfirm.clicked.connect(self.edit_product)
			self.set_confirm_table()
		else:
			self.error_message('Please fill up all necessary information.')

	def add_supplier_list(self):
		self.suppliers = ['my sans','nestle','coca-cola','nuka-cola']
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
		self.bEdit.clicked.connect(self.confirm_edit_product)

		self.lProduct_id = QtWidgets.QLabel("Inventory ID: ") 
		self.lProduct_id.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

		self.tProduct_id = QtWidgets.QComboBox(self.frame)
		self.tProduct_id.setFixedWidth(200)
		self.tProduct_id.currentIndexChanged.connect(self.change_information)
		self.add_id_list()

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