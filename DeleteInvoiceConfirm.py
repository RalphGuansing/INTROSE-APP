import sys
from PyQt5 import QtWidgets,QtCore


class DeleteInvoiceConfirm(QtWidgets.QGridLayout):
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


        self.bBack = QtWidgets.QPushButton("Go back")
        self.bBack.setStyleSheet('QPushButton { font-size: 14px; border-radius:10px ;padding: 10px;}')
        self.bBack.setFixedWidth(80)
        
        self.bConfirm = QtWidgets.QPushButton("Confirm")
        self.bConfirm.setStyleSheet('QPushButton {color: white;background-color: #47c468;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bConfirm.setFixedWidth(200)


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

        self.addWidget(self.lConfirmation, 14, 2, 1, 1)
        
        self.addWidget(self.bBack, 15, 2, 1, 1)
        
        self.addWidget(self.bConfirm, 15, 3, 1, 1)

class WindowFrame(QtWidgets.QWidget):
    def __init__(self, layout):
        super().__init__()
        self.setWindowTitle("Window")
        self.layout = layout(self)
        self.setLayout(self.layout)

class ConfirmWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ConfirmWindow, self).__init__(parent)
        self.resize(420,420)
        self.layout = WindowFrame(AddInvoiceConfirm)
        self.setCentralWidget(self.layout)        
        