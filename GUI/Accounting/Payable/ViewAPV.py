import sys
import datetime
import calendar
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore

class APVView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame  = frame
        self.init_ui()
        
    def set_Details(self, details):
        self.lDate.setText("Date: <div style='"+" text-indent: 30px;"+"'>"+details["Date"] +"</div>")
        self.lParticulars.setText("Particulars: <div style='"+" text-indent: 30px;"+"'>"+ details["name"] +"</div> ")
        self.lAPV_id.setText("APV #: <div style='"+" text-indent: 30px;"+"'>"+ str(details["id_apv"]) +"</div> ")
        self.lVouchers_payable.setText("Vouchers Payable #: <div style='"+" text-indent: 30px;"+"'>"+ str(details["amount"]) +"</div> ")
        
        
        
    def set_Columns(self, columns):
        for column in columns:
            self.Column_Table.insertRow(self.Column_Table.rowCount())
            self.Column_Table.setItem(self.Column_Table.rowCount()-1,0,QtWidgets.QTableWidgetItem(column["type_name"]))
            self.Column_Table.setItem(self.Column_Table.rowCount()-1,1,QtWidgets.QTableWidgetItem(str(column["type_value"])))

        
    
    def init_ui(self):
        self.labelStyle = """QLabel { font-size: 16pt; color: black; padding: 4px;}"""
        self.addressStyle = """QLabel { font-size: 14pt; color: #666666; padding: 4px;}"""
        

        self.lDate = QtWidgets.QLabel("Date: <div class='value'></div>")
        self.lDate.setStyleSheet(self.labelStyle)
        #self.lDate.setAlignment(QtCore.Qt.AlignCenter)
        
        self.lParticulars = QtWidgets.QLabel("Particulars: <div class='value'></div> ")
        self.lParticulars.setStyleSheet(self.addressStyle)
        
        self.lAPV_id = QtWidgets.QLabel("APV #: <div class='value'></div> ")
        self.lAPV_id.setStyleSheet(self.addressStyle)
        
        self.lVouchers_payable = QtWidgets.QLabel("Vouchers Payable #: <div class='value'></div> ")
        self.lVouchers_payable.setStyleSheet(self.addressStyle)
        

        self.Column_Table = QtWidgets.QTableWidget()
        self.Column_Table.setColumnCount(2)
        self.Column_Table.setHorizontalHeaderLabels(["Column Name","Value"])
        self.Column_Table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.Column_Table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.Column_Table.setStyleSheet( """QTableWidget {font-size: 12pt;} QHeaderView::section{font-size: 12pt; padding: 5px;}""")

        

        self.setRowStretch(8,1)
        
        self.addWidget(self.lDate, 1, 1, 1, 1)
        self.addWidget(self.lParticulars, 2, 1, 1, 1)
        self.addWidget(self.lAPV_id, 3, 1, 1, 1)
        self.addWidget(self.lVouchers_payable, 4, 1, 1, 1)
        self.addWidget(self.Column_Table, 1, 2, 8, 2)
        #self.addWidget(self.lEnding_Balance, 3, 2, 1, 1)
        #self.addWidget(self.bDetails, 3, 1, 1, 1)
    
        
class AccountsPayable_MonthlyView(QtWidgets.QGridLayout):
    def __init__(self, frame, accountspayable_info):
        super().__init__()
        #self.customer_name = customer_info["name"]
        self.selectedMonth = accountspayable_info["month"]
        self.selectedYear = accountspayable_info["year"]
        
        if self.selectedMonth == 1:
            self.beforeMonth = 12
            self.beforeYear = self.selectedYear - 1
        else:
            self.beforeMonth = self.selectedMonth - 1
            self.beforeYear = self.selectedYear
        
        
        self.frame = frame
        self.init_ui()
        

    def input_monthly_total(self, total):
        self.lTotal.setText("Total: " + str(total["total"]))
    
    def input_ap_table(self, ap_results):
        for ap_row in ap_results:
            self.ap_Table.insertRow(self.ap_Table.rowCount())
            self.ap_Table.setItem(self.ap_Table.rowCount()-1,0,QtWidgets.QTableWidgetItem(ap_row["Date"]))
            self.ap_Table.setItem(self.ap_Table.rowCount()-1,1,QtWidgets.QTableWidgetItem(ap_row["name"]))
            self.ap_Table.setItem(self.ap_Table.rowCount()-1,2,QtWidgets.QTableWidgetItem(str(ap_row["id_apv"])))
            self.ap_Table.setItem(self.ap_Table.rowCount()-1,3,QtWidgets.QTableWidgetItem(str(ap_row["amount"])))
        
    def init_ui(self):
    
        self.labelStyle = """QLabel { font-size: 16pt; color: black; padding: 4px;}"""
        self.addressStyle = """QLabel { font-size: 14pt; color: #666666; padding: 4px;}"""
        
        self.bDetails = QtWidgets.QPushButton("Details")
        self.bDetails.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; background-color: #5cb85c; border-color: #4cae4c;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #4baa4b; border-color: #409140;}""")
        
        self.lMonth_Year = QtWidgets.QLabel(calendar.month_name[self.selectedMonth] + " " + str(self.selectedYear))
        self.lMonth_Year.setStyleSheet(self.labelStyle)
        self.lMonth_Year.setAlignment(QtCore.Qt.AlignCenter)
        
        self.lTotal = QtWidgets.QLabel("Total:")
        self.lTotal.setStyleSheet(self.addressStyle)
        
#        self.account_receivable_Box()
        #self.label_balances()
        
#        self.setRowStretch(1,9)
#        self.setRowStretch(12,1)
        
        self.ap_Table = QtWidgets.QTableWidget()
        #self.ar_Table.setRowCount(10)
        self.ap_Table.setColumnCount(4)
        self.ap_Table.setHorizontalHeaderLabels(["Date","Particulars","APV #", "Vouchers Payable"])
        self.ap_Table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ap_Table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ap_Table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.ap_Table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.ap_Table.setStyleSheet( """QTableWidget {font-size: 12pt;} QHeaderView::section{font-size: 12pt; padding: 5px;}""")

#        self.addWidget(self.customer_groupbox, 1, 1, 1, 1)
        #self.addWidget(self.lCustomer_name, 1, 1, 1, 1)
        self.addWidget(self.lMonth_Year, 1, 2, 1, 1)
        self.addWidget(self.ap_Table, 2, 1, 1, 3)
        self.addWidget(self.lTotal, 3, 3, 1, 1)
        #self.addWidget(self.lEnding_Balance, 3, 2, 1, 1)
        self.addWidget(self.bDetails, 3, 1, 1, 1)
#        #self.addWidget(self.lUsername, 3, 1, 1, 1)
#        self.addWidget(self.tUsername, 3, 1, 1, 2)
#        #self.addWidget(self.lPassword, 4, 1, 1, 1)
#        self.addWidget(self.tPassword, 4, 1, 1, 2)
#        self.addWidget(self.bLogin, 8, 1, 1, 2)