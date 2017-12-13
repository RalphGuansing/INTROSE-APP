import sys
import hashlib
from functools import partial
from PyQt5 import QtWidgets,QtCore,Qt
from LoginView import LoginView
from HomeView import HomeView
from Accounting.AccountingView import AccountingDB as adb
from Accounting.Accounting_Home import Accounting_HomeView
from Accounting.DialogView import *
from Accounting.Payable.ViewAPV import APVView,AccountsPayable_MonthlyView
from Accounting.Payable.AddAPV import AddAPVView
from Accounting.Payable.AddColumn import AddColumnView
from Accounting.Payable.NewColumn import NewColumnView
from Accounting.Payable.NewGroup import NewGroupView
from Accounting.Receivable.Customer_List import Customer_ListView
from Accounting.Receivable.AccountsReceivable import AccountsReceivableView
from Accounting.Receivable.AccountsReceivable_Monthly import AccountsReceivable_MonthlyView
from Inventory.AddInventory import *
from Inventory.AddInventoryConfirm import *
from Inventory.guiHomePage import *
from Inventory.HomePage import *
from Inventory.InventoryView import *
from Inventory.ViewInventoryList import *
from Inventory.AddNewProduct import *
from Invoice.AddInvoice import AddInvoiceView
from Invoice.ViewInvoice import ViewInvoice
from Invoice.HomeInvoice import HomeInvoice
from Invoice.ViewInvoiceList import ViewInvoice as InvList
from Invoice.AddInvoiceConfirm import AddInvoiceConfirm

class AdminView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Admin")
        self.init_ui()

    def get_plot_points(self):
    	


    def init_ui(self):

        #Create Widgets
        self.lDetails = QtWidgets.QLabel("Admin")
        self.lDetails.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')

        self.points = self.get_plot_points()

        self.lPoints = QtWidgets.QLabel()
        self.lPoints.setStyleSheet('QLabel {font: bold 50px; font-size: 12pt; padding: 10px;}')


        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(13,1)

        #Add Widgets
        
        self.addWidget(self.lDetails, 0, 2, 1, 1)

