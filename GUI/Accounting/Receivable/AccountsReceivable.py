import sys
import datetime
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class AccountsReceivableView(QtWidgets.QGridLayout):
    def __init__(self, frame, customer_name):
        super().__init__()
        self.customer_name = customer_name
        self.frame = frame
        self.init_ui()
    
    def customer_Box(self):
        self.customer_groupbox = QtWidgets.QGroupBox("")
        
        customerGrid = QtWidgets.QGridLayout()
        
        self.lCustomer_name = QtWidgets.QLabel(self.customer_name)
        self.lCustomer_name.setStyleSheet(self.labelStyle)
        
        self.lAddress = QtWidgets.QLabel("Address: ")
        self.lAddress.setStyleSheet(self.addressStyle)
        
        self.lBalance = QtWidgets.QLabel("Balance: ")
        self.lBalance.setStyleSheet(self.addressStyle)
        
        customerGrid.setRowStretch(4,1)
        customerGrid.addWidget(self.lCustomer_name,1,1)
        #customerGrid.addWidget(self.lAddress,2,1)
        customerGrid.addWidget(self.lBalance,5,1)
        
        self.customer_groupbox.setLayout(customerGrid)
    def input_balance(self, balance):
        self.lBalance.setText("Balance: " + str(balance["balance"]))
    
    def input_details(self, details):
        self.lCustomer_name.setText(details["customer_name"])
        self.lAddress.setText("Address:" +details["address"])
    
    def input_ar_table(self, ar_results):
        for ar_row in ar_results:
            if ar_row["status"] != "Fully Paid":
                self.ar_Table.insertRow(self.ar_Table.rowCount())
                date = QtWidgets.QTableWidgetItem(ar_row["Date"])
                date.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ar_Table.setItem(self.ar_Table.rowCount()-1,0,date)
                
                inv_id = QtWidgets.QTableWidgetItem(str(ar_row["inv_id"]))
                inv_id.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ar_Table.setItem(self.ar_Table.rowCount()-1,1,inv_id)
                
                amount = QtWidgets.QTableWidgetItem(str(ar_row["amount"]))
                amount.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ar_Table.setItem(self.ar_Table.rowCount()-1,2,amount)
                
                payment = QtWidgets.QTableWidgetItem(str(ar_row["payment"]))
                payment.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ar_Table.setItem(self.ar_Table.rowCount()-1,3,payment)
                
                status = QtWidgets.QTableWidgetItem(str(ar_row["status"]))
                status.setFlags(QtCore.Qt.ItemIsEnabled)
                self.ar_Table.setItem(self.ar_Table.rowCount()-1,4,status)
        
    
    def account_receivable_Box(self):
        self.ar_groupbox = QtWidgets.QGroupBox("Partially and Unpaid Receivables")
        self.ar_groupbox.setStyleSheet("QGroupBox { font-size: 14pt; } ")
        
        arGrid = QtWidgets.QGridLayout()
        
        self.ar_Table = QtWidgets.QTableWidget()
        self.ar_Table.setColumnCount(5)
        self.ar_Table.setHorizontalHeaderLabels(["Date","Invoice #","Amount","Payment","Status"])
        self.ar_Table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.setStyleSheet( """QTableWidget {font-size: 12pt;} QHeaderView::section{font-size: 12pt; padding: 5px;}""")
        
        
        arGrid.addWidget(self.ar_Table,1,1)
        
        self.ar_groupbox.setLayout(arGrid)
        

    def init_ui(self):
    
        self.labelStyle = """QLabel { font-size: 14pt; color: black; padding: 4px;}"""
        self.addressStyle = """QLabel { font-size: 12pt; color: #666666; padding: 4px; }"""
        
        self.bMonthly = QtWidgets.QPushButton("Show Monthly")
        self.bMonthly.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; background-color: #5cb85c; border-color: #4cae4c;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #4baa4b; border-color: #409140;}""")

        
        
        self.bAdd_Payment = QtWidgets.QPushButton("Add Payment")
        self.bAdd_Payment.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; background-color: #5cb85c; border-color: #4cae4c;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #4baa4b; border-color: #409140;}""")
        
        self.bDel_Payment = QtWidgets.QPushButton("Delete Payment")
        self.bDel_Payment.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; 
        background-color: #d9534f;
        border-color: #d43f3a;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #d5443f; border-color: #d8504b;}""")
        
        
        #Making Customer Division
        self.customer_Box()
        self.account_receivable_Box()
        
        

        self.addWidget(self.customer_groupbox, 1, 1, 1, 1)
        self.addWidget(self.ar_groupbox, 1, 2, 1, 3)
        self.addWidget(self.bMonthly, 2, 1, 1, 1)
        self.addWidget(self.bAdd_Payment, 2, 2, 1, 1)
#        self.addWidget(self.lBalance, 2, 4, 1, 1)
        #self.addWidget(self.bDel_Payment, 2, 4, 1, 1)
#        #self.addWidget(self.lUsername, 3, 1, 1, 1)
#        self.addWidget(self.tUsername, 3, 1, 1, 2)
#        #self.addWidget(self.lPassword, 4, 1, 1, 1)
#        self.addWidget(self.tPassword, 4, 1, 1, 2)
#        self.addWidget(self.bLogin, 8, 1, 1, 2)
        