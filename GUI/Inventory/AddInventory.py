import sys
from PyQt5 import QtWidgets,QtCore,QtGui,Qt
from Inventory.InventoryView import *
from Inventory.AddInventoryConfirm import ConfirmWindow
from Accounting.AccountingView import *
import datetime

class AddInventoryView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Inventory")
        self.added_products = []
        self.current_row = 0
        self.init_ui()

    def re_init(self):
        for i in reversed(range(self.count())): 
            self.itemAt(i).widget().setParent(None)
        self.init_ui()

    def error_message(self, message):
        infoBox = QtWidgets.QMessageBox()
        infoBox.setIcon(QtWidgets.QMessageBox.Warning)
        infoBox.setWindowTitle('Error')
        infoBox.setText(message)
        infoBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        infoBox.setEscapeButton(QtWidgets.QMessageBox.Close) 
        infoBox.exec_()

    def add_product_list(self):
        db_connection = InventoryDatabase()
        self.tProduct.clear()
        self.products = db_connection.get_product_list()
        for product in self.products:
            self.tProduct.addItem(product.name + ', ' + product.packaging)
        db_connection.close_connection()

    # def add_product_unit(self):
    #     self.unit_list = ['plastic','bottle','tetrapack','yakult-sized']
    #     for unit in self.unit_list:
    #         self.tUnit.addItem(unit)

    def add_new_product(self):
        db_connection = InventoryDatabase()
        #db_connection.add_product()
        db_connection.close_connection()        

    def add_product_table(self):
        db_connection = InventoryDatabase()
        if db_connection.is_product_available(self.products[self.tProduct.currentIndex()].name,self.products[self.tProduct.currentIndex()].packaging):
            exist = False
            for x in range(self.tProduct_Table.rowCount()):
                if self.tProduct_Table.item(x,2).text() == self.products[self.tProduct.currentIndex()].name and self.tProduct_Table.item(x,1).text() == self.products[self.tProduct.currentIndex()].packaging:
                    quantity = self.tQuantity.value() + int(self.tProduct_Table.item(x,0).text())
                    amount = quantity * self.tUnitPrice.value()
                    self.tProduct_Table.setItem(x,0,QtWidgets.QTableWidgetItem(str(quantity)))
                    self.tProduct_Table.setItem(x,3,QtWidgets.QTableWidgetItem(str(self.tUnitPrice.value())))
                    self.tProduct_Table.setItem(x,4,QtWidgets.QTableWidgetItem(str(amount)))
                    exist = True
                    break

            if not exist:        
                self.tProduct_Table.insertRow(self.current_row)
                self.tProduct_Table.setItem(self.current_row,0,QtWidgets.QTableWidgetItem(str(self.tQuantity.value())))
                self.tProduct_Table.setItem(self.current_row,1,QtWidgets.QTableWidgetItem(self.products[self.tProduct.currentIndex()].packaging))
                self.tProduct_Table.setItem(self.current_row,2,QtWidgets.QTableWidgetItem(self.products[self.tProduct.currentIndex()].name))
                self.tProduct_Table.setItem(self.current_row,3,QtWidgets.QTableWidgetItem(str(self.tUnitPrice.value())))
                self.tProduct_Table.setItem(self.current_row,4,QtWidgets.QTableWidgetItem(str(int(self.tUnitPrice.value()) * int(self.tQuantity.value()))))
                self.current_row += 1
        else:
            self.error_message("Product doesn't exist!")
        self.tQuantity.setValue(0)
        self.tUnitPrice.setValue(0)
        db_connection.close_connection()

    def submit_products(self):
        db_connection_inv = InventoryDatabase()
        db_connection_apv = AccountingDB()
        apv_list = []
        for x in range(self.current_row):
            db_connection_inv.update_product(self.tProduct_Table.item(x,2).text(),self.tProduct_Table.item(x,1).text(),self.tProduct_Table.item(x,3).text())
            db_connection_inv.add_product_quantity(self.tProduct_Table.item(x,2).text(),self.tProduct_Table.item(x,1).text(),int(self.tProduct_Table.item(x,0).text()))
            apv_list.append(AccountsPayable(datetime.datetime.now(),self.tProduct_Table.item(x,2).text(),db_connection_apv.get_id_apv(),self.tProduct_Table.item(x,4).text()))
        for apv in apv_list:
            db_connection_apv.add_accountspayable(apv)
        self.current_row = 0
        db_connection_inv.close_connection()
        db_connection_apv.close_connection()
        self.tProduct_Table.clearContents()
        self.tProduct_Table.setRowCount(0)
        self.confirm_window.close()

    def confirm_submit(self):
        if self.current_row != 0:
            self.confirm_window = ConfirmWindow()
            self.confirm_window.show()
            self.confirm_window.layout.layout.bAddInventory.clicked.connect(self.submit_products)
            for x in range(self.current_row):
                self.confirm_window.layout.layout.add_to_table(x,0,self.tProduct_Table.item(x,0).text())
                self.confirm_window.layout.layout.add_to_table(x,1,self.tProduct_Table.item(x,1).text())
                self.confirm_window.layout.layout.add_to_table(x,2,self.tProduct_Table.item(x,2).text())
                self.confirm_window.layout.layout.add_to_table(x,3,self.tProduct_Table.item(x,3).text())
                self.confirm_window.layout.layout.add_to_table(x,4,self.tProduct_Table.item(x,4).text())
        else:
            self.error_message('No Products to Update!')


    def delete_entry(self):
        self.tProduct_Table.removeRow(self.tProduct_Table.currentRow())
        self.current_row -= 1

    def init_ui(self):
        #Create Widgets
        self.lInventory_Details = QtWidgets.QLabel("INVENTORY DETAILS")
        self.lInventory_Details.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')
        
        self.tinvoiceNum = QtWidgets.QLabel("System Generated")
        self.tinvoiceNum.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')			

        #Label#
        self.lDate = QtWidgets.QLabel("Date: ")
        self.lDate.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tDate = QtWidgets.QDateEdit(self.frame)
        self.tDate.setCalendarPopup(True)
        self.tDate.setDisplayFormat("yyyy-MM-dd")
        self.tDate.setDate(datetime.datetime.now())
				
		#Label#
        self.lProduct_Table = QtWidgets.QLabel("PRODUCTS")
        self.lProduct_Table.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')		
		
		#Product Table#
        self.tProduct_Table = QtWidgets.QTableWidget()
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
        self.tQuantity.setFixedWidth(200)		
        self.tQuantity.setMinimum(1)
        self.tQuantity.setMaximum(999999999)
		
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

        self.tUnitPrice = QtWidgets.QSpinBox(self.frame)
        self.tUnitPrice.setMinimum(1)
        self.tUnitPrice.setFixedWidth(200)	

        self.bAdd = QtWidgets.QPushButton("Add")
        self.bAdd.setStyleSheet('QPushButton {color: white;background-color: #1db6d1;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 12px;min-width: 10em;padding: 4px;}')
        self.bAdd.setFixedWidth(200)
        self.bAdd.clicked.connect(self.add_product_table)
        
        self.bDelete = QtWidgets.QPushButton("")
        #self.bDelete.setStyleSheet('QPushButton {color: white;background-color: #6017a5;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 12px;min-width: 10em;padding: 4px;}')        
        self.bDelete.setFixedWidth(50)
        self.bDelete.setIcon(QtGui.QIcon('Resources/delete_button.png'))
        self.bDelete.setIconSize(QtCore.QSize(24,24))
        self.bDelete.clicked.connect(self.delete_entry)

        
        self.bSubmit = QtWidgets.QPushButton("Submit")
        self.bSubmit.setStyleSheet('QPushButton {color: white;background-color: #47c468;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bSubmit.setFixedWidth(200)
        self.bSubmit.clicked.connect(self.confirm_submit)

        self.setColumnStretch(7,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(11,1)

        #Add Widgets
        
        self.addWidget(self.lInventory_Details, 0, 2, 1, 1)
		
        self.addWidget(self.lDate, 1, 2, 1, 1)
        self.addWidget(self.tDate, 1, 3, 1, 1)
				
	
        self.addWidget(self.lProduct_Table, 2, 4, 1, 1)	
        self.addWidget(self.tProduct_Table, 3, 4, 4, 3)			
        
        
        self.addWidget(self.lAddProduct, 2, 2, 1, 2, QtCore.Qt.AlignCenter)

        self.addWidget(self.lProduct, 3, 2, 1, 1)
        self.addWidget(self.tProduct, 3, 3, 1, 1)
		
        self.addWidget(self.lQuantity, 4, 2, 1, 1)
        self.addWidget(self.tQuantity, 4, 3, 1, 1)

        self.addWidget(self.lUnitPrice, 5, 2, 1, 1)
        self.addWidget(self.tUnitPrice, 5, 3, 1, 1)
        
        self.addWidget(self.bDelete, 2, 6, 1, 2, QtCore.Qt.AlignCenter)
        self.addWidget(self.bAdd, 6, 2, 1, 2, QtCore.Qt.AlignCenter)
        self.addWidget(self.bSubmit, 10, 5, 1, 1)
        