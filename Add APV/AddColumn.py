import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import Qt
from PyQt5.QtCore import (QDate, QDateTime, QRegExp, QSortFilterProxyModel, Qt, QTime)
from PyQt5.QtWidgets import QHeaderView

class Main(QtWidgets.QTreeView):
    def __init__(self):
        QtWidgets.QTreeView.__init__(self)
        
        self.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        
        self.myModel = QtGui.QStandardItemModel(self)
        
        self.setModel(self.myModel)
        self.var_column_groups = ["Personal", "Business", "Expenses"]
        self.var_column_names = [{"name":"Meals and Snacks", "group":"Personal"}, 
                        {"name":"LCG Drawing", "group":"Business"}, 
                        {"name":"Christmas Expenses", "group":"Expenses"}]
        header_name_item1 = QtGui.QStandardItem("Column Group")
        self.myModel.setHorizontalHeaderItem(0, header_name_item1)
        
    def init_tree(self):
        self.header().setStretchLastSection(False)
        self.header().setSectionResizeMode(0, QHeaderView.Stretch)
        parent = self.myModel.invisibleRootItem()
        
        for column_group in  self.var_column_groups:
            column_group_item = QtGui.QStandardItem(column_group)
            self.myModel.appendRow(column_group_item)
            for column_name in self.var_column_names:
                if column_name["group"] == column_group_item.text():
                    column_name_item = QtGui.QStandardItem(column_name["name"])
                    column_name_item.setCheckable(True)
                    column_group_item.appendRow(column_name_item)


class AddColumnView(QtWidgets.QGridLayout):
    def __init__(self, frame, cur_column_data):
        super().__init__()
        self.frame = frame
        self.column_names = []
        self.cur_column_data = cur_column_data
        print(self.cur_column_data, "here")
        self.init_ui()
    
    def input_Tree_Choices(self, groups, names):
        print(groups)
        print(names)
        self.tree.var_column_groups = groups
        self.tree.var_column_names = names
        self.tree.init_tree()
    
    def refresh_Tree(self):
        rootItem = self.tree.model().invisibleRootItem()
        for mainRootNum in range(rootItem.rowCount()):
            rowRootItem = rootItem.child(mainRootNum,0)
            print("Row:" + rowRootItem.text())
            for rowRootNum in range(rowRootItem.rowCount()):
                print("SubRow:" + rowRootItem.child(rowRootNum,0).text())
                item = rowRootItem.child(rowRootNum,0)
                print(self.cur_column_data)
                if self.cur_column_data is not None:
                    for data in self.cur_column_data:
                        print("loop self.cur_column")
                        if item.text() == data:
                            print("item", item.text(),"column", data)
                            item.setCheckState(Qt.Checked)
                            item.setEnabled(False)

    def tree_selected(self):
        items = self.tree.selectedIndexes()
        for item in items:
            crawler = item.model().itemFromIndex(item)
            if crawler.hasChildren() != True:
                print(crawler.text())
                if crawler.checkState():
                    print("checked")
                #crawler.setEnabled(False)
                #crawler.setIcon(QtGui.QIcon.fromTheme("edit-undo"))
                #print(crawler.icon())
            #print(item.model().itemFromIndex(0).text())
    def addColumn_names(self):
        rootItem = self.tree.model().invisibleRootItem()
        
        self.column_names = []
        for mainRootNum in range(rootItem.rowCount()):
            rowRootItem = rootItem.child(mainRootNum,0)
            #print("Row:" + rowRootItem.text())
            for rowRootNum in range(rowRootItem.rowCount()):
                #print("SubRow:" + rowRootItem.child(rowRootNum,0).text())
                item = rowRootItem.child(rowRootNum,0)
                if item.checkState() and item.isEnabled():
                    print(item.text())
                    self.column_names.append(item.text())
        #self.frame.close()
        
    
    def init_ui(self):
        #Create Widgets
       
        self.tree = Main()
        self.tree.setStyleSheet(""" QTreeView 
        { 
            font-size: 12pt; 
        }""")
        
        self.addWidget(self.tree ,1,1,1,3)
        self.refresh_Tree()
        
        self.bSubmit = QtWidgets.QPushButton("Submit")
        self.bSubmit.setStyleSheet("""
        QPushButton 
        { 
            font-size: 14pt; 
            padding: 10px; 
            color: #fff; 
            background-color: #5cb85c; 
            border-color: #4cae4c;
            border-radius: 5px;
            margin-top: 10px;
        }
        QPushButton:hover 
        {
            background-color: #4baa4b; 
            border-color: 
            #409140;
        }
        """)
        
        self.bAdd = QtWidgets.QPushButton("Add")
        self.bAdd.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; background-color: #5cb85c; border-color: #4cae4c;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #4baa4b; border-color: #409140;}""")
        
        self.bNew = QtWidgets.QPushButton("New")
        self.bNew.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; 
        background-color: #f0ad4e;
        border-color: #eea236;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #eb961e; border-color: #eb961e;}""")
        
        self.bCancel = QtWidgets.QPushButton("Cancel")
        self.bCancel.setStyleSheet("""QPushButton { font-size: 14pt; padding: 10px; color: #fff; 
        background-color: #d9534f;
        border-color: #d43f3a;
                                                    border-radius: 5px;
                                                    margin-top: 10px;}
                                        QPushButton:hover {background-color: #d5443f; border-color: #d8504b;}""")
        
        self.addWidget(self.bAdd, 8, 1, 1, 1)
        self.addWidget(self.bNew, 8, 2, 1, 1)
        self.addWidget(self.bCancel, 8, 3, 1, 1)
        
        #self.addWidget(self.preview_GroupBox, 2, 3, 6, 2)
        
        #DEBUG
        #self.bAdd.clicked.connect(self.addColumn_names)
        #self.tree.doubleClicked.connect(self.tree_DoubleClicked)
        