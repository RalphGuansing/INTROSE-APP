import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QHeaderView


class NewGroupView(QtWidgets.QGridLayout):
    def __init__(self, frame):
        super().__init__()
        self.frame = frame
        self.init_ui()
       
    def init_ui(self):
        self.GroupName_GroupBox = QtWidgets.QGroupBox()
        Ggrid = QtWidgets.QGridLayout()
        
        labelStyle = 'QLabel { font-size: 12pt; padding: 10px; font-weight: bold;}'
        textboxStyle = 'QLineEdit { font-size: 12pt; padding: 2px;}'
        
        self.lGroup = QtWidgets.QLabel("Group Name:")
        #self.lGroup.setAlignment(QtCore.Qt.AlignRight)
        self.lGroup.setStyleSheet(labelStyle)
        self.tGroup = QtWidgets.QLineEdit(self.frame)
        self.tGroup.setStyleSheet(textboxStyle)
        #self.tDate.textChanged.connect(self.preview_items)
        #self.tColumn.setFixedWidth(textboxSize)
        Ggrid.addWidget(self.lGroup, 1, 1)
        Ggrid.addWidget(self.tGroup, 1, 2)
        
        self.GroupName_GroupBox.setLayout(Ggrid)
        
        
        self.bAdd = QtWidgets.QPushButton("Add")
        self.bAdd.setStyleSheet("""
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
            border-color: #409140;
        }
        """)
        
        self.bNew = QtWidgets.QPushButton("Add Group")
        self.bNew.setStyleSheet("""
        QPushButton 
        { 
            font-size: 14pt; 
            padding: 10px; 
            color: #fff; 
            background-color: #f0ad4e;
            border-color: #eea236;
            border-radius: 5px;
            margin-top: 10px;
        }
        QPushButton:hover 
        {
            background-color: #eb961e; 
            border-color: #eb961e;
        }
        """)
        
        self.bBack = QtWidgets.QPushButton("Back")
        self.bBack.setStyleSheet("""
        QPushButton 
        { 
            font-size: 14pt; 
            padding: 10px; 
            color: #fff; 
            background-color: #d9534f;
            border-color: #d43f3a;
            border-radius: 5px;
            margin-top: 10px;
        }
        QPushButton:hover 
        {
            background-color: #d5443f; 
            border-color: #d8504b;
        }
        """)
        
        self.setColumnStretch(1,1)
        self.setColumnStretch(2,1)
        
        #self.addWidget(self.tree, 1, 1, 1, 3)
        self.addWidget(self.GroupName_GroupBox, 2,1,1,2)
        self.addWidget(self.bAdd, 8, 1, 1, 1)
        self.addWidget(self.bBack, 8, 2, 1, 1)
        
        #self.addWidget(self.preview_GroupBox, 2, 3, 6, 2)
        
        #DEBUG
        #self.bAdd.clicked.connect(self.addColumn_names)
        #self.tree.doubleClicked.connect(self.tree_DoubleClicked)
        