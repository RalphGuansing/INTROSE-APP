import sys
from PyQt5 import QtWidgets,QtCore

from InvoiceView import *


class AddInvoiceView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Invoice")
        self.added_products = []
        self.current_row = 0
        self.init_ui()

    def add_products(self):
        try:
            self.tProduct_Table.setItem(self.current_row,0,QtWidgets.QTableWidgetItem(str(self.tQuantity.value())))
            self.tProduct_Table.setItem(self.current_row,1,QtWidgets.QTableWidgetItem(str(self.tUnit.currentText())))
            self.tProduct_Table.setItem(self.current_row,2,QtWidgets.QTableWidgetItem(self.products[self.tProduct.currentIndex()].name))
            self.tProduct_Table.setItem(self.current_row,3,QtWidgets.QTableWidgetItem(str(self.tUnitPrice.text())))
            self.tProduct_Table.setItem(self.current_row,4,QtWidgets.QTableWidgetItem(str(int(self.tUnitPrice.text()) * int(self.tQuantity.value()))))
        except ValueError:
            print('Value Error: Wrong input type')

        self.tQuantity.setValue(0)
        self.tUnit.setText('')
        self.tUnitPrice.setText('')

        self.current_row += 1

    def init_ui(self):
        #Create Widgets
        
        invo_db = InvoiceDB()
        components = []
        client_list = []
        seller_list = []
        client_list = invo_db.get_client_name()
        seller_list = invo_db.get_seller_name()
        last_id = invo_db.get_last_id()
        invnum = last_id + 1
        self.termsList = ("30 days", "60 days", "90 days", "1 year")

        
        self.lInvoice_Details = QtWidgets.QLabel("INVOICE DETAILS")
        self.lInvoice_Details.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')
        
        self.lClient_Details = QtWidgets.QLabel("CLIENT DETAILS")
        self.lClient_Details.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')
        
        self.lCompany_Details = QtWidgets.QLabel("COMPANY DETAILS")
        self.lCompany_Details.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')
        
        self.linvoiceNum = QtWidgets.QLabel("Invoice Number: ")
        self.linvoiceNum.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tinvoiceNum = QtWidgets.QLabel(str(invnum))
        self.tinvoiceNum.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')			

        #Label#
        self.lBuyer = QtWidgets.QLabel("Buyer:")
        self.lBuyer.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        #TEXT INPUT#
        self.tBuyer = QtWidgets.QComboBox(self.frame)
        for x in range(len(client_list)):
            self.tBuyer.insertItem(x, str(client_list[x][0]))
        #self.tProduct_code.
        #self.tProduct_code.resize(280, 40)

        #Label#
        self.lDate = QtWidgets.QLabel("Date: ")
        self.lDate.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tDate = QtWidgets.QCalendarWidget()

		
		
        #Label#
        self.lSeller = QtWidgets.QLabel("Seller:")
        self.lSeller.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        #TEXT INPUT#
        self.tSeller = QtWidgets.QComboBox(self.frame)
        for x in range(len(seller_list)):
            self.tSeller.insertItem(x, seller_list[x])
        
		#Label#
        self.lAdd = QtWidgets.QLabel("Address:")
        self.lAdd.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')


        #TEXT INPUT#
        self.tAdd = QtWidgets.QLabel("")
        self.tAdd.setText(str(client_list[self.tBuyer.currentIndex][1]))	
		
        #Label#
        self.lTerms = QtWidgets.QLabel("Terms:")
        self.lTerms.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        #TEXT INPUT#
        self.tTerms = QtWidgets.QComboBox(self.frame)
        self.tTerms.insertItem(0, self.termsList[0])
        self.tTerms.insertItem(1, self.termsList[1])
        self.tTerms.insertItem(2, self.termsList[2])
        self.tTerms.insertItem(3, self.termsList[3])
		
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
        self.tProduct_Table.setColumnWidth(1, tablewidth / 8)
        self.tProduct_Table.setColumnWidth(2, tablewidth / 2)
        self.tProduct_Table.setColumnWidth(3, tablewidth / 8)		
        self.tProduct_Table.setColumnWidth(4, tablewidth / 8)
        self.tProduct_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)			

        self.Add_Product_Table = QtWidgets.QPushButton("Add Product")
        self.Add_Product_Table.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
		
        #self.lnumProducts = QtWidgets.QLabel("Number of Products:")
        #self.lnumProducts.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        #TEXT INPUT#
        #self.tnumProducts = QtWidgets.QSpinBox(self.frame)
        #self.tnumProducts.setFixedWidth(100)
		
        #self.lProduct = QtWidgets.QLabel("Product:")
        #self.lProduct.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')
        
        #TEXT INPUT#
        #self.tProduct = QtWidgets.QComboBox(self.frame)

        #Label#
        #self.lQuantity = QtWidgets.QLabel("Quantity:")
        #self.lQuantity.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')
        
        #TEXT INPUT#
        #self.tQuantity = QtWidgets.QSpinBox(self.frame)
        #self.tQuantity.setFixedWidth(100)
		
        self.ltaxedTotal = QtWidgets.QLabel("Total taxable: (system generated)")
        self.ltaxedTotal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)	
        
        self.ltaxTotal = QtWidgets.QLabel("Total tax: (system generated)")
        self.ltaxTotal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        self.lamountTotal = QtWidgets.QLabel("Total amount: (system generated)")
        self.lamountTotal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        self.lprofitTotal = QtWidgets.QLabel("Total profit: (system generated)")
        self.lprofitTotal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        
        self.lAddPoduct = QtWidgets.QLabel("PRODUCT DETAILS")
        self.lAddPoduct.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')
        
		#Label#
        self.lQuantity = QtWidgets.QLabel("Quantity: ")
        self.lQuantity.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tQuantity = QtWidgets.QSpinBox(self.frame)
        self.tQuantity.setFixedWidth(50)		

		#Label#
        self.lUnit = QtWidgets.QLabel("Unit: ")
        self.lUnit.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tUnit = QtWidgets.QComboBox(self.frame)
        self.tUnit.setFixedWidth(70)	
		
        #Label#
        self.lProduct = QtWidgets.QLabel("Product:")
        self.lProduct.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        #TEXT INPUT#
        self.tProduct = QtWidgets.QComboBox(self.frame)
        self.tProduct.setFixedWidth(200)		
        #self.tProduct_code.
        #self.tProduct_code.resize(280, 40)

        #Label#
        self.lUnitPrice = QtWidgets.QLabel("Unit Price: ")
        self.lUnitPrice.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tUnitPrice = QtWidgets.QLineEdit(self.frame)
        self.tUnitPrice.setFixedWidth(70)	
		


        self.bAdd = QtWidgets.QPushButton("Add")
        self.bAdd.setStyleSheet('QPushButton {color: white;background-color: #1db6d1;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 12px;min-width: 10em;padding: 4px;}')
        self.bAdd.setFixedWidth(200)
        self.bAdd.clicked.connect(self.add_products)
        
        self.bDelete = QtWidgets.QPushButton("Delete")
        self.bDelete.setStyleSheet('QPushButton {color: white;background-color: #6017a5;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 12px;min-width: 10em;padding: 4px;}')        
        self.bDelete.setFixedWidth(200)

        self.bBack = QtWidgets.QPushButton("Back")
        self.bBack.setStyleSheet('QPushButton {color: white;background-color: #d62f2f;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bBack.setFixedWidth(80)
        
        self.bSubmit = QtWidgets.QPushButton("Submit")
        self.bSubmit.setStyleSheet('QPushButton {color: white;background-color: #47c468;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bSubmit.setFixedWidth(200)


        self.setColumnStretch(7,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(21,1)

        #Add Widgets
        
        self.addWidget(self.lInvoice_Details, 0, 3, 1, 1)

        self.addWidget(self.linvoiceNum, 1, 3, 1, 1)
        self.addWidget(self.tinvoiceNum, 1, 4, 1, 1)
		
        self.addWidget(self.lDate, 2, 3, 1, 1)
        self.addWidget(self.tDate, 2, 4, 1, 1)
        
        self.addWidget(self.lClient_Details, 3, 3, 1, 1)        

        self.addWidget(self.lBuyer, 4, 3, 1, 1)
        self.addWidget(self.tBuyer, 4, 4, 1, 1)
		
        self.addWidget(self.lAdd, 5, 3, 1, 1)
        self.addWidget(self.tAdd, 5, 4, 1, 1)
        
        self.addWidget(self.lCompany_Details, 3, 5, 1, 1) 
        
        self.addWidget(self.lSeller, 4, 5, 1, 1)
        self.addWidget(self.tSeller, 4, 6, 1, 1)	

        self.addWidget(self.lTerms, 5, 5, 1, 1)
        self.addWidget(self.tTerms, 5, 6, 1, 1)			
	
        self.addWidget(self.lProduct_Table, 8, 5, 1, 1)	
        self.addWidget(self.tProduct_Table, 9, 5, 5, 2)			
        
        self.addWidget(self.ltaxedTotal, 14, 6, 1, 1)

        self.addWidget(self.ltaxTotal, 15,6, 1, 1)

        self.addWidget(self.lamountTotal, 16, 6, 1, 1)

        self.addWidget(self.lprofitTotal, 17, 6, 1, 1)
        
        self.addWidget(self.lAddPoduct, 8, 3, 1, 1)

        self.addWidget(self.lProduct, 9, 3, 1, 1)
        self.addWidget(self.tProduct, 9, 4, 1, 1)
		
        self.addWidget(self.lQuantity, 10, 3, 1, 1)
        self.addWidget(self.tQuantity, 10, 4, 1, 1)

        self.addWidget(self.lUnit, 11, 3, 1, 1)
        self.addWidget(self.tUnit, 11, 4, 1, 1)

        self.addWidget(self.lUnitPrice, 12, 3, 1, 1)
        self.addWidget(self.tUnitPrice, 12, 4, 1, 1)
        
        #self.addWidget(self.lProduct_Code, 1, 1, 1, 1)
        self.addWidget(self.bDelete, 13, 3, 1, 1)
        self.addWidget(self.bAdd, 13, 4, 1, 1)

        
        #self.addWidget(self.lProduct_Code, 1, 1, 1, 1)
        self.addWidget(self.bBack, 20, 3, 1, 1)
        self.addWidget(self.bSubmit, 21, 3, 1, 1)
        