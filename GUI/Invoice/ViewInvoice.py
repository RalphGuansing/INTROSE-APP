import sys
from PyQt5 import QtWidgets,QtCore

from InvoiceView import *



class ViewInvoice(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("View Invoice")
        self.init_ui()

    def get_invoice(self, invoice_number):
        total_amount = 0
        total_nonvat = 0
        total_vat = 0
        total_taxable = 0
        total_profit = 0
        invo_db = InvoiceDB()
        self.invoice_query = []
        invoice_query = invo_db.get_query(invoice_number)

        for total_temp in invoice_query[11]:

            total_amount += total_temp[7]
            total_nonvat += total_temp[8]
            total_vat += total_temp[9]
            total_taxable += total_temp[10]
            total_profit += total_temp[11]

        for row in range(len(invoice_query[11])):
            self.tProduct_Table.setItem(row,0,QtWidgets.QTableWidgetItem(str(invoice_query[11][row][4])))
            self.tProduct_Table.setItem(row,1,QtWidgets.QTableWidgetItem(invoice_query[11][row][3]))
            self.tProduct_Table.setItem(row,2,QtWidgets.QTableWidgetItem(invoice_query[11][row][2]))
            self.tProduct_Table.setItem(row,3,QtWidgets.QTableWidgetItem(str(invoice_query[11][row][6])))
            self.tProduct_Table.setItem(row,4,QtWidgets.QTableWidgetItem(str(invoice_query[11][row][7])))

        self.lamountTotal.setText("Total amount: " + str(total_amount))
        self.ltaxedTotal.setText("Total taxable: "  + str(total_taxable))
        self.ltaxTotal.setText("Total tax: "  + str(total_vat))
        self.lprofitTotal.setText("Total profit: "  + str(total_profit))

        self.lInvNum.setText("Invoice No.  " + str(invoice_query[0]))
        self.lChargedTo.setText("Charged to: " + str(invoice_query[1][0]))
        self.lDate.setText("Date: " + str(invoice_query[3]))
        self.lSeller.setText("Seller: " + str(invoice_query[2]))
        self.lTerms.setText("Terms: " + str(invoice_query[4]))
        self.lAddress.setText("Address: " + str(invoice_query[1][1]))

        invo_db.close_connection()
    
    def add_to_table(self, row, column, text):
        self.tProduct_Table.setItem(row,column,QtWidgets.QTableWidgetItem(text))

    def init_ui(self):

        #Create Widgets
        self.lInvoice_Details = QtWidgets.QLabel("INVOICE")
        self.lInvoice_Details.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')

		#Label#
        self.lInvNum = QtWidgets.QLabel("Invoice No.  ")
        self.lInvNum.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')	      
		
		#Label#
        self.lChargedTo = QtWidgets.QLabel("Charged to: ")
        self.lChargedTo.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')		

		#Label#
        self.lDate = QtWidgets.QLabel("Date: ")
        self.lDate.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')	

		#Label#
        self.lSeller = QtWidgets.QLabel("Seller: ")
        self.lSeller.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')		
		
		#Label#
        self.lTerms = QtWidgets.QLabel("Terms: ")
        self.lTerms.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')
		
		#Label#
        self.lAddress = QtWidgets.QLabel("Address: ")
        self.lAddress.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')		

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
        # self.tProduct_Table.setItem(0, 0, component_item.quantity)
        # self.tProduct_Table.setItem(1, 1, "unit")
        # self.tProduct_Table.setItem(2, 2, component_item.name)
        # self.tProduct_Table.setItem(3, 3, component_item.unitprice)
        # self.tProduct_Table.setItem(4, 4, self.totalamount)


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

        self.bBack = QtWidgets.QPushButton("Back")
        self.bBack.setStyleSheet('QPushButton {color: white;background-color: #d62f2f;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bBack.setFixedWidth(80)
        
        self.bAddInvoice = QtWidgets.QPushButton("Add Invoice")
        self.bAddInvoice.setStyleSheet('QPushButton {color: white;background-color: #47c468;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bAddInvoice.setFixedWidth(200)


        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(13,1)

        #Add Widgets
        
        self.addWidget(self.lInvoice_Details, 0, 2, 1, 1)
		
        self.addWidget(self.lInvNum, 1, 2, 1, 1)
        self.addWidget(self.lDate, 1, 4, 1, 1)		
        self.addWidget(self.lChargedTo, 2, 2, 1, 1)	
        self.addWidget(self.lSeller, 2, 4, 1, 1)		
        self.addWidget(self.lAddress, 3, 2, 1, 1)			
        self.addWidget(self.lTerms, 3, 4, 1, 1)	
        self.addWidget(self.lProduct_Table, 4, 2, 1, 1)	        
        self.addWidget(self.tProduct_Table, 5, 2, 3, 3)
        
        self.addWidget(self.ltaxedTotal, 9, 4, 1, 1)

        self.addWidget(self.ltaxTotal, 10, 4, 1, 1)

        self.addWidget(self.lamountTotal, 11, 4, 1, 1)
		
        self.addWidget(self.lprofitTotal, 12, 4, 1, 1)
        
        self.addWidget(self.bBack, 14, 2, 1, 1)
        
        self.addWidget(self.bAddInvoice, 15, 2, 1, 1)        
        