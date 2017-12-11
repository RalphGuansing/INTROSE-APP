import sys
import pymysql
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
from Invoice.AddInvoice import AddInvoiceView
from Invoice.ViewInvoice import ViewInvoice
from Invoice.HomeInvoice import HomeInvoice
from Invoice.ViewInvoiceList import ViewInvoice as InvList
from Invoice.AddInvoiceConfirm import AddInvoiceConfirm


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setFixedSize(1024,720)
        self.resize(1366,768)

#        self.db = pymysql.connect("localhost","root","p@ssword","introse",autocommit=True)
#        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        
        self.adb = adb()
        
        #self.view_details_payable_tab()
        self.login_tab()
        #self.accounting_home_view()
        #self.view_receivable_tab()
    
    def inventory_view(self):
        self.setWindowTitle("Inventory") 
        self.widgetFrame = WindowFrame(InventoryTabs)
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
    #JAROLD
    #INVOICING

    def add_invoice_tab(self):
        self.setWindowTitle("Invoice")       
        self.widgetFrame = WindowFrame(AddInvoiceView)

        self.widgetFrame.layout.bBack.clicked.connect(self.home_invoice_tab)
        	
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        
    def view_invoice_tab(self):
        self.setWindowTitle("Invoice")
        self.widgetFrame = WindowFrame(ViewInvoice)

        self.Dialog = QtWidgets.QInputDialog.getInt(self, "Invoice number", "Please enter the invoice number", 1,)
        try:
            self.widgetFrame.layout.get_invoice(self.Dialog[0])
            self.widgetFrame.layout.bBack.clicked.connect(self.home_invoice_tab)
            self.widgetFrame.layout.bAddInvoice.clicked.connect(self.add_invoice_tab)
        except IndexError:
            self.home_invoice_tab()

        

        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        
    def home_invoice_tab(self):
        self.setWindowTitle("Invoice")
        self.widgetFrame = WindowFrame(InvoiceTabs)

        # self.widgetFrame.layout.bAddInvoice.clicked.connect(self.add_invoice_tab)
        # self.widgetFrame.layout.bViewInvoice.clicked.connect(self.view_invoice_tab)
        # self.widgetFrame.layout.bInvoiceList.clicked.connect(self.view_list_tab)

        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()

    def view_list_tab(self):
        self.setWindowTitle("Invoice")
        self.widgetFrame = WindowFrame(InvList)

        self.widgetFrame.layout.bBack.clicked.connect(self.home_invoice_tab)

        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        
    pass #END OF INVOICING
    #RALPH
    def cust_monthly_dia(self, func):
        self.dialog_monthly = DialogFrame("Input",input_month_year,self)
        self.dialog_monthly.layout.bSubmit.clicked.connect(self.dialog_monthly.close)
        self.dialog_monthly.layout.bCancel.clicked.connect(self.dialog_monthly.close)
        self.dialog_monthly.layout.bSubmit.clicked.connect(func)
        self.dialog_monthly.exec()
        
    def cust_payment_dia(self, func):
        ar_Table = self.widgetFrame.layout.ar_Table
        items ={}
        pr_id = self.adb.get_latest_pr()
        items["pr_id"] = pr_id
        try:
            cost = ar_Table.item(ar_Table.currentRow(), 2).text()
            items["cost"] = cost
            self.dialog_payment = DialogFrame("Input",input_payment,self, items)
            self.dialog_payment.layout.bSubmit.clicked.connect(self.dialog_payment.close)
            self.dialog_payment.layout.bCancel.clicked.connect(self.dialog_payment.close)
            self.dialog_payment.layout.bSubmit.clicked.connect(partial(func, self.dialog_payment.layout, self.widgetFrame.layout))
            self.dialog_payment.exec()

        except:
            if ar_Table.rowCount() != 0:
                self.showMessage('Error Input', "Please select a receivable")
            else:
                self.showMessage('Error', "No receivable to be paid")
    pass#ACCOUNTING   
    def accounting_home_view(self):
        self.setWindowTitle("Accounting")
        self.widgetFrame = WindowFrame(Accounting_HomeView)
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        self.widgetFrame.layout.bView_APayable.clicked.connect(partial(self.cust_monthly_dia, self.view_payable_tab))
        self.widgetFrame.layout.bAdd_APayable.clicked.connect(self.add_apv_tab)
        self.widgetFrame.layout.bView_AReceivable.clicked.connect(partial(self.view_customer_tab,self.adb.get_customer_names()))
        
    pass#RECEIVABLES
    def view_customer_tab(self, customer_names):
        self.setWindowTitle("Customer List")
        self.widgetFrame = WindowFrame(Customer_ListView, customer_names)
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        self.widgetFrame.layout.tCustomer_table.itemDoubleClicked.connect(self.view_receivable_tab)
        self.widgetFrame.layout.tCustomer_table.itemActivated.connect(self.view_receivable_tab)

    def view_receivable_tab(self, customer_name):
#        customer_name = self.widgetFrame.layout.customer_name
        try:
            print(customer_name.text())
            self.customer_name= customer_name.text()
        except:
            pass
        
        self.setWindowTitle("Accounts Receivable")
        self.widgetFrame = WindowFrame(AccountsReceivableView, self.customer_name)
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        
        self.widgetFrame.layout.input_details(self.adb.get_customer_details(self.customer_name))
        self.widgetFrame.layout.input_ar_table(self.adb.get_customer_ar(self.customer_name))
        self.widgetFrame.layout.input_balance(self.adb.get_customer_balance(self.customer_name))
        self.widgetFrame.layout.bMonthly.clicked.connect(partial(self.cust_monthly_dia, self.view_receivable_monthly_tab))
        self.widgetFrame.layout.bAdd_Payment.clicked.connect(partial(self.cust_payment_dia, self.adb.add_payment_ar))
        self.widgetFrame.layout.bAdd_Payment.clicked.connect(self.refresh_ui)

        
    pass#MONTHLY RECEIVABLES
    def view_receivable_monthly_tab(self):
        self.setWindowTitle("Accounts Receivable")
        
        customer_name= self.widgetFrame.layout.customer_name
        month = self.dialog_monthly.layout.month_choice.value()
        year = self.dialog_monthly.layout.year_choice.value()
        
        self.widgetFrame = WindowFrame(AccountsReceivable_MonthlyView,{"name":customer_name, "month":month, "year":year})
        self.widgetFrame.layout.bAdd_Payment.clicked.connect(partial(self.cust_payment_dia, self.adb.add_payment_ar))
        self.widgetFrame.layout.bAdd_Payment.clicked.connect(self.refresh_ui)
        self.widgetFrame.layout.bDel_Payment.clicked.connect(partial(self.showMessage, "Deleting Payment", "Are you sure?", None, 1))
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        
        self.widgetFrame.layout.input_ar_table(self.adb.get_customer_ar_monthly(customer_name, month, year))
        self.widgetFrame.layout.input_beg_balance(self.adb.get_customer_beg_monthly(customer_name, month, year))
        self.widgetFrame.layout.input_end_balance(self.adb.get_customer_end_monthly(customer_name, month, year))
        
    def refresh_ui(self):
        if type(self.widgetFrame.layout) is AccountsReceivableView:
            print(" is AccountsReceivableView")
            self.view_receivable_tab(self.widgetFrame.layout.customer_name)
        if type(self.widgetFrame.layout) is AccountsReceivable_MonthlyView:
            print(" is AccountsReceivable_MonthlyView")
            self.view_receivable_monthly_tab()
  
    pass#PAYABLES
    def view_payable_tab(self):
        month = self.dialog_monthly.layout.month_choice.value()
        year = self.dialog_monthly.layout.year_choice.value()
        self.setWindowTitle("Monthly Accounts Payable")
        self.widgetFrame = WindowFrame(AccountsPayable_MonthlyView, {"month":month, "year":year})
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        #self.widgetFrame.layout.bDetails.clicked.connect(self.view_details_payable_tab)
        self.widgetFrame.layout.bDetails.clicked.connect(self.set_view_payable)
        self.widgetFrame.layout.input_ap_table(self.adb.get_apv_monthly( month, year))
        self.widgetFrame.layout.input_monthly_total(self.adb.get_apv_monthly_total( month, year))
    
    def view_details_payable_tab(self):
        self.setWindowTitle("Accounts Payable Details")
        self.widgetFrame = WindowFrame(APVView)
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        
        
        
    def set_view_payable(self):
        ap_Table = self.widgetFrame.layout.ap_Table
        try:
            id_apv = ap_Table.item(ap_Table.currentRow(), 2).text()
            
            print(id_apv)
            self.view_details_payable_tab()
            print(self.adb.get_apv_details(id_apv))
            self.widgetFrame.layout.set_Details(self.adb.get_apv_details(id_apv))
            self.widgetFrame.layout.set_Columns(self.adb.get_apv_columns(id_apv))

        except:
            if ap_Table.rowCount() != 0:
                self.showMessage('Error Input', "Please select a payable")
            else:
                self.showMessage('Error', "No payable to be checked")
    
    pass#ADD PAYABLES
    def add_apv_tab(self):
        self.setWindowTitle("Add Account Payable Voucher")
        self.widgetFrame = WindowFrame(AddAPVView)
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        self.widgetFrame.layout.bSubmit.clicked.connect(partial(self.adb.db_add_apv, self))
        self.widgetFrame.layout.bColumn_Add.clicked.connect(self.add_apv_column_window)        
        self.widgetFrame.layout.bColumn_Delete.clicked.connect(self.delete_row)
    
    def add_apv_column_window(self):
        col_data = self.widgetFrame.layout.column_data
        self.subFrame = SubWindow(col_data,  self)
        #self.subFrame = AddColumnDialogFrame(col_data,self.db, "title",self, self.widgetFrame)
        #self.subFrame.subwidgetFrame.layout.bAdd.clicked.connect(self.transfer_add_apv)
        self.subFrame.show()
        #sys.exit(app.exec_())
    
    def transfer_add_apv(self):
        self.widgetFrame.layout.add_column(self.subFrame.subwidgetFrame.layout.column_names)
        
    def delete_row(self):
        row_num = self.widgetFrame.layout.pColumn_Table.currentRow()
        self.widgetFrame.layout.pColumn_Table.removeRow(row_num)
        
        #UPDATE COLUMN_DATA
        self.widgetFrame.layout.column_data = []
        row_count = self.widgetFrame.layout.pColumn_Table.rowCount()
        print(row_count)
        for i in range(row_count):
            self.widgetFrame.layout.column_data.append(self.widgetFrame.layout.pColumn_Table.item(i,0).text())
        

    pass #END OF ACCOUNTING
    
    def showMessage(self, title, message, info=None, func=None, messageType=0):
        
        """ This Method is responsible for Showing Dialogs if there is an error """
        cont = True;
        if func:
            ar_Table = self.widgetFrame.layout.ar_Table
            try:
                invoice_number = ar_Table.item(ar_Table.currentRow(), 1).text()
            except:
                    if ar_Table.rowCount() != 0:
                        self.showMessage('Error Input', "Please select a receivable")
                    else:
                        self.showMessage('Error', "No receivable to be paid")
                    cont= False
                    
        
        if cont:
            infoBox = QtWidgets.QMessageBox()
            if messageType == 0:
                infoBox.setIcon(QtWidgets.QMessageBox.Warning)
            else:
                infoBox.setIcon(QtWidgets.QMessageBox.Information)
            infoBox.setText(message)
            if info is not None:
                infoBox.setInformativeText(info)
            infoBox.setWindowTitle(title)
            #infoBox.setDetailedText("Detailed Text")
            if func is None:
                infoBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                infoBox.setEscapeButton(QtWidgets.QMessageBox.Close) 
            else:
                yesbutton = infoBox.addButton(QtWidgets.QMessageBox.Yes)
                nobutton = infoBox.addButton(QtWidgets.QMessageBox.No)

            infoBox.exec_()
            
            if messageType == 1:
                self.accounting_home_view()
            
            if func is not None:
                if infoBox.clickedButton() == yesbutton:
                    print("hello")
                    self.adb.del_payment_ar(invoice_number)
                    self.refresh_ui()

                else:
                    infoBox.close()

        
    def init_navbar(self):
        """ This method initializes the functionalities of the navbar """
        #TEMPORARY
        self.widgetFrame.bAccounting.clicked.connect(self.accounting_home_view)
        self.widgetFrame.bInventory.clicked.connect(self.inventory_view)
        self.widgetFrame.bInvoice.clicked.connect(self.home_invoice_tab)
        self.widgetFrame.bLogo.clicked.connect(self.home_tab)
        self.widgetFrame.bLogout.clicked.connect(self.login_tab)
    
    def login_tab(self):
        self.setWindowTitle("LCG Veterinary Trading")
        self.widgetFrame = SubWindowFrame(LoginView)
        self.setCentralWidget(self.widgetFrame)    
        self.widgetFrame.layout.bLogin.clicked.connect(self.login)
    
    def home_tab(self):
        self.setWindowTitle("Home")
        self.widgetFrame = WindowFrame(HomeView)
        self.setCentralWidget(self.widgetFrame)
        self.init_navbar()
        #self.widgetFrame.layout.bLogin.clicked.connect(self.login)
    
    def close_subFrame(self):
        
        """ Closes the Subwidget frame if it is visible"""
        
        try:
            if self.subFrame is not None:
                if self.subFrame.isVisible():
                    self.subFrame.close()
                    print("Closing Sub-Widget Frame")
                else:
                    print("Closing (with memory)")
        except:
            print("Closing")
    

    
    def login(self):
        username = self.widgetFrame.layout.tUsername.text()
        
        encoded_plaintext = self.widgetFrame.layout.tPassword.text().encode('utf-8')
        
        tempvar = self.adb.login(username, encoded_plaintext)
        #CORRECT OR VALID
        if tempvar:
            print("Employee ID: " + str(tempvar["employee_id"]))
            print("Username: " + str(tempvar["username"]))
            print("Full Name: " + str(tempvar["full_name"]))
            
            self.username = tempvar["username"]
            self.home_tab()
            
        #WRONG OR DOES NOT EXIST
        else:
            self.showMessage("Invalid Entry", "Invalid username or password")

            
            
class SubWindow(QtWidgets.QMainWindow):
    
    def __init__(self, col_data, mainwindow, parent=None):
        super(SubWindow, self).__init__(parent)
        #self.setFixedSize(,1024,720)
        self.resize(600,300)
        self.setWindowFlags(QtCore.Qt.SubWindow)
        self.adb = adb()
        self.mainwindow = mainwindow
        #self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        self.col_data = col_data
        self.add_apv_column_tab()
        
    def add_apv_column_tab(self):
        self.setWindowTitle("Add Column")
        self.subwidgetFrame = SubWindowFrame(AddColumnView, self.col_data)
        columns = self.adb.get_column_choices()
        print(columns)
        self.subwidgetFrame.layout.input_Tree_Choices(columns["groups"], columns["names"])
        self.subwidgetFrame.layout.refresh_Tree()
        
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.subwidgetFrame.layout.addColumn_names)
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.mainwindow.transfer_add_apv)
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.close)
        self.subwidgetFrame.layout.bNew.clicked.connect(self.new_apv_column_tab)
        self.subwidgetFrame.layout.bCancel.clicked.connect(self.close)

        self.setCentralWidget(self.subwidgetFrame)
    
    def new_apv_column_tab(self):
        self.setWindowTitle("Add New Column")
        self.subwidgetFrame = SubWindowFrame(NewColumnView, self.adb.get_column_groups())
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.add_column_to_group)
        self.subwidgetFrame.layout.bNew.clicked.connect(self.new_group_tab)
        self.subwidgetFrame.layout.bCancel.clicked.connect(self.close)
        #self.subwidgetFrame.layout.bAdd.clicked.connect(self.add_apv_column_tab)
        self.setCentralWidget(self.subwidgetFrame)
        
    def new_group_tab(self):
        self.setWindowTitle("Add New Group")
        self.subwidgetFrame = SubWindowFrame(NewGroupView)
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.add_group_name)
        #self.subwidgetFrame.layout.bAdd.clicked.connect(self.new_apv_column_tab)
        self.subwidgetFrame.layout.bBack.clicked.connect(self.new_apv_column_tab)
        self.setCentralWidget(self.subwidgetFrame)
    
    def add_group_name(self):
        #print("here")
        groupName = self.subwidgetFrame.layout.tGroup.text()
        isNotDupe = self.adb.checkDupe(groupName, 1)
        if groupName and isNotDupe:
            self.adb.add_group_name(groupName)
            
            #GO BACK TO PREVIOUS TAB
            self.new_apv_column_tab()
            
        else:
            error = []
            errorMessage = "Error"
            
            if not groupName:
                error.append("No Group name inputted")
            if not isNotDupe:
                error.append("Group name already exists")
            if len(error) == 1:
                errorMessage += ":"
            else: 
                errorMessage += "s:"
            for i in range(len(error)):
                errorMessage += """
                """ + error[i]

            self.mainwindow.showMessage("Error Input",  errorMessage)
        
    def add_column_to_group(self):        
        groupName = self.subwidgetFrame.layout.radioButton_Group.checkedButton()
        columnName = self.subwidgetFrame.layout.tColumn.text()
        isNotDupe = self.adb.checkDupe(columnName, 0)
        
        if groupName is not None and columnName and isNotDupe:

            self.adb.add_column_to_group(groupName.text(), columnName)
            #GO BACK TO PREVIOUS TAB
            self.add_apv_column_tab()
            
        else:#RAISE ERROR
            error = []
            errorMessage = "Error"
            
            if not columnName:
                error.append("No Column name inputted")
            if not isNotDupe:
                error.append("Column name already exists")
            if groupName is None:
                error.append("No Group Selected")
            if len(error) == 1:
                errorMessage += ":"
            else: 
                errorMessage += "s:"
            for i in range(len(error)):
                errorMessage += """
                """ + error[i]

            self.mainwindow.showMessage("Error Input",  errorMessage)
            
#IMPLEMENTING DIALOG WINDOW



class DialogFrame(QtWidgets.QDialog):
    def __init__(self, title,layout, parent=None, extra=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        
        if extra is None:
            self.layout = layout(self)
        else:
            self.layout = layout(self, extra)
            
        self.setLayout(self.layout)
        
        self.resize(300,214)
        
class SubWindowFrame(QtWidgets.QWidget):
    
    def __init__(self, layout, extra=None):
        super().__init__()
        
        if extra is None:
            self.layout = layout(self)
        else:
            self.layout = layout(self, extra)
        
        self.setLayout(self.layout)
        

class WindowFrame(QtWidgets.QWidget):
    
    def __init__(self, layout, extra=None):
        super().__init__()
        
        self.container_layout = QtWidgets.QGridLayout()
        self.container_layout.setContentsMargins(0,0,0,0)
        
        #ADDING NAVBAR
        self.make_navbar()
        self.container_layout.addWidget(self.navbar,1,1,1,4)
        
        if extra is None:
            self.layout = layout(self)
        else:
            self.layout = layout(self, extra)
        
        self.layout_groupbox = QtWidgets.QGroupBox("")
        self.layout_groupbox.setLayout(self.layout)
        self.container_layout.addWidget(self.layout_groupbox,2,1,1,4)

        self.setLayout(self.container_layout)
        
    def make_navbar(self):
        self.navbar = QtWidgets.QGroupBox("")
        #self.navbar.setFlat(True)
        self.navbar.setStyleSheet("QGroupBox{border:0; background-color:#ca4f4f;}")
        
        navGrid = QtWidgets.QGridLayout()
        
        labelStyle = """QLabel { font-size: 12pt; color: white; padding: 4px; font-family:Montserrat;}
                        QLabel:hover{color:gainsboro;}
                     """
        labelStyle2 = """QLabel { font-size: 24pt; color: white; padding: 1px; font-family:Montserrat;}
                         QLabel:hover{color:gainsboro;}
                      """
        buttonStyle = """QPushButton {
                         background:none!important;
                         color:inherit;
                         border:none; 
                         padding:0!important;
                         font: inherit;
                         font-size: 12pt; color: white; padding: 4px; font-family:Montserrat;
                         }
                         QPushButton:hover{color:gainsboro;}
                        """
        buttonStyle2 = """QPushButton {
                         background:none!important;
                         color:inherit;
                         border:none; 
                         padding:0!important;
                         font: inherit;
                         font-size: 24pt; color: white; padding: 1px; font-family:Montserrat;
                         }
                         QPushButton:hover{color:gainsboro;}
                        """
        
        self.bLogo = QtWidgets.QPushButton("LCG")
        self.bLogo.setStyleSheet(buttonStyle2)
        
        self.bInvoice = QtWidgets.QPushButton("Invoice")
        self.bInvoice.setStyleSheet(buttonStyle)
        
        self.bInventory = QtWidgets.QPushButton("Inventory")
        self.bInventory.setStyleSheet(buttonStyle)
        
        self.bAccounting = QtWidgets.QPushButton("Accounting")
        self.bAccounting.setStyleSheet(buttonStyle)
        
        self.bAdmin = QtWidgets.QPushButton("Admin")
        self.bAdmin.setStyleSheet(buttonStyle)
        
        self.bLogout = QtWidgets.QPushButton("Log Out")
        self.bLogout.setStyleSheet(buttonStyle)
        
        navGrid.setColumnStretch(5,1)
        navGrid.addWidget(self.bLogo, 1,1)
        navGrid.addWidget(self.bInvoice, 1,2)
        navGrid.addWidget(self.bInventory,1,3)
        navGrid.addWidget(self.bAccounting,1,4)
        navGrid.addWidget(self.bAdmin,1,6)
        navGrid.addWidget(self.bLogout,1,7)
        
        self.navbar.setLayout(navGrid)

class InvoiceTabs(QtWidgets.QGridLayout):

    def __init__(self, parent=None):   
        super(QtWidgets.QGridLayout, self).__init__(parent)
        #self.layout = QtWidgets.QGridLayout(self)
        self.tabs = QtWidgets.QTabWidget()
        self.add_invoice_tab = SubWindowFrame(AddInvoiceView)
        self.view_invoice_tab = SubWindowFrame(ViewInvoice)
        self.view_list_tab = SubWindowFrame(InvList)
        self.tabs.addTab(self.add_invoice_tab,"Add Invoice")
        self.tabs.addTab(self.view_invoice_tab,"View Invoice")
        self.tabs.addTab(self.view_list_tab,"View Invoice List")
        #self.layout.addWidget(self.tabs)
        self.addWidget(self.tabs)


class InventoryTabs(QtWidgets.QGridLayout):

    def __init__(self, parent=None):   
        super(QtWidgets.QGridLayout, self).__init__(parent)
        #self.layout = QtWidgets.QGridLayout(self)
        self.tabs = QtWidgets.QTabWidget()
        self.add_inventory_tab = SubWindowFrame(AddInventoryView)
        self.view_inventory_tab = SubWindowFrame(ViewInventoryList)
        self.tabs.addTab(self.add_inventory_tab,"Add Inventory")
        self.tabs.addTab(self.view_inventory_tab,"View Inventory")
        #self.layout.addWidget(self.tabs)
        self.addWidget(self.tabs)

        
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    Qt.QFontDatabase.addApplicationFont("Resources/Montserrat-Regular.ttf")
    
    a_window = MainWindow()
    a_window.show()
    sys.exit(app.exec_())
    