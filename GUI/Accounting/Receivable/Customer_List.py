import sys
from PyQt5 import QtWidgets,QtCore


class Customer_ListView(QtWidgets.QGridLayout):
    def __init__(self, frame, customer_names):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Home Page")
        self.init_ui()
        
        if customer_names is not None: 
            self.customer_names = [i["customer_name"] for i in customer_names]
            self.input_customers(self.customer_names)
    
    def refresh_customer_list(self):
        self.tCustomer_table.clearContents()
        self.tCustomer_table.setRowCount(0)
        searchString = self.tCustomer.text().lower()
        
        customer_dict = {}
        for nameString in self.customer_names:
            lower = nameString.lower()
            orig = nameString
            customer_dict[lower] = orig
        
        matching = [list(customer_dict.values())[index] for index,s in enumerate(list(customer_dict.keys())) if searchString in s]
        
        self.input_customers(matching)
    
    def input_customers(self, customers):
        for customer in customers:
            self.tCustomer_table.insertRow(self.tCustomer_table.rowCount())
            self.tCustomer_table.setItem(self.tCustomer_table.rowCount()-1,0,QtWidgets.QTableWidgetItem(customer))

    def init_ui(self):
        #Create Widgets
        self.tCustomer = QtWidgets.QLineEdit(self.frame)
        self.tCustomer.setStyleSheet('QLineEdit { font-size: 14pt; padding: 7px; border-radius:5px;}')
        self.tCustomer.setPlaceholderText("Search for a Customer")
        self.tCustomer.textChanged.connect(self.refresh_customer_list)
        
        #Customer Table
        self.tCustomer_table = QtWidgets.QTableWidget()
        self.tCustomer_table.setColumnCount(1)
        self.tCustomer_table.setHorizontalHeaderLabels(["Customers"])
        self.tCustomer_table.setStyleSheet( """QTableWidget {font-size: 14pt;}""")
        self.tCustomer_table.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.tCustomer_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tCustomer_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tCustomer_table.verticalHeader().setVisible(False)
        self.tCustomer_table.horizontalHeader().setVisible(False)
        
        #Setting Alignment
        self.setColumnStretch(1,1)
        self.setColumnStretch(2,1)
        self.setColumnStretch(3,6)
        self.setColumnStretch(4,1)
        self.setColumnStretch(5,1)
        self.setColumnStretch(0,6)
        self.setColumnStretch(6,6)
        
        #Add Widgets
        self.addWidget(self.tCustomer, 1,3,1,1)
        self.addWidget(self.tCustomer_table, 2,1,1,5)
