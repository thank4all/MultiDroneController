# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultipleDroneController.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Qt_AddDrone = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_AddDrone.setGeometry(QtCore.QRect(210, 50, 75, 23))
        self.Qt_AddDrone.setObjectName("Qt_AddDrone")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 80, 291, 551))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.Qt_ControlDroneList = QtWidgets.QWidget()
        self.Qt_ControlDroneList.setGeometry(QtCore.QRect(0, 0, 269, 529))
        self.Qt_ControlDroneList.setObjectName("Qt_ControlDroneList")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Qt_ControlDroneList)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Qt_ControlDroneInfo = QtWidgets.QWidget(self.Qt_ControlDroneList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Qt_ControlDroneInfo.sizePolicy().hasHeightForWidth())
        self.Qt_ControlDroneInfo.setSizePolicy(sizePolicy)
        self.Qt_ControlDroneInfo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Qt_ControlDroneInfo.setBaseSize(QtCore.QSize(0, 0))
        self.Qt_ControlDroneInfo.setObjectName("Qt_ControlDroneInfo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Qt_ControlDroneInfo)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Qt_ipStatic = QtWidgets.QLabel(self.Qt_ControlDroneInfo)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Qt_ipStatic.sizePolicy().hasHeightForWidth())
        self.Qt_ipStatic.setSizePolicy(sizePolicy)
        self.Qt_ipStatic.setObjectName("Qt_ipStatic")
        self.horizontalLayout.addWidget(self.Qt_ipStatic)
        self.Qt_ipInput = QtWidgets.QLineEdit(self.Qt_ControlDroneInfo)
        self.Qt_ipInput.setObjectName("Qt_ipInput")
        self.horizontalLayout.addWidget(self.Qt_ipInput)
        self.Qt_bControl = QtWidgets.QCheckBox(self.Qt_ControlDroneInfo)
        self.Qt_bControl.setObjectName("Qt_bControl")
        self.horizontalLayout.addWidget(self.Qt_bControl)
        self.verticalLayout_2.addWidget(self.Qt_ControlDroneInfo)
        self.Qt_ControlDroneInfo_2 = QtWidgets.QWidget(self.Qt_ControlDroneList)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Qt_ControlDroneInfo_2.sizePolicy().hasHeightForWidth())
        self.Qt_ControlDroneInfo_2.setSizePolicy(sizePolicy)
        self.Qt_ControlDroneInfo_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Qt_ControlDroneInfo_2.setBaseSize(QtCore.QSize(0, 0))
        self.Qt_ControlDroneInfo_2.setObjectName("Qt_ControlDroneInfo_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Qt_ControlDroneInfo_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Qt_ipStatic_2 = QtWidgets.QLabel(self.Qt_ControlDroneInfo_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Qt_ipStatic_2.sizePolicy().hasHeightForWidth())
        self.Qt_ipStatic_2.setSizePolicy(sizePolicy)
        self.Qt_ipStatic_2.setObjectName("Qt_ipStatic_2")
        self.horizontalLayout_2.addWidget(self.Qt_ipStatic_2)
        self.Qt_ipInput_2 = QtWidgets.QLineEdit(self.Qt_ControlDroneInfo_2)
        self.Qt_ipInput_2.setObjectName("Qt_ipInput_2")
        self.horizontalLayout_2.addWidget(self.Qt_ipInput_2)
        self.Qt_bControl_2 = QtWidgets.QCheckBox(self.Qt_ControlDroneInfo_2)
        self.Qt_bControl_2.setObjectName("Qt_bControl_2")
        self.horizontalLayout_2.addWidget(self.Qt_bControl_2)
        self.verticalLayout_2.addWidget(self.Qt_ControlDroneInfo_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.Qt_ControlDroneList)
        self.verticalLayout.addWidget(self.scrollArea)
        self.Qt_logTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.Qt_logTextBox.setEnabled(True)
        self.Qt_logTextBox.setGeometry(QtCore.QRect(680, 330, 201, 301))
        self.Qt_logTextBox.setReadOnly(False)
        self.Qt_logTextBox.setObjectName("Qt_logTextBox")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 891, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Qt_ControllerIPStatic = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Qt_ControllerIPStatic.setEnabled(True)
        self.Qt_ControllerIPStatic.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Qt_ControllerIPStatic.setFont(font)
        self.Qt_ControllerIPStatic.setObjectName("Qt_ControllerIPStatic")
        self.horizontalLayout_3.addWidget(self.Qt_ControllerIPStatic)
        self.Qt_ControllerIPInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Qt_ControllerIPInput.setMaximumSize(QtCore.QSize(150, 20))
        self.Qt_ControllerIPInput.setObjectName("Qt_ControllerIPInput")
        self.horizontalLayout_3.addWidget(self.Qt_ControllerIPInput)
        self.Qt_Bind_IP = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Qt_Bind_IP.setObjectName("Qt_Bind_IP")
        self.horizontalLayout_3.addWidget(self.Qt_Bind_IP)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.Qt_DirectCommandStatic = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Qt_DirectCommandStatic.setEnabled(True)
        self.Qt_DirectCommandStatic.setMaximumSize(QtCore.QSize(100, 20))
        self.Qt_DirectCommandStatic.setObjectName("Qt_DirectCommandStatic")
        self.horizontalLayout_3.addWidget(self.Qt_DirectCommandStatic)
        self.Qt_DirectCommandInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Qt_DirectCommandInput.setMaximumSize(QtCore.QSize(150, 20))
        self.Qt_DirectCommandInput.setObjectName("Qt_DirectCommandInput")
        self.horizontalLayout_3.addWidget(self.Qt_DirectCommandInput)
        self.Qt_DefaultIPInput = QtWidgets.QLineEdit(self.centralwidget)
        self.Qt_DefaultIPInput.setGeometry(QtCore.QRect(70, 50, 131, 20))
        self.Qt_DefaultIPInput.setObjectName("Qt_DefaultIPInput")
        self.Qt_DefaultIPStatic = QtWidgets.QLabel(self.centralwidget)
        self.Qt_DefaultIPStatic.setGeometry(QtCore.QRect(10, 55, 56, 12))
        self.Qt_DefaultIPStatic.setObjectName("Qt_DefaultIPStatic")
        self.Qt_OrderStart = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_OrderStart.setGeometry(QtCore.QRect(320, 300, 75, 23))
        self.Qt_OrderStart.setObjectName("Qt_OrderStart")
        self.Qt_OrderList = QtWidgets.QListWidget(self.centralwidget)
        self.Qt_OrderList.setGeometry(QtCore.QRect(320, 330, 256, 192))
        self.Qt_OrderList.setObjectName("Qt_OrderList")
        item = QtWidgets.QListWidgetItem()
        self.Qt_OrderList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.Qt_OrderList.addItem(item)
        self.Qt_OrderStop = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_OrderStop.setGeometry(QtCore.QRect(400, 300, 75, 23))
        self.Qt_OrderStop.setObjectName("Qt_OrderStop")
        self.Qt_AddOrder = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_AddOrder.setGeometry(QtCore.QRect(460, 530, 111, 23))
        self.Qt_AddOrder.setObjectName("Qt_AddOrder")
        self.Qt_OrderInput = QtWidgets.QLineEdit(self.centralwidget)
        self.Qt_OrderInput.setGeometry(QtCore.QRect(320, 530, 131, 20))
        self.Qt_OrderInput.setObjectName("Qt_OrderInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 897, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Qt_AddDrone.setText(_translate("MainWindow", "AddDrone"))
        self.Qt_ipStatic.setText(_translate("MainWindow", "IP"))
        self.Qt_bControl.setText(_translate("MainWindow", "Control this"))
        self.Qt_ipStatic_2.setText(_translate("MainWindow", "IP"))
        self.Qt_bControl_2.setText(_translate("MainWindow", "Control this"))
        self.Qt_logTextBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">qwer</p></body></html>"))
        self.Qt_ControllerIPStatic.setText(_translate("MainWindow", "Controller IP"))
        self.Qt_Bind_IP.setText(_translate("MainWindow", "Bind"))
        self.Qt_DirectCommandStatic.setText(_translate("MainWindow", "SendCommand"))
        self.Qt_DefaultIPInput.setText(_translate("MainWindow", "192.168."))
        self.Qt_DefaultIPStatic.setText(_translate("MainWindow", "default IP"))
        self.Qt_OrderStart.setText(_translate("MainWindow", "시작"))
        __sortingEnabled = self.Qt_OrderList.isSortingEnabled()
        self.Qt_OrderList.setSortingEnabled(False)
        item = self.Qt_OrderList.item(0)
        item.setText(_translate("MainWindow", "New Item"))
        item = self.Qt_OrderList.item(1)
        item.setText(_translate("MainWindow", "New Item"))
        self.Qt_OrderList.setSortingEnabled(__sortingEnabled)
        self.Qt_OrderStop.setText(_translate("MainWindow", "중지"))
        self.Qt_AddOrder.setText(_translate("MainWindow", "Add Command"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

