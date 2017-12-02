import sys
import pymysql
from PyQt5 import QtWidgets,QtCore,Qt
from AddAPV import AddAPVView
from AddColumn import AddColumnView
from NewColumn import NewColumnView
from NewGroup import NewGroupView


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setFixedSize(1024,720)
        self.resize(1024,720)
        #self.resize(600,300)
        
        self.db = pymysql.connect("localhost","root","p@ssword","introse",autocommit=True)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        
        self.add_apv_tab()
        
#        #self.db.close() #close db
#        
#    #REMOVE THIS LATER
#    def get_column_choices(self):
#        group_statement = "select group_name from column_group"
#        self.cursor.execute(group_statement)
#        tempvar = self.cursor.fetchall()
#        temp = [row["group_name"] for row in tempvar]
#        print(temp)
#        return temp
    
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
        self.widgetFrame = WindowFrame(AddAPVView)
        self.setCentralWidget(self.widgetFrame)

        self.widgetFrame.layout.bSubmit.clicked.connect(self.db_add_apv)
        self.widgetFrame.layout.bColumn_Add.clicked.connect(self.add_apv_column_window)        

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
        
        if self.checkAPV_id(items["id_apv"]):
            self.apv_execute_statement(items["date"],items["name"],items["id_apv"],items["amount"])
            self.apv_credit_execute_statement(items["column_names"],items["column_val"],items["id_apv"])
        else:
            #SHOW ERROR WINDOW
            print("Duplicate APV ID!")
        #change to turn back to other window
        self.close()
            
    
    
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
        self.subwidgetFrame = WindowFrame(AddColumnView, self.col_data)
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
        self.subwidgetFrame = WindowFrame(NewColumnView, self.get_column_groups())
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.add_column_to_group)
        self.subwidgetFrame.layout.bNew.clicked.connect(self.new_group_tab)
        self.subwidgetFrame.layout.bCancel.clicked.connect(self.close)
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.add_apv_column_tab)
        self.setCentralWidget(self.subwidgetFrame)
        
    def new_group_tab(self):
        self.setWindowTitle("Add New Group")
        self.subwidgetFrame = WindowFrame(NewGroupView)
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.add_group_name)
        self.subwidgetFrame.layout.bAdd.clicked.connect(self.new_apv_column_tab)
        self.subwidgetFrame.layout.bBack.clicked.connect(self.new_apv_column_tab)
        self.setCentralWidget(self.subwidgetFrame)
    
    def add_group_name(self):
        groupName = self.subwidgetFrame.layout.tGroup.text()
        insert_statement = "INSERT INTO column_group SET group_name = '"+ groupName +"'"
        self.cursor.execute(insert_statement)
        
    def add_column_to_group(self):        
        groupName = self.subwidgetFrame.layout.radioButton_Group.checkedButton().text()
        columnName = self.subwidgetFrame.layout.tColumn.text()
        
        
        #print("group name:" + groupName + " \ncolumn name:" + columnName)
        
        insert_statement = """ INSERT INTO column_name_table
   SET column_name = '"""+ columnName +"""',
		id_group = (
       SELECT id_group
         FROM column_group
        WHERE group_name = '"""+ groupName +"""' )"""
        
        print(insert_statement)
        self.cursor.execute(insert_statement)#Execute
    
    def get_column_groups(self):
        group_statement = "select group_name from column_group"
        self.cursor.execute(group_statement)
        tempvar = self.cursor.fetchall()
        temp = [row["group_name"] for row in tempvar]
        print(temp)
        return temp
    
    def get_column_choices(self):
        group_statement = "select group_name from column_group"
        self.cursor.execute(group_statement)
        tempvar = self.cursor.fetchall()
        temp = [row["group_name"] for row in tempvar]
        print(temp)
        self.column_groups = temp

        name_statement = """select g.group_name as 'group', n.column_name as 'name'
                            from column_group as g, column_name_table as n
                            where g.id_group = n.id_group"""
        self.cursor.execute(name_statement)
        temp = self.cursor.fetchall()
        #print(temp)
        self.column_names = temp
      
        

class WindowFrame(QtWidgets.QWidget):
    
    def __init__(self, layout, extra=None):
        super().__init__()
        
        if extra is None:
            self.layout = layout(self)
        else:
            self.layout = layout(self, extra)
        
        self.setLayout(self.layout)
        
        
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    
    a_window = MainWindow()
    a_window.show()
    sys.exit(app.exec_())
    