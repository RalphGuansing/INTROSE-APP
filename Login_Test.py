import sys
import pymysql
import hashlib
from PyQt5 import QtWidgets,QtCore,Qt
from LoginView import LoginView




class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setFixedSize(1024,720)
        self.resize(1024,720)
        #self.resize(600,300)
        
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
        self.widgetFrame = WindowFrame(LoginView)
        self.setCentralWidget(self.widgetFrame)    
        self.widgetFrame.layout.bLogin.clicked.connect(self.hash_password)  
    
    #to be edited later
    def hash_password(self):
        plaintext = self.widgetFrame.layout.tPassword.text().encode('utf-8')
        print(plaintext)
        sha = hashlib.sha1(plaintext)
        print(sha.hexdigest())
#    def close_subFrame(self):
#        
#        """ Closes the Subwidget frame if it is visible"""
#        
#        try:
#            if self.subFrame is not None:
#                if self.subFrame.isVisible():
#                    self.subFrame.close()
#                    print("Closing Sub-Widget Frame")
#                else:
#                    print("Closing (with memory)")
#        except:
#            print("Closing")
#    
#    def closeEvent(self, event):
#        
#        """ Adding more functions when the mainwindow closes """
#        
#        self.db.close()
#        self.close_subFrame()
#        self.close()
   
            
        

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
    