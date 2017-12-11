import sys
from PyQt5 import QtWidgets,QtCore

class AddNewConfirm(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.frame.setWindowTitle("Confirmation")
        self.init_ui()

    def add_to_table(self, row, column, text):
        self.tProduct_Table.setItem(row,column,QtWidgets.QTableWidgetItem(text))

    def init_ui(self):
        #Create Widgets

        self.lConfirmation = QtWidgets.QLabel("Are you sure you want to add this product?")
        self.lConfirmation.setStyleSheet('QLabel { font-size: 12pt; padding: 10px;}')

        self.tProduct_Table = QtWidgets.QTableWidget()
        self.tProduct_Table.setColumnCount(6)
        self.tProduct_Table.setRowCount(1)
        self.tProduct_Table.setHorizontalHeaderLabels(["Articles", "Supplier", "Unit", "Retail Price",
         "Unit Price", "Vatable"])
        self.tProduct_Table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        tablewidth = self.tProduct_Table.width() + 6
        self.tProduct_Table.setColumnWidth(0, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(1, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(2, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(3, tablewidth / 6)       
        self.tProduct_Table.setColumnWidth(4, tablewidth / 6)
        self.tProduct_Table.setColumnWidth(5, tablewidth / 6)
        self.tProduct_Table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers) 

        self.bConfirm = QtWidgets.QPushButton("Confirm")
        self.bConfirm.setStyleSheet('QPushButton {color: white;background-color: #47c468;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 6px;}')
        self.bConfirm.setFixedWidth(200)

        self.bBack = QtWidgets.QPushButton("Cancel")
        self.bBack.setStyleSheet('QPushButton {color: white;background-color: #ff0000;border-style: outset;border-width: 2px;border-radius: 10px;border-color: beige;font: bold 14px;min-width: 10em;padding: 4px;}')
        self.bBack.setFixedWidth(80)
        
        self.setColumnStretch(6,1)
        self.setColumnStretch(1,1)
        self.setRowStretch(13,1)

        self.addWidget(self.lConfirmation, 1, 2, 1, 3, QtCore.Qt.AlignCenter)
        self.addWidget(self.tProduct_Table, 2, 2, 4, 3, QtCore.Qt.AlignCenter)   
        self.addWidget(self.bConfirm, 6, 2, 1, 2, QtCore.Qt.AlignCenter)
        self.addWidget(self.bBack, 6, 3, 1, 2, QtCore.Qt.AlignCenter)        

        
class WindowFrame(QtWidgets.QWidget):
    def __init__(self, layout):
        super().__init__()
        self.setWindowTitle("Confirmation")
        self.layout = layout(self)
        self.setLayout(self.layout)

class ConfirmWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(ConfirmWindow, self).__init__(parent)
        self.resize(800,200)
        self.layout = WindowFrame(AddNewConfirm)
        self.setCentralWidget(self.layout)