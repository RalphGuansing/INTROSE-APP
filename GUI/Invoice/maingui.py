import sys
from PyQt5 import QtWidgets,QtCore
from AddInvoice import AddInvoiceView
from ViewInvoice import ViewInvoice
from HomeInvoice import HomeInvoice
from ViewInvoiceList import ViewInvoice as InvList
from AddInvoiceConfirm import AddInvoiceConfirm

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setFixedSize(1024,720)
        self.resize(1500,720)
        self.home_invoice_tab()
    
    def add_invoice_tab(self):
        self.setWindowTitle("Invoice")       
        self.widgetFrame = WindowFrame(AddInvoiceView)

        self.widgetFrame.layout.bBack.clicked.connect(self.home_invoice_tab)
        #self.widgetFrame.layout.bSubmit.clicked.connect(self.add_invoice_confirm_tab)
        # self.widgetFrame.layout.layout.clicked.connect(self.home_invoice_tab)
        	
        self.setCentralWidget(self.widgetFrame)

    # def add_invoice_confirm_tab(self):
    #     self.setWindowTitle("Invoice")       
    #     self.widgetFrame = WindowFrame(AddInvoiceConfirm)

    #     self.widgetFrame.layout.bBack.clicked.connect(self.add_invoice_tab)
    #     self.widgetFrame.layout.bAddInvoice.clicked.connect(self.home_invoice_tab)

    #     self.setCentralWidget(self.widgetFrame)
        
        
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
        
    def home_invoice_tab(self):
        self.setWindowTitle("Invoice")
        self.widgetFrame = WindowFrame(Tabs)

        # self.widgetFrame.layout.bAddInvoice.clicked.connect(self.add_invoice_tab)
        # self.widgetFrame.layout.bViewInvoice.clicked.connect(self.view_invoice_tab)
        # self.widgetFrame.layout.bInvoiceList.clicked.connect(self.view_list_tab)

        self.setCentralWidget(self.widgetFrame)

    def view_list_tab(self):
        self.setWindowTitle("Invoice")
        self.widgetFrame = WindowFrame(InvList)

        self.widgetFrame.layout.bBack.clicked.connect(self.home_invoice_tab)

        self.setCentralWidget(self.widgetFrame)    


class WindowFrame(QtWidgets.QWidget):
    
    def __init__(self, layout):
        super().__init__()
        self.setWindowTitle("Window")
        #self.view_invoice = ViewInvoice(self)
        self.layout = layout(self)
        self.setLayout(self.layout)


class Tabs(QtWidgets.QGridLayout):

    def __init__(self, parent=None):   
        super(QtWidgets.QGridLayout, self).__init__(parent)
        #self.layout = QtWidgets.QGridLayout(self)
        self.tabs = QtWidgets.QTabWidget()
        self.add_invoice_tab = WindowFrame(AddInvoiceView)
        self.view_invoice_tab = WindowFrame(ViewInvoice)
        self.view_list_tab = WindowFrame(InvList)
        self.tabs.addTab(self.add_invoice_tab,"Add Invoice")
        self.tabs.addTab(self.view_invoice_tab,"View Invoice")
        self.tabs.addTab(self.view_list_tab,"View Invoice List")
        #self.layout.addWidget(self.tabs)
        self.addWidget(self.tabs)
        
        
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    a_window = MainWindow()
    a_window.show()
    sys.exit(app.exec_())