# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MultipleDroneController.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import CustomQt
import socket
import traceback
import threading
import time
from threading import Lock
class Ui_MainWindow(object):
    def __init__(self, MainWindow):
        super().__init__()
        self.logBuffer = []
        self.logWriteTimer = QtCore.QTimer()
        self.logWriteTimer.timeout.connect(self.logWriter)
        self.logWriteTimer.start(10)

        self.setupUi(MainWindow)
        self.bindFuncs()

        self.controlDrones = []
        self.addDrone()

        self.controlSocket = None

        self.controllerAddr = ["999.999.999.999",8889]
        self.updateIP()

        self.bOrdering = False

        th = threading.Thread(target=self.recvThread)
        th.daemon=True
        th.start()

        th = threading.Thread(target=self.doNotLand)
        th.daemon=True
        th.start()
    def logWriter(self):
        for logStr in self.logBuffer:
            self.Qt_logTextBox.append(logStr)
        if len(self.logBuffer) > 0:
            self.Qt_logTextBox.verticalScrollBar().setValue(self.Qt_logTextBox.verticalScrollBar().maximum())
        self.logBuffer.clear()
    def log(self, logStr):
            logStr = logStr.strip()
            self.logBuffer.append(logStr)

    # Controller
    def updateIP(self):
        ip = self.Qt_ControllerIPInput.text()
        ipStrs = ip.split('.')
        if len(ipStrs) != 4:
            return False
        for ipStr in ipStrs:
            try:
                if int(ipStr) < 0 or 255 < int(ipStr):
                    return False
            except:
                return False
        self.controllerAddr[0] = ip
        return True
    def controlSocketBind(self):
        try:
            if self.controlSocket is not None:
                self.controlSocket.close()
            self.controlSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.controlSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
            #self.controlSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1)
            self.controlSocket.bind(tuple(self.controllerAddr))
            self.log("Bind Success: " + self.controllerAddr[0]+ ":" + self.controllerAddr[1].__str__())
        except Exception as error:
            traceback.print_exc()
            self.log("Bind Failed : " + error.__str__())
            print("catch")
    def sendDirectCMD(self):
        if self.controlSocket is None:
            self.log("바인딩되지 않았습니다.")
            return False
        cmd = self.Qt_DirectCommandInput.text()
        encodedCMD = cmd.encode('utf-8')
        for drone in self.controlDrones:
            if drone.bControl:
                try:
                    self.controlSocket.sendto(encodedCMD,(drone.ip,drone.port))
                    self.log('send direct : ' + cmd + ' to ' + drone.ip)
                except:
                    traceback.print_exc()
                    print('catch')
        self.Qt_DirectCommandInput.setText('')
        return True

    # OrderList
    def addOrder(self,str=None):
        if str is None:
            str = self.Qt_OrderInput.text()
            if str == '':
                return
        idx = self.Qt_OrderList.currentRow()+1


        item = QtWidgets.QListWidgetItem()
        self.Qt_OrderList.insertItem(idx, item)
        item.setText(str)
        self.Qt_OrderList.setCurrentRow(idx)

        self.Qt_OrderInput.setText('')
    def removeOrder(self):
        idx = self.Qt_OrderList.currentRow()
        self.Qt_OrderList.takeItem(idx)
    def orderSave(self):
        filename = self.Qt_Filename.text()
        if filename == '':
            self.log('please input fileName')
            return
        f = open(filename,'w')
        for i in range(self.Qt_OrderList.count()):
            f.write(self.Qt_OrderList.item(i).text() + '\n')
        f.close()
        self.log(filename + ' file saved')
        pass
    def orderLoad(self):
        filename=self.Qt_Filename.text()
        try:
            f = open(filename, 'r')
            self.Qt_OrderList.clear()
            strs = f.readlines()
            for str in strs:
                self.addOrder(str.strip())
            f.close()
        except Exception as err:
            traceback.print_exc()
            self.log(err.__str__())

    def orderStart(self):
        if self.bOrdering:
            self.log('이미 실행중인 오더가 있습니다.')
            return
        self.bOrdering = True
        th = threading.Thread(target=self.orderThread)
        th.daemon = True
        th.start()
    def orderStop(self):
        self.bOrdering = False
    def orderThread(self):
        curOrderIdx = 0
        while self.bOrdering:
            curOrder = self.Qt_OrderList.item(curOrderIdx)
            if curOrder is None:
                break
            self.Qt_OrderList.setCurrentRow(curOrderIdx)
            cmd = curOrder.text()
            if not self.sendOrderedCommand(cmd):
                self.log('order재생중 오류')
                break
            curOrderIdx+=1
            #time.sleep(0.1)
        if not self.bOrdering:
            self.log('order 중지')

        self.bOrdering = False
        self.log('order가 종료되었습니다.')
    def sendOrderedCommand(self, cmd):
        if self.controlSocket is None:
            self.log("바인딩되지 않았습니다.")
            return False
        try:
            bSendAll = False
            cmdSplitRes=cmd.split(' ')
            if cmdSplitRes[0] == 'sleep':
                sleepTime = float(cmdSplitRes[1])
                self.log('ORDER: '+ cmd)
                time.sleep(sleepTime)
                return True
            else:
                targetDroneIdxs = []
                cmdStartIdx = 0
                if cmdSplitRes[0] == 'all':
                    bSendAll = True
                    cmdStartIdx = 1
                else:
                    for i, cmdSag in enumerate(cmdSplitRes):
                        try:
                            num = int(cmdSag)
                            targetDroneIdxs.append(num)
                        except:
                            cmdStartIdx = i
                            break
                cmds = cmdSplitRes[cmdStartIdx:]
                cmd = ''
                for i, cmdSag in enumerate(cmds):
                    if i != cmds.__len__()-1:
                        cmd += (cmdSag+' ')
                    else:
                        cmd += cmdSag
                encodedCMD = cmd.encode('utf-8')

                if not bSendAll:
                    for idx in targetDroneIdxs:
                        drone = self.controlDrones[idx]
                        if drone.bControl:
                            try:
                                self.controlSocket.sendto(encodedCMD,(drone.ip,drone.port))
                                self.log('ORDER: ' + cmd + ' to ' + drone.ip)
                            except:
                                traceback.print_exc()
                                print('catch')
                                self.log('Order송신중 오류')
                                return False
                else:
                    for drone in self.controlDrones:
                        if drone.bControl:
                            try:
                                self.controlSocket.sendto(encodedCMD,(drone.ip,drone.port))
                                self.log('ORDER: ' + cmd + ' to ' + drone.ip)
                            except:
                                traceback.print_exc()
                                print('catch')
                                self.log('Order송신중 오류')
                                return False
                return True
        except:
            traceback.print_exc()
            self.log('Order해석오류')
            return False

    # ControlDrones
    def addDrone(self):
        defaultIP = self.Qt_DefaultIPInput.text()
        newDrone = CustomQt.ControllerDroneInfo(self.Qt_ControlDroneList, self.verticalLayout_2)
        newDrone.ip = defaultIP
        newDrone.Qt_ipInput.setText(defaultIP)
        self.controlDrones.append(newDrone)

    #Thread
    def doNotLand(self):
            while True:
                if self.controlSocket is None:
                    continue
                self.log('doNotLand run')
                cmd = 'command'
                encodedCMD = cmd.encode('utf-8')
                for drone in self.controlDrones:
                    if drone.bControl:
                        try:
                            self.controlSocket.sendto(encodedCMD, (drone.ip, drone.port))
                        except:
                            traceback.print_exc()
                            print('catch')
                time.sleep(12)
    def recvThread(self):
        while True:
            try:
                if self.controlSocket is not None:
                    response, ip = self.controlSocket.recvfrom(1024)
                    response = response.decode('utf-8')
                    self.log(ip[0] + " : " + response)
            except:
                traceback.print_exc()
                print('catch')

    # UI
    def bindFuncs(self):
        self.Qt_AddDrone.clicked.connect(self.addDrone)
        self.Qt_Bind_IP.clicked.connect(self.controlSocketBind)
        self.Qt_ControllerIPInput.textChanged.connect(self.updateIP)
        self.Qt_DirectCommandInput.returnPressed.connect(self.sendDirectCMD)
        self.Qt_RemoveOrder.clicked.connect(self.removeOrder)
        self.Qt_OrderInput.returnPressed.connect(self.addOrder)
        self.Qt_OrderStart.clicked.connect(self.orderStart)
        self.Qt_OrderStop.clicked.connect(self.orderStop)
        self.Qt_OrderSave.clicked.connect(self.orderSave)
        self.Qt_OrderLoad.clicked.connect(self.orderLoad)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(897, 673)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Qt_AddDrone = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_AddDrone.setGeometry(QtCore.QRect(210, 50, 75, 23))
        self.Qt_AddDrone.setObjectName("Qt_AddDrone")
        self.Qt_DefaultIPInput = QtWidgets.QLineEdit(self.centralwidget)
        self.Qt_DefaultIPInput.setGeometry(QtCore.QRect(70, 50, 131, 20))
        self.Qt_DefaultIPInput.setObjectName("Qt_DefaultIPInput")
        self.Qt_DefaultIPStatic = QtWidgets.QLabel(self.centralwidget)
        self.Qt_DefaultIPStatic.setGeometry(QtCore.QRect(10, 55, 56, 12))
        self.Qt_DefaultIPStatic.setObjectName("Qt_DefaultIPStatic")
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
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.scrollArea.setWidget(self.Qt_ControlDroneList)
        self.verticalLayout.addWidget(self.scrollArea)
        self.Qt_logTextBox = QtWidgets.QTextEdit(self.centralwidget)
        self.Qt_logTextBox.setEnabled(True)
        self.Qt_logTextBox.setGeometry(QtCore.QRect(590, 330, 291, 301))
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
        # find current local ip
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ipStr = s.getsockname()[0]
        except OSError as error:
            self.log("자동으로 사설ip를 잡는데에 실패했습니다.")
            ipStr = '192.168.10.2'
        self.Qt_ControllerIPInput.setText(ipStr)
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.Qt_OrderStart = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_OrderStart.setGeometry(QtCore.QRect(320, 300, 75, 23))
        self.Qt_OrderStart.setObjectName("Qt_OrderStart")
        self.Qt_OrderList = QtWidgets.QListWidget(self.centralwidget)
        self.Qt_OrderList.setGeometry(QtCore.QRect(320, 330, 256, 192))
        self.Qt_OrderList.setObjectName("Qt_OrderList")
        item = QtWidgets.QListWidgetItem()
        self.Qt_OrderList.addItem(item)
        self.Qt_OrderStop = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_OrderStop.setGeometry(QtCore.QRect(400, 300, 75, 23))
        self.Qt_OrderStop.setObjectName("Qt_OrderStop")
        self.Qt_RemoveOrder = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_RemoveOrder.setGeometry(QtCore.QRect(460, 530, 111, 23))
        self.Qt_RemoveOrder.setObjectName("Qt_RemoveOrder")
        self.Qt_OrderInput = QtWidgets.QLineEdit(self.centralwidget)
        self.Qt_OrderInput.setGeometry(QtCore.QRect(320, 530, 131, 20))
        self.Qt_OrderInput.setObjectName("Qt_OrderInput")
        self.Qt_OrderSave = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_OrderSave.setGeometry(QtCore.QRect(420, 560, 71, 23))
        self.Qt_OrderSave.setObjectName("Qt_OrderSave")
        self.Qt_OrderLoad = QtWidgets.QPushButton(self.centralwidget)
        self.Qt_OrderLoad.setGeometry(QtCore.QRect(500, 560, 71, 23))
        self.Qt_OrderLoad.setObjectName("Qt_OrderLoad")
        self.Qt_Filename = QtWidgets.QLineEdit(self.centralwidget)
        self.Qt_Filename.setGeometry(QtCore.QRect(320, 560, 91, 20))
        self.Qt_Filename.setObjectName("Qt_Filename")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MultipleDroneController - made by AINukeHere(iii4625@naver.com)"))
        self.Qt_AddDrone.setText(_translate("MainWindow", "AddDrone"))
        self.Qt_logTextBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.Qt_ControllerIPStatic.setText(_translate("MainWindow", "Controller IP"))
        self.Qt_Bind_IP.setText(_translate("MainWindow", "Bind"))
        self.Qt_DirectCommandStatic.setText(_translate("MainWindow", "SendCommand"))
        self.Qt_DefaultIPInput.setText(_translate("MainWindow", "192.168."))
        self.Qt_DefaultIPStatic.setText(_translate("MainWindow", "default IP"))
        self.Qt_OrderStart.setText(_translate("MainWindow", "시작"))
        __sortingEnabled = self.Qt_OrderList.isSortingEnabled()
        self.Qt_OrderList.setSortingEnabled(False)
        item = self.Qt_OrderList.item(0)
        item.setText(_translate("MainWindow", "all command"))
        self.Qt_OrderList.setSortingEnabled(__sortingEnabled)
        self.Qt_OrderStop.setText(_translate("MainWindow", "중지"))
        self.Qt_RemoveOrder.setText(_translate("MainWindow", "Remove Order"))
        self.Qt_OrderSave.setText(_translate("MainWindow", "Save"))
        self.Qt_OrderLoad.setText(_translate("MainWindow", "Load"))




