import sys
import pymysql
import hashlib
from PyQt5 import QtWidgets,QtCore,Qt
from LoginView import LoginView
from HomeView import HomeView


class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setFixedSize(1024,720)
        self.resize(1024,720)

        self.db = pymysql.connect("localhost","root","p@ssword","introse",autocommit=True)
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
        
        self.login_tab()
        
    def showMessage(self, title, message, info=None):
        
        """ This Method is responsible for Showing Dialogs if there is an error """
        
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
    
    def login_tab(self):
        self.setWindowTitle("LCG Veterinary Trading")
        self.widgetFrame = SubWindowFrame(LoginView)
        self.setCentralWidget(self.widgetFrame)    
        self.widgetFrame.layout.bLogin.clicked.connect(self.login)
    
    def home_tab(self):
        self.setWindowTitle("Home")
        self.widgetFrame = WindowFrame(HomeView)
        self.setCentralWidget(self.widgetFrame)    
        #self.widgetFrame.layout.bLogin.clicked.connect(self.login)
        
    def login(self):
        username = self.widgetFrame.layout.tUsername.text()
        
        encoded_plaintext = self.widgetFrame.layout.tPassword.text().encode('utf-8')
        sha = hashlib.sha1(encoded_plaintext)
        password = sha.hexdigest()
        
        select_statement = """select employee_id, username, concat(first_name, ' ' , last_name) as full_name
            from employee
            where username = '"""+ username +"""' and password = '"""+ password +"""'"""
        
        print(select_statement)
        self.cursor.execute(select_statement)
        
        tempvar = self.cursor.fetchone()
        
        #CORRECT
        if tempvar is not None:
            print("Employee ID: " + str(tempvar["employee_id"]))
            print("Username: " + str(tempvar["username"]))
            print("Full Name: " + str(tempvar["full_name"]))
            
            self.username = tempvar["username"]
            self.home_tab()
            
        #WRONG OR DOES NOT EXIST
        else:
            self.showMessage("Invalid Entry", "Invalid username or password")

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
        
        self.bLogout = QtWidgets.QLabel("Log Out")
        self.bLogout.setStyleSheet(labelStyle)
        
        navGrid.setColumnStretch(5,1)
        navGrid.addWidget(self.bLogo, 1,1)
        navGrid.addWidget(self.bInvoice, 1,2)
        navGrid.addWidget(self.bInventory,1,3)
        navGrid.addWidget(self.bAccounting,1,4)
        navGrid.addWidget(self.bLogout,1,6)
        
        self.navbar.setLayout(navGrid)

        
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    Qt.QFontDatabase.addApplicationFont("Resources/Montserrat-Regular.ttf")
    
    a_window = MainWindow()
    a_window.show()
    sys.exit(app.exec_())
    