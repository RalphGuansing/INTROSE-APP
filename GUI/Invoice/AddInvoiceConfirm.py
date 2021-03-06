import sys
from PyQt5 import QtWidgets,QtCore
from Invoice.InvoiceView import *

class AddInvoiceConfirm(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("View Invoice")
        self.init_ui()

    def checkout_info(self, amount, vat, taxable, profit, info):
        self.lamountTotal.setText("Total amount: " + str(amount))
        self.ltaxedTotal.setText("Total taxable: "  + str(taxable))
        self.ltaxTotal.setText("Total tax: "  + str(vat))
        self.lprofitTotal.setText("Total profit: "  + str(profit))

        self.lInvNum.setText("Invoice No.  " + str(info["invoice_id"]))
        self.lChargedTo.setText("Charged to: " + str(info["buyer"]))
        self.lDate.setText("Date: " + str(info["date"]))
        self.lSeller.setText("Seller: " + str(info["seller"]))
        self.lTerms.setText("Terms: " + str(info["term"]))
        self.lAddress.setText("Address: " + str(info["Address"]))

    def delete_info(self, invoice_number):
        invo_db = InvoiceDB()

        invoice_query = []
        invoice_query = invo_db.get_query(invoice_number)
        user_info = {'invoice_id': invoice_query[0], 'buyer': invoice_query[1][0], 'date': invoice_query[3], 'seller': invoice_query[2], 'term': invoice_query[4], 'Address': invoice_query[1][1]}
        self.checkout_info(invoice_query[6], invoice_query[8], invoice_query[9], invoice_query[10], user_info)

        for row in range(len(invoice_query[11])):

            self.add_to_table(row,0, str(invoice_query[11][row][4]))
            self.add_to_table(row,1, invoice_query[11][row][3])
            self.add_to_table(row,2, invoice_query[11][row][2])
            self.add_to_table(row,3, str(invoice_query[11][row][6]))
            self.add_to_table(row,4, str(invoice_query[11][row][7]))

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

		
        self.ltaxedTotal = QtWidgets.QLabel("Total taxable: (system generated)")
        self.ltaxedTotal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)		

        self.ltaxTotal = QtWidgets.QLabel("Total tax: (system generated)")
        self.ltaxTotal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)	
		
        self.lamountTotal = QtWidgets.QLabel("Total amount: (system generated)")
        self.lamountTotal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)	
		
        self.lprofitTotal = QtWidgets.QLabel("Total profit: (system generated)")
        self.lprofitTotal.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)	

        self.lConfirmation = QtWidgets.QLabel("Please confirm if these values are correct")
        self.lTerms.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        
        self.bAddInvoice = QtWidgets.QPushButton("Confirm")
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
        self.addWidget(self.lConfirmation, 5, 2, 1, 1)	        
        self.addWidget(self.tProduct_Table, 6, 2, 3, 3)
        
        self.addWidget(self.ltaxedTotal, 9, 4, 1, 1)

        self.addWidget(self.ltaxTotal, 10, 4, 1, 1)

        self.addWidget(self.lamountTotal, 11, 4, 1, 1)
		
        self.addWidget(self.lprofitTotal, 12, 4, 1, 1)
        
        self.addWidget(self.bAddInvoice, 15, 3, 1, 1)

class WindowFrame(QtWidgets.QWidget):
    def __init__(self, layout):
        super().__init__()
        self.setWindowTitle("Window")
        self.layout = layout(self)
        self.setLayout(self.layout)

class ConfirmWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ConfirmWindow, self).__init__(parent)
        self.resize(800,600)
        self.layout = WindowFrame(AddInvoiceConfirm)
        self.setCentralWidget(self.layout)        
        