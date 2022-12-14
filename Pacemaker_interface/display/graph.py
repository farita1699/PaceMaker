# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'graphsprelim.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Graph(object):
    def setupUi(self, Graph):
        Graph.setObjectName("Graph")
        Graph.resize(1201, 869)
        self.centralwidget = QtWidgets.QWidget(Graph)
        self.centralwidget.setStyleSheet("QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"    border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color:rgb(33, 33, 33)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_welcome = QtWidgets.QLabel(self.frame_7)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_welcome.sizePolicy().hasHeightForWidth())
        self.label_welcome.setSizePolicy(sizePolicy)
        self.label_welcome.setStyleSheet("color:white;\n"
"\n"
"")
        self.label_welcome.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_welcome.setObjectName("label_welcome")
        self.horizontalLayout_3.addWidget(self.label_welcome)
        self.btn_close = QtWidgets.QPushButton(self.frame_7)
        self.btn_close.setStyleSheet("color:white;\n"
"background-color:rgb(54, 54, 54);\n"
"border-radius:5px;\n"
"")
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_3.addWidget(self.btn_close)
        self.btn_settings = QtWidgets.QPushButton(self.frame_7)
        self.btn_settings.setStyleSheet("background:transparent")
        self.btn_settings.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resources/images/settings-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_settings.setIcon(icon)
        self.btn_settings.setIconSize(QtCore.QSize(25, 25))
        self.btn_settings.setObjectName("btn_settings")
        self.horizontalLayout_3.addWidget(self.btn_settings)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: rgb(54, 54, 54);\n"
"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(54,54,54,255), stop:0.497326 rgba(54,54,54,255), stop:1 rgba(55,55,55,255));")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet("color:white")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_plots_checks = QtWidgets.QFrame(self.groupBox)
        self.frame_plots_checks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_plots_checks.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_plots_checks.setObjectName("frame_plots_checks")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_plots_checks)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(166, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(166, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_2.addWidget(self.frame_plots_checks)
        self.frame_atrial = QtWidgets.QFrame(self.groupBox)
        self.frame_atrial.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_atrial.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_atrial.setObjectName("frame_atrial")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_atrial)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(526, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addWidget(self.frame_atrial)
        self.EGram_comboBox = QtWidgets.QComboBox(self.groupBox)
        self.EGram_comboBox.setObjectName("EGram_comboBox")
        self.EGram_comboBox.addItem("")
        self.EGram_comboBox.addItem("")
        self.EGram_comboBox.addItem("")
        self.verticalLayout_2.addWidget(self.EGram_comboBox)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.plots = PlotWidget(self.groupBox)
        self.plots.setObjectName("plots")
        self.verticalLayout_2.addWidget(self.plots)
        self.frame_ventricular = QtWidgets.QFrame(self.groupBox)
        self.frame_ventricular.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ventricular.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ventricular.setObjectName("frame_ventricular")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_ventricular)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(526, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_2.addWidget(self.frame_ventricular)
        self.horizontalLayout.addWidget(self.groupBox)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout.addWidget(self.frame_2)
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setStyleSheet("background-color:rgb(156, 156, 156);\n"
"border:1px inset black;")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        Graph.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(Graph)
        self.statusBar.setStyleSheet("background-color:rgb(33, 33, 33)")
        self.statusBar.setObjectName("statusBar")
        Graph.setStatusBar(self.statusBar)
        
       #new
        self.btn_close.clicked.connect(Graph.close)
        self.EGram_comboBox.currentTextChanged.connect(self.switchPlot)
        #end of new^^ 
        self.retranslateUi(Graph)
        QtCore.QMetaObject.connectSlotsByName(Graph)

    def retranslateUi(self, Graph):
        _translate = QtCore.QCoreApplication.translate
        Graph.setWindowTitle(_translate("Graph", "Pacemaker: Graph"))
        self.label_welcome.setText(_translate("Graph", "Welcome, "))
        self.btn_close.setText(_translate("Graph", "Close Graph"))
        self.groupBox.setTitle(_translate("Graph", "Egram Data: "))
        self.EGram_comboBox.setItemText(0, _translate("Graph", "Atrial Data"))
        self.EGram_comboBox.setItemText(1, _translate("Graph", "Ventricular Data"))
        self.EGram_comboBox.setItemText(2, _translate("Graph", "Both "))
from pyqtgraph import PlotWidget
