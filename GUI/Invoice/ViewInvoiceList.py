import sys
from PyQt5 import QtWidgets,QtCore
from Invoice.InvoiceView import *
from Invoice.AddInvoiceConfirm import *
from Invoice.EditInvoice import *

class ViewInvoice(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("View Invoice")
        self.init_ui()

    def error_message(self, message):
        infoBox = QtWidgets.QMessageBox()
        infoBox.setIcon(QtWidgets.QMessageBox.Warning)
        infoBox.setWindowTitle('Error')
        infoBox.setText(message)
        infoBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        infoBox.setEscapeButton(QtWidgets.QMessageBox.Close) 
        infoBox.exec_()

    def edit_invoice(self):
        self.edit_window = EditWindow()
        self.edit_window.show()

    def get_all_invoice(self):
        invo_db = InvoiceDB()
        all_invoice_list = invo_db.get_all_invoice()
        
        for row in range(len(all_invoice_list)):
            buyer_name = invo_db.get_client_name(all_invoice_list[row][1])
            self.tProduct_Table.setItem(row,0,QtWidgets.QTableWidgetItem(str(all_invoice_list[row][0])))
            self.tProduct_Table.setItem(row,1,QtWidgets.QTableWidgetItem(str(all_invoice_list[row][6])))
            self.tProduct_Table.setItem(row,2,QtWidgets.QTableWidgetItem(buyer_name[0]))
            self.tProduct_Table.setItem(row,3,QtWidgets.QTableWidgetItem(all_invoice_list[row][3]))

        total = []
        total = invo_db.get_total()
        self.lamountTotal.setText("Total amount: " + str(total[0]))
        self.ltaxedTotal.setText("Total taxable: "  + str(total[2]))
        self.ltaxTotal.setText("Total tax: "  + str(total[3]))
        self.lprofitTotal.setText("Total profit: "  + str(total[4]))

        invo_db.close_connection()

    def delete_invoice_confirm(self):
        indices = self.tProduct_Table.selectionModel().selectedRows()
        try:
            for index in sorted(indices):
                self.confirm_window = ConfirmWindow()
                self.confirm_window.show()
                self.confirm_window.layout.layout.bAddInvoice.clicked.connect(self.delete_invoice)
                self.confirm_window.layout.layout.delete_info(self.tProduct_Table.item(index.row(),0).text())
        except (IndexError,AttributeError):
            self.error_message('Invalid Row')

    def delete_invoice(self):
        print(self.tProduct_Table.item(0,0).text())
        print(self.tProduct_Table.selectionModel().selectedRows())
        invo_db = InvoiceDB()
        model = self.tProduct_Table
        total_temp = []
        indices = self.tProduct_Table.selectionModel().selectedRows()

        for index in sorted(indices):
            invo_db.delete_row(invoice_number=self.tProduct_Table.item(index.row(),0).text())
            model.removeRow(index.row())

        self.confirm_window.close()
        total = []
        total = invo_db.get_total()
        self.lamountTotal.setText("Total amount: " + str(total[0]))
        self.ltaxedTotal.setText("Total taxable: "  + str(total[2]))
        self.ltaxTotal.setText("Total tax: "  + str(total[3]))
        self.lprofitTotal.setText("Total profit: "  + str(total[4]))

        invo_db.close_connection()

    def init_ui(self):
        #Create Widgets
        self.lInvoice_Details = QtWidgets.QLabel("INVOICE LIST")
        self.lInvoice_Details.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')
        

        self.bEditInvoice = QtWidgets.QPushButton("Edit Invoice")
        self.bEditInvoice.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bEditInvoice.setFixedWidth(200)
        self.bEditInvoice.clicked.connect(self.edit_invoice)

        #self.bDelInvoice = QtWidgets.QPushButton("Delete Invoice")
        #self.bDelInvoice.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        #self.bDelInvoice.setFixedWidth(200)
        #self.bDelInvoice.clicked.connect(self.delete_invoice_confirm)

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

        self.bBack = QtWidgets.QPushButton("Back")
        self.bBack.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bBack.setFixedWidth(200)


        self.get_all_invoice()

        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(16,1)

        #Add Widgets
        
        self.addWidget(self.lInvoice_Details, 0, 2, 1, 1)
        #self.addWidget(self.bEditInvoice, 2, 6, 1, 1)
        #self.addWidget(self.bDelInvoice, 3, 6, 1, 1)

		
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

        #self.addWidget(self.bBack, 15, 4, 1, 1)        
        