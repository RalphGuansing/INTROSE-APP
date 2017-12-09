import sys
from PyQt5 import QtWidgets,QtCore

from HomePage import HomePage
from ViewInventoryList import ViewInventoryList
from AddInventory import AddInventoryView

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setFixedSize(1024,720)
        self.resize(1024,720)
        self.homepage_tab()
        
    def homepage_tab(self):
        self.setWindowTitle("Home Page")
        self.widgetFrame = Tabs(self)

        # self.widgetFrame.layout.bAddInventory.clicked.connect(self.add_inventory_tab)
        # self.widgetFrame.layout.bViewInventory.clicked.connect(self.view_inventory_list_tab)

        self.setCentralWidget(self.widgetFrame)
    
    def view_inventory_list_tab(self):
        self.setWindowTitle("View Inventory List")
        self.widgetFrame = WindowFrame(ViewInventoryList)

        self.widgetFrame.layout.bBack.clicked.connect(self.homepage_tab)

        self.setCentralWidget(self.widgetFrame)

    def add_inventory_tab(self):
        self.setWindowTitle("Add Inventory")
        self.widgetFrame = WindowFrame(AddInventoryView)

        self.widgetFrame.layout.bBack.clicked.connect(self.homepage_tab)

        self.setCentralWidget(self.widgetFrame)


class WindowFrame(QtWidgets.QWidget):
    
    def __init__(self, layout):
        super().__init__()
        self.setWindowTitle("Window")
        self.layout = layout(self)
        self.setLayout(self.layout)


class Tabs(QtWidgets.QWidget):

    def __init__(self, parent):   
        super(QtWidgets.QWidget, self).__init__(parent)
        self.layout = QtWidgets.QGridLayout(self)
        self.tabs = QtWidgets.QTabWidget()
        self.add_inventory_tab = WindowFrame(AddInventoryView)
        self.view_inventory_tab = WindowFrame(ViewInventoryList)
        self.tabs.addTab(self.add_inventory_tab,"Add Inventory")
        self.tabs.addTab(self.view_inventory_tab,"View Inventory")
        self.layout.addWidget(self.tabs)
        
if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    a_window = MainWindow()
    a_window.show()
    sys.exit(app.exec_())