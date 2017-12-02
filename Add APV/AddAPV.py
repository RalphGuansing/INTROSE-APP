import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QHeaderView


class AddAPVView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.init_ui()
        
#    def createPreview_group(self):
#        self.preview_GroupBox = QtWidgets.QGroupBox("Preview")
#        
#        self.pDate = QtWidgets.QLabel("Date: "+ self.tDate.text())
#        self.pDate.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')
#        
#        self.pName = QtWidgets.QLabel("Particulars: "+ self.tName.text())
#        self.pName.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')
#        
#        self.pId = QtWidgets.QLabel("APV#: "+ self.tId.text())
#        self.pId.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')
#        
#        self.pAmount = QtWidgets.QLabel("Vouchers Payable: "+ self.tAmount.text())
#        self.pAmount.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')
#        
#        self.column_data = []
#        self.pColumn_Table = QtWidgets.QTableWidget()
#        #self.pColumn_Table.setRowCount(1)
#        self.pColumn_Table.setColumnCount(2)
#        self.pColumn_Table.setHorizontalHeaderLabels(["Column Name", "Value"])
#        self.pColumn_Table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
#        self.pColumn_Table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
#        
#        Ggrid = QtWidgets.QGridLayout()
#        Ggrid.addWidget(self.pDate, 1, 1)
#        Ggrid.addWidget(self.pName, 2, 1)
#        Ggrid.addWidget(self.pId, 3, 1)
#        Ggrid.addWidget(self.pAmount, 4, 1)
#        Ggrid.addWidget(self.pColumn_Table, 5,1)
#        
#        #Ggrid.setColumnStretch(7,4)
#        Ggrid.setRowStretch(5,1)
#        self.preview_GroupBox.setLayout(Ggrid)
        

    def createColumn_group(self):
        self.column_name_GroupBox = QtWidgets.QGroupBox("Columns")
        self.column_name_GroupBox.setStyleSheet(""" QGroupBox{font-size: 10pt;} """)
        
        self.column_data = []
        self.column_data_val = []
        self.pColumn_Table = QtWidgets.QTableWidget()
        #self.pColumn_Table.setRowCount(1)
        self.pColumn_Table.setColumnCount(2)
        self.pColumn_Table.setHorizontalHeaderLabels(["Column Name", "Value"])
        self.pColumn_Table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.pColumn_Table.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.pColumn_Table.setStyleSheet( """QTableWidget {font-size: 12pt;} QHeaderView::section{font-size: 13pt; padding: 5px;}""")
        
        self.bColumn_Add = QtWidgets.QPushButton("Add")
        self.bColumn_Add.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        self.bColumn_Delete = QtWidgets.QPushButton("Delete")
        self.bColumn_Delete.setStyleSheet('QPushButton { font-size: 12pt; padding: 10px;}')
        
        Ggrid = QtWidgets.QGridLayout()
        Ggrid.addWidget(self.pColumn_Table, 1, 1, 3, 4)
        Ggrid.addWidget(self.bColumn_Add, 4, 1, 1, 2)
        Ggrid.addWidget(self.bColumn_Delete, 4, 3, 1, 2)
#        Ggrid.setColumnStretch(5,1)
#        Ggrid.setRowStretch(3,1)
        self.column_name_GroupBox.setLayout(Ggrid)

    
    def add_column(self, column_names):
        for column_name in column_names:
            self.pColumn_Table.insertRow(self.pColumn_Table.rowCount())
            self.pColumn_Table.setItem(self.pColumn_Table.rowCount()-1,0,QtWidgets.QTableWidgetItem(column_name))
            self.column_data.append(column_name)
        #self.pColumn_Table.setItem(self.pColumn_Table.rowCount()-1,1,QtWidgets.QTableWidgetItem(self.tColumn_val.text()))
        
#        temp = {}
#        
#        temp["name"] = self.tColumn_name.text()
#        temp["value"] = self.tColumn_val.text()
#        
#        self.column_data.append(temp)
#        
#        print(self.column_data)
    
    def get_items(self):
        
        items = {}
        items["date"] = self.tDate.text()
        items["name"] = self.tName.text()
        items["id_apv"] = self.tId.text()
        items["amount"] = self.tAmount.text()
        
        
        print(self.column_data)
        for i in range(len(self.column_data)):
            print(self.pColumn_Table.item(i,1).text())
            self.column_data_val.append(self.pColumn_Table.item(i,1).text())
        
        
        
        items["column_names"] = self.column_data
        items["column_val"] = self.column_data_val
        
        print(items)
        return items
    
#    def preview_items(self):
#        self.pDate.clear()
#        self.pDate.setText("Date: "+ self.tDate.text())
#        self.pName.clear()
#        self.pName.setText("Particulars: "+ self.tName.text())
#        self.pId.clear()
#        self.pId.setText("APV#: "+ self.tId.text())
#        self.pAmount.clear()
#        self.pAmount.setText("Vouchers Payable: "+ self.tAmount.text())
    
    
    def createDetails_group(self):
        self.APV_details_GroupBox = QtWidgets.QGroupBox("")
        
        textboxSize = 350
        
        labelStyle = 'QLabel { font-size: 12pt; padding: 10px; font-weight: bold;}'
        textboxStyle = 'QLineEdit { font-size: 12pt; padding: 2px;}'
        
        
        self.lDate = QtWidgets.QLabel("Date:")
        #self.lDate.setAlignment(QtCore.Qt.AlignRight)
        self.lDate.setStyleSheet(labelStyle)
        self.tDate = QtWidgets.QLineEdit(self.frame)
        self.tDate.setStyleSheet(textboxStyle)
        #self.tDate.textChanged.connect(self.preview_items)
        self.tDate.setFixedWidth(textboxSize)

        self.lName = QtWidgets.QLabel("Particulars:")
        #self.lName.setAlignment(QtCore.Qt.AlignRight)
        self.lName.setStyleSheet(labelStyle)
        self.tName = QtWidgets.QLineEdit(self.frame)
        self.tName.setStyleSheet(textboxStyle)
        #self.tName.textChanged.connect(self.preview_items)
        self.tName.setFixedWidth(textboxSize)
        
        self.lId = QtWidgets.QLabel("APV #:")
        #self.lId.setAlignment(QtCore.Qt.AlignRight)
        self.lId.setStyleSheet(labelStyle)
        self.tId = QtWidgets.QLineEdit(self.frame)
        self.tId.setStyleSheet(textboxStyle)
        #self.tId.textChanged.connect(self.preview_items)
        self.tId.setFixedWidth(textboxSize)

        self.lAmount = QtWidgets.QLabel("Vouchers Payable:")
        #self.lAmount.setAlignment(QtCore.Qt.AlignRight)
        self.lAmount.setStyleSheet(labelStyle)
        self.tAmount = QtWidgets.QLineEdit(self.frame)
        self.tAmount.setStyleSheet(textboxStyle)
        #self.tAmount.textChanged.connect(self.preview_items)
        self.tAmount.setFixedWidth(textboxSize)
        
        Ggrid = QtWidgets.QGridLayout()
        Ggrid.addWidget(self.lDate, 1, 1)
        Ggrid.addWidget(self.tDate, 1, 2)
        Ggrid.addWidget(self.lName, 2, 1)
        Ggrid.addWidget(self.tName, 2, 2)
        Ggrid.addWidget(self.lId, 3, 1)
        Ggrid.addWidget(self.tId, 3, 2)
        Ggrid.addWidget(self.lAmount, 4, 1)
        Ggrid.addWidget(self.tAmount, 4, 2)
    
        self.APV_details_GroupBox.setLayout(Ggrid)
    
    def init_ui(self):
        #Create Widgets
        self.lAPV_Title = QtWidgets.QLabel("LCG Veterinary Trading")
        self.lAPV_Title.setStyleSheet('QLabel { font-size: 18pt; padding: 10px; font-weight: bold;}')
        
        self.createDetails_group()
        self.createColumn_group()
        #self.createPreview_group()

        self.bSubmit = QtWidgets.QPushButton("Submit")
        self.bSubmit.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; background-color: #5cb85c; border-color: #4cae4c;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #4baa4b; border-color: #409140;}""")
        
#        self.Spacer = QtWidgets.QLabel("")
#        self.addWidget(self.Spacer, 7, 5, 1, 3)
        self.setColumnStretch(11,1)
        self.setColumnStretch(0,1)
        self.setRowStretch(11,1)
        
        self.addWidget(self.lAPV_Title, 1,1,1,1)
        self.addWidget(self.APV_details_GroupBox, 2, 1, 4, 2)
        self.addWidget(self.column_name_GroupBox, 6, 1, 2, 2)
        self.addWidget(self.bSubmit, 8, 1, 1, 2)
        #self.addWidget(self.preview_GroupBox, 2, 3, 6, 2)
        
        #DEBUG
        #self.bColumn_Add.clicked.connect(self.add_column)
        