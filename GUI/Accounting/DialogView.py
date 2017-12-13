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
        
        #self.setRowStretch(4,1)
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
      
    
class input_payment(QtWidgets.QGridLayout):
    def __init__(self, frame, items):
        super().__init__()
        self.cost = items["cost"]
        self.pr_id = items["pr_id"]
        self.frame = frame
        self.init_ui()
    
    def get_inputs(self):
        items = {}
        
        items["date"] = self.tDate.text()
        items["pr_id"] = self.tPR.text()
        items["payment"] = self.tPayment.text()
        
        return items
        
    def init_ui(self):
        
        self.labelStyle = """QLabel { font-size: 14pt; color: black; padding: 4px;}"""
        self.addressStyle = """QLabel { font-size: 12pt; color: #666666; padding: 4px; font-family:Montserrat;}"""
        
        textboxStyle = 'QLineEdit { font-size: 12pt; padding: 2px;}'
        textboxStyle2 = 'QDateEdit { font-size: 12pt; padding: 2px;}'
        
        
        self.lDate = QtWidgets.QLabel("Date:")
        self.lDate.setStyleSheet(self.labelStyle)
        self.tDate = QtWidgets.QDateEdit(self.frame)
        self.tDate.setCalendarPopup(True)
        self.tDate.setDisplayFormat("yyyy-MM-dd")
        self.tDate.setDate(datetime.datetime.now())
        self.tDate.setMaximumDate(datetime.datetime.now())
        self.tDate.setStyleSheet(textboxStyle2)
        
        self.lPR = QtWidgets.QLabel("PR #:")
        #self.lId.setAlignment(QtCore.Qt.AlignRight)
        self.lPR.setStyleSheet(self.labelStyle)
        self.tPR = QtWidgets.QLineEdit(self.frame)
        self.tPR.setStyleSheet(textboxStyle)
        self.tPR.setText(str(self.pr_id["pr_id"]+1))
        #self.tId.textChanged.connect(self.preview_items)
        #self.tId.setFixedWidth(textboxSize)
        
        
        self.lPayment = QtWidgets.QLabel("Payment:")
        #self.lId.setAlignment(QtCore.Qt.AlignRight)
        self.lPayment.setStyleSheet(self.labelStyle)
        self.tPayment = QtWidgets.QLineEdit(self.frame)
        self.tPayment.setStyleSheet(textboxStyle)
        self.tPayment.setText(self.cost)
        
        
        self.top_box = QtWidgets.QGroupBox("")
        Ggrid = QtWidgets.QGridLayout()
        Ggrid.addWidget(self.lDate,1,1)
        Ggrid.addWidget(self.tDate,1,2)
        Ggrid.addWidget(self.lPR,2,1)
        Ggrid.addWidget(self.tPR,2,2)
        Ggrid.addWidget(self.lPayment,3,1)
        Ggrid.addWidget(self.tPayment,3,2)
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
        