# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(1400, 1000)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 180, 1081, 761))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAutoFillBackground(False)
        self.title.setStyleSheet("font-size: 30px;")
        self.title.setTextFormat(QtCore.Qt.AutoText)
        self.title.setScaledContents(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setWordWrap(False)
        self.title.setObjectName("title")
        self.verticalLayout.addWidget(self.title)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.LRL_frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.LRL_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LRL_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LRL_frame.setObjectName("LRL_frame")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.LRL_frame)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(0, -10, 501, 151))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.LRL = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.LRL.setFont(font)
        self.LRL.setTextFormat(QtCore.Qt.AutoText)
        self.LRL.setScaledContents(True)
        self.LRL.setObjectName("LRL")
        self.verticalLayout_9.addWidget(self.LRL)
        self.LRL_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_9)
        self.LRL_input.setObjectName("LRL_input")
        self.verticalLayout_9.addWidget(self.LRL_input)
        self.horizontalLayout_10.addLayout(self.verticalLayout_9)
        self.LRL_value = QtWidgets.QLabel(self.horizontalLayoutWidget_9)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.LRL_value.setFont(font)
        self.LRL_value.setObjectName("LRL_value")
        self.horizontalLayout_10.addWidget(self.LRL_value)
        self.horizontalLayout_2.addWidget(self.LRL_frame)
        self.URL_frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.URL_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.URL_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.URL_frame.setObjectName("URL_frame")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.URL_frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(-1, -1, 501, 141))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.URL = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.URL.setFont(font)
        self.URL.setScaledContents(True)
        self.URL.setObjectName("URL")
        self.verticalLayout_3.addWidget(self.URL)
        self.URL_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.URL_input.setObjectName("URL_input")
        self.verticalLayout_3.addWidget(self.URL_input)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.URL_value = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.URL_value.setFont(font)
        self.URL_value.setObjectName("URL_value")
        self.horizontalLayout_4.addWidget(self.URL_value)
        self.horizontalLayout_2.addWidget(self.URL_frame)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.APW_frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.APW_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.APW_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.APW_frame.setObjectName("APW_frame")
        self.horizontalLayoutWidget_7 = QtWidgets.QWidget(self.APW_frame)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(-1, -1, 501, 151))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.APW = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.APW.setFont(font)
        self.APW.setScaledContents(True)
        self.APW.setObjectName("APW")
        self.verticalLayout_7.addWidget(self.APW)
        self.APW_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_7)
        self.APW_input.setObjectName("APW_input")
        self.verticalLayout_7.addWidget(self.APW_input)
        self.horizontalLayout_8.addLayout(self.verticalLayout_7)
        self.APW_value = QtWidgets.QLabel(self.horizontalLayoutWidget_7)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.APW_value.setFont(font)
        self.APW_value.setObjectName("APW_value")
        self.horizontalLayout_8.addWidget(self.APW_value)
        self.horizontalLayout_3.addWidget(self.APW_frame)
        self.AA_frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.AA_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AA_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AA_frame.setObjectName("AA_frame")
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.AA_frame)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(-1, -1, 501, 151))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.AA = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.AA.setFont(font)
        self.AA.setScaledContents(True)
        self.AA.setObjectName("AA")
        self.verticalLayout_6.addWidget(self.AA)
        self.AA_input = QtWidgets.QLineEdit(self.horizontalLayoutWidget_6)
        self.AA_input.setObjectName("AA_input")
        self.verticalLayout_6.addWidget(self.AA_input)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        self.AA_value = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.AA_value.setFont(font)
        self.AA_value.setObjectName("AA_value")
        self.horizontalLayout_7.addWidget(self.AA_value)
        self.horizontalLayout_3.addWidget(self.AA_frame)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)

        self.retranslateUi(Main)
        self.comboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main)

        self.comboBox.currentTextChanged.connect(self.switchMode)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "MainWindow"))
        self.title.setText(_translate("Main", "AOO Mode"))
        self.comboBox.setCurrentText(_translate("Main", "AOO"))
        self.comboBox.setItemText(0, _translate("Main", "AOO"))
        self.comboBox.setItemText(1, _translate("Main", "VOO"))
        self.comboBox.setItemText(2, _translate("Main", "AAI"))
        self.comboBox.setItemText(3, _translate("Main", "VVI"))
        self.LRL.setText(_translate("Main", "Lower Rate Limit (bpm)"))
        self.LRL_value.setText(_translate("Main", "N/A"))
        self.URL.setText(_translate("Main", "Upper Rate Limit (bpm)"))
        self.URL_value.setText(_translate("Main", "N/A"))
        self.APW.setText(_translate("Main", "Atrial Pulse Width (ms)"))
        self.APW_value.setText(_translate("Main", "N/A"))
        self.AA.setText(_translate("Main", "Atrial Amplitude (V)"))
        self.AA_value.setText(_translate("Main", "N/A"))
    
    def switchMode(self):
        self.title.setText(self.comboBox.currentText() + " Mode")
        self.LRL_frame.hide()
        self.URL_frame.hide()
        # self.AA_frame.hide()
        # self.APW_frame.hide()
        
        # if self.comboBox_pacing_mode.currentText() == "VOO":
        #     self.frame_lower_rate_limit.show()
        #     self.frame_upper_rate_limit.show()
        #     self.frame_ventricular_amplitude.show()
        #     self.frame_ventricular_pulse_width.show()

        # elif self.comboBox_pacing_mode.currentText() == "AOO":
        #     self.frame_lower_rate_limit.show()
        #     self.frame_upper_rate_limit.show()
        #     self.frame_atrial_amplitude.show()
        #     self.frame_atrial_pulses_width.show()

        # elif self.comboBox_pacing_mode.currentText() == "AAI":
        #     self.label_pacing_mode.setStyleSheet("font: 12pt 'MS Shell Dlg 2';color:rgb(255, 170, 0);")
        #     self.frame_lower_rate_limit.show()
        #     self.frame_upper_rate_limit.show()
        #     self.frame_atrial_amplitude.show()
        #     self.frame_atrial_pulses_width.show()
        #     self.frame_atrial_sensitivity.show()
        #     self.frame_atrial_refractory_period.show()
        #     self.frame_hysteresis.show()
        #     self.frame_rate_smoothing.show()

        # elif self.comboBox_pacing_mode.currentText() == "VVI":
        #     self.label_pacing_mode.setStyleSheet("font: 12pt 'MS Shell Dlg 2';color: rgb(0, 170, 255);")
        #     self.frame_lower_rate_limit.show()
        #     self.frame_upper_rate_limit.show()
        #     self.frame_ventricular_amplitude.show()
        #     self.frame_ventricular_pulse_width.show()
        #     self.frame_ventricular_sensitivity.show()
        #     self.frame_ventricular_refractory_period.show()
        #     self.frame_hysteresis.show()
        #     self.frame_rate_smoothing.show()
