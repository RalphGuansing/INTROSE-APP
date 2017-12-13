import sys
from PyQt5 import QtWidgets,QtCore
from Admin import AdminView

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        #self.setFixedSize(1024,720)
        self.resize(1500,720)
        self.home_invoice_tab()

    def view_list_tab(self):
        self.setWindowTitle("Invoice")
        self.widgetFrame = WindowFrame(InvList)

        self.widgetFrame.layout.bBack.clicked.connect(self.home_invoice_tab)

        self.setCentralWidget(self.widgetFrame)    


if __name__ == "__main__":    
    app = QtWidgets.QApplication(sys.argv)
    a_window = MainWindow()
    a_window.show()
    sys.exit(app.exec_())