import sys
from PyQt5 import QtWidgets,QtCore
from Inventory.InventoryView import *


class ViewInventoryList(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("View Inventory")
        self.init_ui()

    def add_table_entries(self):
        db_connection = InventoryDatabase()
        products = db_connection.get_product_list()
        for x in range(len(products)):
            self.tInventory_Table.setItem(x,0,QtWidgets.QTableWidgetItem(str(products[x].id)))
            self.tInventory_Table.setItem(x,1,QtWidgets.QTableWidgetItem(str(products[x].quantity)))
            self.tInventory_Table.setItem(x,2,QtWidgets.QTableWidgetItem(products[x].name))
            self.tInventory_Table.setItem(x,3,QtWidgets.QTableWidgetItem(products[x].supplier))
            self.tInventory_Table.setItem(x,4,QtWidgets.QTableWidgetItem(str(products[x].last_updated)))
        db_connection.close_connection()

    def init_ui(self):
        #Create Widgets
        self.lInventory_Details = QtWidgets.QLabel("INVENTORY LIST")
        self.lInventory_Details.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')


		#Inventory Table#
        self.tInventory_Table = QtWidgets.QTableWidget()
        self.tInventory_Table.setRowCount(10)
        self.tInventory_Table.setColumnCount(5)
        self.tInventory_Table.setHorizontalHeaderLabels(["Inventory Number", "Amount", "Product Name", "Supplier", "Date"])
        self.tInventory_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        tablewidth = self.tInventory_Table.width() + 4
        self.tInventory_Table.setColumnWidth(0, tablewidth / 6)
        self.tInventory_Table.setColumnWidth(1, tablewidth / 6)
        self.tInventory_Table.setColumnWidth(2, tablewidth / 2)
        self.tInventory_Table.setColumnWidth(3, tablewidth / 6)	
        self.tInventory_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)				

        self.Add_Inventory_Table = QtWidgets.QPushButton("Add Inventory")
        self.Add_Inventory_Table.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')	

        ###backend function
        self.add_table_entries()


        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(16,1)

        #Add Widgets
        self.addWidget(self.lInventory_Details, 0, 2, 1, 1)
        self.addWidget(self.tInventory_Table, 1, 2, 10, 3)     
        
        