import sys
from PyQt5 import QtWidgets,QtCore


class ViewInvoice(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("View Invoice")
        self.init_ui()

    def init_ui(self):
        #Create Widgets
        self.lInvoice_Details = QtWidgets.QLabel("INVOICE LIST")
        self.lInvoice_Details.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')


        self.bEditInvoice = QtWidgets.QPushButton("Edit Invoice")
        self.bEditInvoice.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bEditInvoice.setFixedWidth(200)


        self.bDelInvoice = QtWidgets.QPushButton("Delete Invoice")
        self.bDelInvoice.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bDelInvoice.setFixedWidth(200)

		#Product Table#
        self.tProduct_Table = QtWidgets.QTableWidget()
        self.tProduct_Table.setRowCount(10)
        self.tProduct_Table.setColumnCount(4)
        self.tProduct_Table.setHorizontalHeaderLabels(["Invoice Number", "Amount", "Buyer", "Date"])
        self.tProduct_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        tablewidth = self.tProduct_Table.width() + 4
        self.tProduct_Table.setColumnWidth(0, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(1, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(2, tablewidth / 2)
        self.tProduct_Table.setColumnWidth(3, tablewidth / 6)					

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

        self.bBack = QtWidgets.QPushButton("Back")
        self.bBack.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bBack.setFixedWidth(200)


        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(16,1)

        #Add Widgets
        
        self.addWidget(self.lInvoice_Details, 0, 2, 1, 1)
        self.addWidget(self.bEditInvoice, 2, 6, 1, 1)
        self.addWidget(self.bDelInvoice, 3, 6, 1, 1)

		
        self.addWidget(self.tProduct_Table, 1, 2, 10, 3)
					
       #self.addWidget(self.lnumProducts, 7, 3, 1, 1)
       #self.addWidget(self.tnumProducts, 7, 4, 1, 1)
        
       #self.addWidget(self.lProduct, 8, 3, 1, 1)
       #self.addWidget(self.tProduct, 8, 4, 1, 1)

       #self.addWidget(self.lQuantity, 9, 3, 1, 1)
       #self.addWidget(self.tQuantity, 9, 4, 1, 1)
        
        self.addWidget(self.ltaxedTotal, 11, 4, 1, 1)

        self.addWidget(self.ltaxTotal, 12, 4, 1, 1)

        self.addWidget(self.lamountTotal, 13, 4, 1, 1)
		
        self.addWidget(self.lprofitTotal, 14, 4, 1, 1)

        self.addWidget(self.bBack, 15, 4, 1, 1)        
        