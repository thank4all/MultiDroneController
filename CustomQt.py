from PyQt5 import QtCore, QtGui, QtWidgets

class ControllerDroneInfo(QtWidgets.QWidget):
    def __init__(self,parent, verticalLayout_2):
        super(ControllerDroneInfo, self).__init__(parent)
        self.setupUI(verticalLayout_2)
        self.bindFuncs()

        self.ip = "999.999.999.999"
        self.port = 8889
        self.bControl = False
    def updateIP(self):
        ip = self.Qt_ipInput.text()
        ipStrs = ip.split('.')
        if len(ipStrs) != 4:
            return False
        for ipStr in ipStrs:
            try:
                if int(ipStr) < 0 or 255 < int(ipStr):
                    return False
            except:
                return False
        self.ip = ip
        return True
    def update_bControl(self):
        self.bControl = self.Qt_bControl.isChecked()

    def bindFuncs(self):
        self.Qt_ipInput.textChanged.connect(self.updateIP)
        self.Qt_bControl.stateChanged.connect(self.update_bControl)
    def setupUI(self, verticalLayout_2):
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMaximumSize(QtCore.QSize(16777215, 40))
        self.setBaseSize(QtCore.QSize(0, 0))
        self.setObjectName("Qt_ControlDroneInfo")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(6)
        self.Qt_ipStatic = QtWidgets.QLabel(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Qt_ipStatic.sizePolicy().hasHeightForWidth())
        self.Qt_ipStatic.setSizePolicy(sizePolicy)
        self.Qt_ipStatic.setObjectName("Qt_ipStatic")
        self.horizontalLayout.addWidget(self.Qt_ipStatic)
        self.Qt_ipInput = QtWidgets.QLineEdit(self)
        self.Qt_ipInput.setObjectName("Qt_ipInput")
        self.horizontalLayout.addWidget(self.Qt_ipInput)
        self.Qt_bControl = QtWidgets.QCheckBox(self)
        self.Qt_bControl.setObjectName("Qt_bControl")
        self.horizontalLayout.addWidget(self.Qt_bControl)
        idx = verticalLayout_2.count() -1
        verticalLayout_2.insertWidget(idx,self)
        self.Qt_ipStatic.setText("IP")
        self.Qt_bControl.setText("Control this")