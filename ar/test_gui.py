import sys
import pymysql
from PyQt5 import QtWidgets,QtCore,Qt
from AddAPV import AddAPVView as testlayout
#from AddColumn import AddColumnView
#from NewColumn import NewColumnView
#from NewGroup import NewGroupView
from AccountsReceivable import AccountsReceivableView as AddAPVView
from AccountsReceivable_Monthly import AccountsReceivable_MonthlyView, input_month_year


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setFixedSize(1024,720)
        self.resize(1024,720)
        #self.resize(600,300)
        
        self.db = pymysql.connect("localhost","root","p@ssword","introse",autocommit=True)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        
        self.add_apv_tab()
        
    def showMessage(self, title, message, info=None):
        infoBox = QtWidgets.QMessageBox()
        infoBox.setIcon(QtWidgets.QMessageBox.Warning)
        infoBox.setText(message)
        if info is not None:
            infoBox.setInformativeText(info)
        infoBox.setWindowTitle(title)
        #infoBox.setDetailedText("Detailed Text")
        infoBox.setStandardButtons(QtWidgets.QMessageBox.Ok )
        infoBox.setEscapeButton(QtWidgets.QMessageBox.Close) 
        infoBox.exec_()
    
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
    
    def closeEvent(self, event):
        
        """ Adding more functions when the mainwindow closes """
        
        self.db.close()
        self.close_subFrame()
        self.close()
    
    def add_apv_tab(self):
        self.setWindowTitle("Add Account Payable Voucher")
        #ACCOUNTS RECEIVABLE
        self.widgetFrame = WindowFrame(AddAPVView,"Kingsroad vet")
        #ACCOUNTS RECEIVABLE MONTHLY
        #self.widgetFrame = WindowFrame(AddAPVView, {"name":"Kingsroad vet", "month":10, "year":2017})
        
        
        self.widgetFrame.layout.bMonthly.clicked.connect(self.ar_cust_monthly_dia)
        self.setCentralWidget(self.widgetFrame)
    
#    ACCOUNTS RECEIVABLE
        self.get_customer_details()
        self.get_customer_ar()
        self.get_customer_balance()
#    ACCOUNTS RECEIVABLE MONTHLY
#        self.get_customer_ar_monthly()
#        self.get_customer_beg_monthly()
#        self.get_customer_end_monthly()
    def ar_monthly_tab(self):
        customer_name = self.widgetFrame.layout.customer_name
        month = self.dialog_monthly.layout.month_choice.value()
        year = self.dialog_monthly.layout.year_choice.value()
        self.setWindowTitle("Monthly Accounts Receivable")
        self.widgetFrame = WindowFrame(AccountsReceivable_MonthlyView, {"name":customer_name, "month":month, "year":year})
        self.setCentralWidget(self.widgetFrame)
        
        self.get_customer_ar_monthly()
        self.get_customer_beg_monthly()
        self.get_customer_end_monthly()
    
    def ar_cust_monthly_dia(self):
        self.dialog_monthly = DialogFrame("Input",input_month_year,self.widgetFrame)
        self.dialog_monthly.layout.bSubmit.clicked.connect(self.dialog_monthly.close)
        self.dialog_monthly.layout.bCancel.clicked.connect(self.dialog_monthly.close)
        self.dialog_monthly.layout.bSubmit.clicked.connect(self.ar_monthly_tab)
        self.dialog_monthly.exec()
        
    
    def get_customer_ar_monthly(self):
        customer_name = self.widgetFrame.layout.customer_name
        month = self.widgetFrame.layout.selectedMonth
        year = self.widgetFrame.layout.selectedYear
        
        select_statement = """select DATE_FORMAT(date,'%M %e, %Y') AS Date, inv_id,amount,date_paid,pr_id,payment
        from accounts_receivable 
        where customer_id = (select customer_id from customer where customer_name = '"""+customer_name+"""') and MONTH(Date) = """+str(month)+""" and YEAR(Date) = """+str(year)+""" """
        
        self.cursor.execute(select_statement)
        temp = self.cursor.fetchall()
        #print(temp)
        #print(select_statement)
        self.widgetFrame.layout.input_ar_table(temp)
        
    def get_customer_beg_monthly(self):
        customer_name = self.widgetFrame.layout.customer_name
        month = self.widgetFrame.layout.beforeMonth
        year = self.widgetFrame.layout.beforeYear
        
        select_statement = """select IFNULL(sum(amount), 0) - IFNULL(sum(payment), 0) as balance
        from accounts_receivable 
        where customer_id = (select customer_id from customer where customer_name = '"""+customer_name+"""') and MONTH(Date) = """+str(month)+""" and YEAR(Date) = """+str(year)+""" """
        
        self.cursor.execute(select_statement)
        temp = self.cursor.fetchone()
        #print(temp)
        self.widgetFrame.layout.input_beg_balance(temp)
        #print(select_statement)
        #self.widgetFrame.layout.input_ar_table(temp)
    
    
    def get_customer_end_monthly(self):
        customer_name = self.widgetFrame.layout.customer_name
        month = self.widgetFrame.layout.selectedMonth
        year = self.widgetFrame.layout.selectedYear
        
        select_statement = """select IFNULL(sum(amount), 0) - IFNULL(sum(payment), 0) as balance
        from accounts_receivable 
        where customer_id = (select customer_id from customer where customer_name = '"""+customer_name+"""') and MONTH(Date) = """+str(month)+""" and YEAR(Date) = """+str(year)+""" """
        
        self.cursor.execute(select_statement)
        temp = self.cursor.fetchone()
        #print(temp)
        self.widgetFrame.layout.input_end_balance(temp)
        #print(select_statement)
        
        
    
    #FOR ACCOUNTS RECEIVABLE
    def get_customer_details(self):
        customer_name = self.widgetFrame.layout.customer_name
        select_statement = """select customer_name, address from customer where customer_name = '"""+customer_name+"""'"""
        self.cursor.execute(select_statement)
        temp = self.cursor.fetchone()
        #print(temp)
        self.widgetFrame.layout.input_details(temp)
    
    def get_customer_ar(self):
        customer_name = self.widgetFrame.layout.customer_name
        select_statement = """select DATE_FORMAT(date,'%M %e, %Y') AS Date, inv_id,amount 
        from accounts_receivable 
        where customer_id = (select customer_id from customer where customer_name = '"""+ customer_name +"""') and payment is null"""
        self.cursor.execute(select_statement)
        temp = self.cursor.fetchall()
        #print(temp)
        self.widgetFrame.layout.input_ar_table(temp)
    
    def get_customer_balance(self):
        customer_name = self.widgetFrame.layout.customer_name
        
        select_statement = """select sum(amount) as balance 
        from accounts_receivable 
        where customer_id = (select customer_id from customer where customer_name = '"""+ customer_name +"""') and payment is null"""
        
        self.cursor.execute(select_statement)
        temp = self.cursor.fetchone()
        self.widgetFrame.layout.input_balance(temp)
        
        
        

#        self.widgetFrame.layout.bSubmit.clicked.connect(self.db_add_apv)
#        self.widgetFrame.layout.bColumn_Add.clicked.connect(self.add_apv_column_window)        
#        self.widgetFrame.layout.bColumn_Delete.clicked.connect(self.delete_row)        

        #REMOVE THESE LATER
        #self.widgetFrame.layout.get_Current_Groups(self.get_column_choices())
    
    def add_apv_column_window(self):
        col_data = self.widgetFrame.layout.column_data
        self.subFrame = SubWindow(col_data, self.db, self)
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
    
    def checkAPV_id(self, id_apv):
        
        """ returns true if it is able to retrieve something from the database """
        
        select_statement = "Select * from `vouchers payable` where id_apv = " + str(id_apv)
        self.cursor.execute(select_statement)
        temp = self.cursor.fetchone()
        #print(temp)
        return temp is None
        
    def db_add_apv(self):
        
        """ Checks if the new APV # is already in the database """
        
        items = self.widgetFrame.layout.get_items()
        if items["id_apv_BOOL"] and items["amount_BOOL"]:
            if self.checkAPV_id(items["id_apv"]):
                self.apv_execute_statement(items["date"],items["name"],items["id_apv"],items["amount"])
                self.apv_credit_execute_statement(items["column_names"],items["column_val"],items["id_apv"])
                #REMOVE LATER
                
                #self.close()
            else:
                #SHOW ERROR WINDOW
                print("Duplicate APV ID!")
        else:
            self.showMessage("Error Input", "PLEASE INPUT A NUMBER")
        #change to turn back to other window
    
    def apv_execute_statement(self, date, name, id_apv, amount):
        
        """Executes the insert statement based on the data inputted by the user"""
        
        insert_statement = 'INSERT INTO `vouchers payable` (date, name, id_apv, amount) VALUES ( \''+ date +'\',\''+ name +'\',\''+ str(id_apv) + '\',\''+str(amount) + '\');'
        print(insert_statement)
        self.cursor.execute(insert_statement)#Execute
        
    def apv_credit_execute_statement(self, column_names, column_val, id_apv):

        credit_statement = """INSERT INTO credit_type (type_name, id_apv, type_value)
                              Values
                           """
        tempString1 = ",(SELECT id_apv FROM `vouchers payable`WHERE id_apv = "

        for i in range(len(column_names)):
            credit_statement += "('" + column_names[i] + "'"+ tempString1 + str(id_apv) +"), "+ str(column_val[i]) + ")"

            if i != len(column_names)-1:
                credit_statement += ",\n"
            else:
                credit_statement += ";"

        print(credit_statement)
        self.cursor.execute(credit_statement)#Execute


class SubWindow(QtWidgets.QMainWindow):
    
    def __init__(self, col_data, db, mainwindow, parent=None):
        super(SubWindow, self).__init__(parent)
        #self.setFixedSize(,1024,720)
        self.resize(600,300)
        self.setWindowFlags(QtCore.Qt.SubWindow)
        self.db = db
        self.mainwindow = mainwindow
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        self.col_data = col_data
        self.add_apv_column_tab()
        
    def add_apv_column_tab(self):
        self.setWindowTitle("Add Column")
        self.subwidgetFrame = SubWindowFrame(AddColumnView, self.col_data)
        self.get_column_choices()
        self.subwidgetFrame.layout.input_Tree_Choices(self.column_groups, self.column_names)
        self.subwidgetFrame.layout.refresh_Tree()
        
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.subwidgetFrame.layout.addColumn_names)
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.mainwindow.transfer_add_apv)
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.close)
        self.subwidgetFrame.layout.bNew.clicked.connect(self.new_apv_column_tab)
        self.subwidgetFrame.layout.bCancel.clicked.connect(self.close)

        self.setCentralWidget(self.subwidgetFrame)
    
    def new_apv_column_tab(self):
        self.setWindowTitle("Add New Column")
        self.subwidgetFrame = SubWindowFrame(NewColumnView, self.get_column_groups())
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
        isNotDupe = self.checkDupe(groupName, 1)
        if groupName and isNotDupe:
            insert_statement = "INSERT INTO column_group SET group_name = '"+ groupName +"'"
            self.cursor.execute(insert_statement)
            
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
        isNotDupe = self.checkDupe(columnName, 0)
        
        if groupName is not None and columnName and isNotDupe:
            #print("groupName", groupName.isChecked())
        #print("group name:" + groupName + " \ncolumn name:" + columnName)
            
            insert_statement = """ INSERT INTO column_name_table
       SET column_name = '"""+ columnName +"""',
            id_group = (
           SELECT id_group
             FROM column_group
            WHERE group_name = '"""+ groupName.text() +"""' )"""

            print(insert_statement)
            self.cursor.execute(insert_statement)#Execute
            
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
            #print("Please select a Radiobutton")
            
    
    def get_column_groups(self):
        group_statement = "select group_name from column_group"
        self.cursor.execute(group_statement)
        tempvar = self.cursor.fetchall()
        temp = [row["group_name"] for row in tempvar]
        #print(temp)
        return temp
    
    def get_column_choices(self):
        group_statement = "select group_name from column_group"
        self.cursor.execute(group_statement)
        tempvar = self.cursor.fetchall()
        temp = [row["group_name"] for row in tempvar]
        #print(temp)
        self.column_groups = temp

        name_statement = """select g.group_name as 'group', n.column_name as 'name'
                            from column_group as g, column_name_table as n
                            where g.id_group = n.id_group"""
        self.cursor.execute(name_statement)
        temp = self.cursor.fetchall()
        #print(temp)
        self.column_names = temp
    
    def checkDupe(self, name, num):
        """ This Function Checks if the a name of a Column/Group has a duplicate 
            
            Returns: False if it has a Duplicate, True if unique
        """
        # num = 0 if Column Name
        # num = 1 if Group Name
        
        if num == 0:
            select_statement = """select id_column
                                from column_name_table
                                where column_name = '"""+name+"""'"""    
            
        if num == 1:
            select_statement = """select id_group
                                from column_group
                                where group_name = '"""+name+"""'"""
        if select_statement:
            self.cursor.execute(select_statement)
            temp = self.cursor.fetchone()
            return temp is None

#IMPLEMENTING DIALOG WINDOW
class DialogFrame(QtWidgets.QDialog):
    def __init__(self, title,layout, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.layout = layout(self)
        self.setLayout(self.layout)
        
        self.resize(300,200)
        
        
        
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
        
        self.container_layout = QtWidgets.QVBoxLayout()
        self.setContentsMargins(0,0,0,0)
        
        #ADDING NAVBAR
        self.make_navbar()
        self.container_layout.addWidget(self.navbar)
        
        
        if extra is None:
            self.layout = layout(self)
        else:
            self.layout = layout(self, extra)
        
        self.layout_groupbox = QtWidgets.QGroupBox("")
        self.layout_groupbox.setLayout(self.layout)
        self.container_layout.addWidget(self.layout_groupbox)

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
        
        self.bLogo = QtWidgets.QLabel("LCG")
        self.bLogo.setStyleSheet(labelStyle2)
        
        self.bInvoice = QtWidgets.QLabel("Invoice")
        self.bInvoice.setStyleSheet(labelStyle)
        
        self.bInventory = QtWidgets.QLabel("Inventory")
        self.bInventory.setStyleSheet(labelStyle)
        
        self.bAccounting = QtWidgets.QLabel("Accounting")
        self.bAccounting.setStyleSheet(labelStyle)
        
        navGrid.setColumnStretch(5,1)
        navGrid.addWidget(self.bLogo, 1,1)
        navGrid.addWidget(self.bInvoice, 1,2)
        navGrid.addWidget(self.bInventory,1,3)
        navGrid.addWidget(self.bAccounting,1,4)
        
        self.navbar.setLayout(navGrid)
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    Qt.QFontDatabase.addApplicationFont("Resources/Montserrat-Regular.ttf")
    
    a_window = MainWindow()
    a_window.show()
    sys.exit(app.exec_())
    