import sys
import datetime
import calendar
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


class input_month_year(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.init_ui()
    
    def init_ui(self):
        now = datetime.date.today()
        
        self.labelStyle = """QLabel { font-size: 14pt; color: black; padding: 4px;}"""
        self.addressStyle = """QLabel { font-size: 12pt; color: #666666; padding: 4px; font-family:Montserrat;}"""
        
        
        self.lMonth = QtWidgets.QLabel("Month: ")
        self.lMonth.setStyleSheet(self.labelStyle)
        
        self.month_choice = QtWidgets.QSpinBox()
        self.month_choice.setRange(1,12)
        self.month_choice.setValue(now.month)
        self.month_choice.setStyleSheet('QSpinBox { font-size: 12pt; padding: 2px;}')
        
        
        self.lYear = QtWidgets.QLabel("Year: ")
        self.lYear.setStyleSheet(self.labelStyle)
        
        self.year_choice = QtWidgets.QSpinBox()
        self.year_choice.setRange(0,9999)
        self.year_choice.setValue(now.year)
        self.year_choice.setStyleSheet('QSpinBox { font-size: 12pt; padding: 2px;}')
        
        self.top_box = QtWidgets.QGroupBox("")
        Ggrid = QtWidgets.QGridLayout()
        Ggrid.addWidget(self.lMonth,1,1)
        Ggrid.addWidget(self.month_choice,1,2)
        Ggrid.addWidget(self.lYear,2,1)
        Ggrid.addWidget(self.year_choice,2,2)
        self.top_box.setLayout(Ggrid)
        
        self.setRowStretch(4,1)
#        self.setColumnStretch(0,1)
#        self.setColumnStretch(3,1)
        
        self.bSubmit = QtWidgets.QPushButton("Submit")
        self.bSubmit.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; background-color: #5cb85c; border-color: #4cae4c;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #4baa4b; border-color: #409140;}""")
        
        self.bCancel = QtWidgets.QPushButton("Cancel")
        self.bCancel.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; 
        background-color: #d9534f;
        border-color: #d43f3a;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #d5443f; border-color: #d8504b;}""")
        
        
        self.addWidget(self.top_box,1,1,2,2)
        self.addWidget(self.bSubmit,3,1)
        self.addWidget(self.bCancel,3,2)
        
        
        

class AccountsReceivable_MonthlyView(QtWidgets.QGridLayout):
    def __init__(self, frame,customer_info):
        super().__init__()
        self.customer_name = customer_info["name"]
        self.selectedMonth = customer_info["month"]
        self.selectedYear = customer_info["year"]
        
        if self.selectedMonth == 1:
            self.beforeMonth = 12
            self.beforeYear = self.selectedYear - 1
        else:
            self.beforeMonth = self.selectedMonth - 1
            self.beforeYear = self.selectedYear
        
        
        self.frame = frame
        self.init_ui()
        

    def input_beg_balance(self, balance):
        self.lBeginning_Balance.setText("Beginning Balance: " + str(balance["balance"]))
    def input_end_balance(self, balance):
        self.lEnding_Balance.setText("Ending Balance: " + str(balance["balance"]))
    
    def input_ar_table(self, ar_results):
        for ar_row in ar_results:
            self.ar_Table.insertRow(self.ar_Table.rowCount())
            self.ar_Table.setItem(self.ar_Table.rowCount()-1,0,QtWidgets.QTableWidgetItem(ar_row["Date"]))
            self.ar_Table.setItem(self.ar_Table.rowCount()-1,1,QtWidgets.QTableWidgetItem(str(ar_row["inv_id"])))
            self.ar_Table.setItem(self.ar_Table.rowCount()-1,2,QtWidgets.QTableWidgetItem(str(ar_row["amount"])))
            
            if ar_row["date_paid"] is not None:
                self.ar_Table.setItem(self.ar_Table.rowCount()-1,3,QtWidgets.QTableWidgetItem(str(ar_row["date_paid"])))
            if ar_row["pr_id"] is not None:
                self.ar_Table.setItem(self.ar_Table.rowCount()-1,4,QtWidgets.QTableWidgetItem(str(ar_row["pr_id"])))
            if ar_row["payment"] is not None:
                self.ar_Table.setItem(self.ar_Table.rowCount()-1,5,QtWidgets.QTableWidgetItem(str(ar_row["payment"])))
        
    def label_balances(self):
        self.lCustomer_name = QtWidgets.QLabel(self.customer_name)
        self.lCustomer_name.setStyleSheet(self.labelStyle)
        self.lMonth_Year = QtWidgets.QLabel(calendar.month_name[self.selectedMonth] + " " + str(self.selectedYear))
        self.lMonth_Year.setStyleSheet(self.labelStyle)
        self.lMonth_Year.setAlignment(QtCore.Qt.AlignCenter)
        self.lBeginning_Balance = QtWidgets.QLabel("Beginning Balance:")
        self.lBeginning_Balance.setStyleSheet(self.addressStyle)
        self.lEnding_Balance = QtWidgets.QLabel("Ending Balance:")
        self.lEnding_Balance.setStyleSheet(self.addressStyle)
        
    def init_ui(self):
    
        self.labelStyle = """QLabel { font-size: 14pt; color: black; padding: 4px;}"""
        self.addressStyle = """QLabel { font-size: 10pt; color: #666666; padding: 4px;}"""
        
        self.bAdd_Payment = QtWidgets.QPushButton("Add Payment")
        self.bAdd_Payment.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; background-color: #5cb85c; border-color: #4cae4c;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #4baa4b; border-color: #409140;}""")
        
        
#        self.account_receivable_Box()
        self.label_balances()
        
#        self.setRowStretch(1,9)
#        self.setRowStretch(12,1)
        
        self.ar_Table = QtWidgets.QTableWidget()
        #self.ar_Table.setRowCount(10)
        self.ar_Table.setColumnCount(6)
        self.ar_Table.setHorizontalHeaderLabels(["Date","Invoice #","Amount", "Date Paid","PR no.", "Payment"])
        self.ar_Table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.horizontalHeader().setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.horizontalHeader().setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.ar_Table.setStyleSheet( """QTableWidget {font-size: 12pt;} QHeaderView::section{font-size: 12pt; padding: 5px;}""")

#        self.addWidget(self.customer_groupbox, 1, 1, 1, 1)
        self.addWidget(self.lCustomer_name, 1, 1, 1, 1)
        self.addWidget(self.lMonth_Year, 1, 2, 1, 1)
        self.addWidget(self.ar_Table, 2, 1, 1, 3)
        self.addWidget(self.lBeginning_Balance, 3, 1, 1, 1)
        self.addWidget(self.lEnding_Balance, 3, 2, 1, 1)
        self.addWidget(self.bAdd_Payment, 3, 3, 1, 1)
#        #self.addWidget(self.lUsername, 3, 1, 1, 1)
#        self.addWidget(self.tUsername, 3, 1, 1, 2)
#        #self.addWidget(self.lPassword, 4, 1, 1, 1)
#        self.addWidget(self.tPassword, 4, 1, 1, 2)
#        self.addWidget(self.bLogin, 8, 1, 1, 2)
        