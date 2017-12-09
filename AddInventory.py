import sys
from PyQt5 import QtWidgets,QtCore,QtGui,Qt
from InventoryView import *

class AddInventoryView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Inventory")
        self.added_products = []
        self.current_row = 0
        self.init_ui()

    def add_product_list(self):
        db_connection = InventoryDatabase()
        self.products = db_connection.get_product_list()
        for product in self.products:
            self.tProduct.addItem(product.name)
        db_connection.close_connection()

    def add_new_product(self):
        db_connection = InventoryDatabase()
        #db_connection.add_product()
        db_connection.close_connection()        

    def add_product_table(self):
        try:
            self.tProduct_Table.setItem(self.current_row,0,QtWidgets.QTableWidgetItem(str(self.tQuantity.value())))
            self.tProduct_Table.setItem(self.current_row,1,QtWidgets.QTableWidgetItem(str(self.tUnit.text())))
            self.tProduct_Table.setItem(self.current_row,2,QtWidgets.QTableWidgetItem(self.products[self.tProduct.currentIndex()].name))
            self.tProduct_Table.setItem(self.current_row,3,QtWidgets.QTableWidgetItem(str(self.tUnitPrice.text())))
            self.tProduct_Table.setItem(self.current_row,4,QtWidgets.QTableWidgetItem(str(int(self.tUnitPrice.text()) * int(self.tQuantity.value()))))
        except ValueError:
            print('Value Error: Wrong input type')

        self.tQuantity.setValue(0)
        self.tUnit.setText('')
        self.tUnitPrice.setText('')

        self.current_row += 1

    def submit_products(self):
        db_connection = InventoryDatabase()
        for x in range(self.current_row):
            try:
                db_connection.update_product(self.tProduct_Table.item(x,2).text(),self.tProduct_Table.item(x,1).text(),self.tProduct_Table.item(x,3).text())
                db_connection.add_product_quantity(self.tProduct_Table.item(x,2).text(),self.tQuantity.value())
            except BaseException:
                print('Error')
        self.current_row = 0
        db_connection.close_connection()
        self.tProduct_Table.clearContents()


    def delete_entry(self):
        self.tProduct_Table.removeRow(self.tProduct_Table.currentRow())
        self.tProduct_Table.setRowCount(5)

    def init_ui(self):
        #Create Widgets
        self.lInventory_Details = QtWidgets.QLabel("INVENTORY DETAILS")
        self.lInventory_Details.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')
        
        self.tinvoiceNum = QtWidgets.QLabel("System Generated")
        self.tinvoiceNum.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')			

        #Label#
        self.lDate = QtWidgets.QLabel("Date: ")
        self.lDate.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tDate = QtWidgets.QCalendarWidget()
				
		#Label#
        self.lProduct_Table = QtWidgets.QLabel("PRODUCTS")
        self.lProduct_Table.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')		
		
		#Product Table#
        self.tProduct_Table = QtWidgets.QTableWidget()
        self.tProduct_Table.setRowCount(5)
        self.tProduct_Table.setColumnCount(5)
        self.tProduct_Table.setHorizontalHeaderLabels(["Quantity", "Unit", "Articles", "Unit Price", "Amount"])
        self.tProduct_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        tablewidth = self.tProduct_Table.width() + 5
        self.tProduct_Table.setColumnWidth(0, tablewidth / 8)
        self.tProduct_Table.setColumnWidth(1, tablewidth / 5)
        self.tProduct_Table.setColumnWidth(2, tablewidth / 3)
        self.tProduct_Table.setColumnWidth(3, tablewidth / 8)		
        self.tProduct_Table.setColumnWidth(4, tablewidth / 6)
        self.tProduct_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)			

        self.Add_Product_Table = QtWidgets.QPushButton("Add Product")
        self.Add_Product_Table.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
		
        
        self.lAddProduct = QtWidgets.QLabel("PRODUCT DETAILS")
        self.lAddProduct.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')
        
		#Label#
        self.lQuantity = QtWidgets.QLabel("Quantity: ")
        self.lQuantity.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tQuantity = QtWidgets.QSpinBox(self.frame)
        self.tQuantity.setFixedWidth(50)		
        self.tQuantity.setMinimum(0)
        self.tQuantity.setMaximum(999999999)

		#Label#
        self.lUnit = QtWidgets.QLabel("Unit: ")
        self.lUnit.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tUnit = QtWidgets.QLineEdit(self.frame)
        self.tUnit.setFixedWidth(70)	
		
        #Label#
        self.lProduct = QtWidgets.QLabel("Product:")
        self.lProduct.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        #TEXT INPUT#
        self.tProduct = QtWidgets.QComboBox(self.frame)
        self.tProduct.setFixedWidth(200)		
        self.add_product_list()

        #Label#
        self.lUnitPrice = QtWidgets.QLabel("Unit Price: ")
        self.lUnitPrice.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tUnitPrice = QtWidgets.QLineEdit(self.frame)
        self.tUnitPrice.setFixedWidth(70)	

        self.bAdd = QtWidgets.QPushButton("Add")
        self.bAdd.setStyleSheet('QPushButton {color: white;background-color: #1db6d1;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 12px;min-width: 10em;padding: 4px;}')
        self.bAdd.setFixedWidth(200)
        self.bAdd.clicked.connect(self.add_product_table)
        
        self.bDelete = QtWidgets.QPushButton("")
        #self.bDelete.setStyleSheet('QPushButton {color: white;background-color: #6017a5;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 12px;min-width: 10em;padding: 4px;}')        
        self.bDelete.setFixedWidth(50)
        self.bDelete.setIcon(QtGui.QIcon('delete_button.png'))
        self.bDelete.setIconSize(QtCore.QSize(24,24))
        self.bDelete.clicked.connect(self.delete_entry)

        self.bBack = QtWidgets.QPushButton("Back")
        self.bBack.setStyleSheet('QPushButton {color: white;background-color: #d62f2f;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bBack.setFixedWidth(80)
        
        self.bSubmit = QtWidgets.QPushButton("Submit")
        self.bSubmit.setStyleSheet('QPushButton {color: white;background-color: #47c468;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bSubmit.setFixedWidth(200)
        self.bSubmit.clicked.connect(self.submit_products)


        self.setColumnStretch(7,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(11,1)

        #Add Widgets
        
        self.addWidget(self.lInventory_Details, 0, 1, 1, 1)
		
        self.addWidget(self.lDate, 1, 1, 1, 1)
        self.addWidget(self.tDate, 1, 2, 1, 1)
				
	
        self.addWidget(self.lProduct_Table, 2, 1, 1, 1)	
        self.addWidget(self.tProduct_Table, 3, 1, 4, 3)			
        
        
        self.addWidget(self.lAddProduct, 2, 4, 1, 2, QtCore.Qt.AlignCenter)

        self.addWidget(self.lProduct, 3, 4, 1, 1)
        self.addWidget(self.tProduct, 3, 5, 1, 1)
		
        self.addWidget(self.lQuantity, 4, 4, 1, 1)
        self.addWidget(self.tQuantity, 4, 5, 1, 1)

        self.addWidget(self.lUnit, 5, 4, 1, 1)
        self.addWidget(self.tUnit, 5, 5, 1, 1)

        self.addWidget(self.lUnitPrice, 6, 4, 1, 1)
        self.addWidget(self.tUnitPrice, 6, 5, 1, 1)
        
        #self.addWidget(self.lProduct_Code, 1, 1, 1, 1)
        self.addWidget(self.bDelete, 2, 3, 1, 2, QtCore.Qt.AlignCenter)
        self.addWidget(self.bAdd, 7, 4, 1, 2, QtCore.Qt.AlignCenter)

        
        #self.addWidget(self.lProduct_Code, 1, 1, 1, 1)
        self.addWidget(self.bBack, 10, 2, 1, 1, QtCore.Qt.AlignRight)
        self.addWidget(self.bSubmit, 10, 3, 1, 1)
        