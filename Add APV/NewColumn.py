import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import QHeaderView


class NewColumnView(QtWidgets.QGridLayout):
    def __init__(self, frame, current_groups):
        super().__init__()
        self.frame = frame
        self.current_groups = current_groups
        self.init_ui()
       
    def createRadio_group(self):
        self.outer_radiobutton_GroupBox = QtWidgets.QGroupBox("Please Select a Group")
        
        self.outer_radiobutton_GroupBox.setStyleSheet(""" QGroupBox{font-size: 10pt;} """)
        
        self.inner_radiobutton_GroupBox = QtWidgets.QGroupBox()
        scrollArea = QtWidgets.QScrollArea()
        
        Ggrid = QtWidgets.QGridLayout()
        boxContainer = QtWidgets.QVBoxLayout()
        
#        for n in range (0,100):
#            self.current_groups.append(self.current_groups[n%2])
 
        self.radioButtons = []
        self.radioButton_Group = QtWidgets.QButtonGroup()
        
        radioButtStylesheet = """QRadioButton{ font-size: 12pt; }"""
        
        for groupText in self.current_groups:
            radiobutton = QtWidgets.QRadioButton(groupText)
            #radiobutton.setChecked(True)
            radiobutton.setStyleSheet(radioButtStylesheet)
            radiobutton.groupText = groupText
            radiobutton.toggled.connect(self.on_radio_button_toggled)
            self.radioButtons.append(radiobutton)
        
        for i,radiobutton in enumerate(self.radioButtons):
            Ggrid.addWidget(radiobutton, i, 0)
            self.radioButton_Group.addButton(radiobutton, i)
        
        
       
        
#        GroupBoxIn ->setLayout(LayoutIn ); 
#        scrollArea->setWidget(GroupBoxIn );  
#        scrollArea->setWidgetResizable( true );  
#        LayoutOut ->addWidget(scrollArea);      
#        GroupBoxOut ->setLayout(LayoutOut ); 
        
        #Ggrid.setColumnStretch(7,4)
        Ggrid.setRowStretch(100,1)
        self.inner_radiobutton_GroupBox.setLayout(Ggrid)
        scrollArea.setWidget(self.inner_radiobutton_GroupBox)
        scrollArea.setWidgetResizable(True)
        boxContainer.addWidget(scrollArea)
        self.outer_radiobutton_GroupBox.setLayout(boxContainer)
    
    def on_radio_button_toggled(self):
        radiobutton = self.frame.sender()

        if radiobutton.isChecked():
            print("Group is %s" % (radiobutton.groupText))
    
    def init_ui(self):
        #Create Widgets
        #self.create_Group_Tree()
        
        self.createRadio_group()
        #self.outer_radiobutton_GroupBox = QtWidgets.QGroupBox("Please Select a Group")
        
        labelStyle = 'QLabel { font-size: 12pt; padding: 10px; font-weight: bold;}'
        textboxStyle = 'QLineEdit { font-size: 12pt; padding: 2px;}'
        
        
        self.lColumn = QtWidgets.QLabel("Column Name:")
        self.lColumn.setAlignment(QtCore.Qt.AlignRight)
        self.lColumn.setStyleSheet(labelStyle)
        self.tColumn = QtWidgets.QLineEdit(self.frame)
        self.tColumn.setStyleSheet(textboxStyle)
        #self.tDate.textChanged.connect(self.preview_items)
        #self.tColumn.setFixedWidth(textboxSize)
        
        
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
        
        self.bCancel = QtWidgets.QPushButton("Cancel")
        self.bCancel.setStyleSheet("""
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
        self.setColumnStretch(3,1)
        
        #self.addWidget(self.tree, 1, 1, 1, 3)
        self.addWidget(self.outer_radiobutton_GroupBox, 1, 1, 1, 3)
        self.addWidget(self.lColumn, 7,1,1,1)
        self.addWidget(self.tColumn, 7,2,1,2)
        self.addWidget(self.bAdd, 8, 1, 1, 1)
        self.addWidget(self.bNew, 8, 2, 1, 1)
        self.addWidget(self.bCancel, 8, 3, 1, 1)
        
        #self.addWidget(self.preview_GroupBox, 2, 3, 6, 2)
        
        #DEBUG
        #self.bAdd.clicked.connect(self.addColumn_names)
        #self.tree.doubleClicked.connect(self.tree_DoubleClicked)
        