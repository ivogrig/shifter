import mgear.core.pyqt as gqt
from mgear.vendor.Qt import QtCore, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(403, 299)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.jointNamesList = QtWidgets.QTableWidget(Form)
        self.jointNamesList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.jointNamesList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.jointNamesList.setAlternatingRowColors(True)
        self.jointNamesList.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.jointNamesList.setObjectName("jointNamesList")
        self.jointNamesList.setColumnCount(1)
        self.jointNamesList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.jointNamesList.setHorizontalHeaderItem(0, item)
        self.jointNamesList.horizontalHeader().setCascadingSectionResizes(True)
        self.jointNamesList.horizontalHeader().setDefaultSectionSize(40)
        self.jointNamesList.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout.addWidget(self.jointNamesList)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.add_pushButton = QtWidgets.QPushButton(Form)
        self.add_pushButton.setObjectName("add_pushButton")
        self.verticalLayout_2.addWidget(self.add_pushButton)
        self.remove_pushButton = QtWidgets.QPushButton(Form)
        self.remove_pushButton.setObjectName("remove_pushButton")
        self.verticalLayout_2.addWidget(self.remove_pushButton)
        self.removeAll_pushButton = QtWidgets.QPushButton(Form)
        self.removeAll_pushButton.setObjectName("removeAll_pushButton")
        self.verticalLayout_2.addWidget(self.removeAll_pushButton)
        self.line = QtWidgets.QFrame(Form)
        self.line.setMinimumSize(QtCore.QSize(0, 16))
        self.line.setBaseSize(QtCore.QSize(0, 0))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.moveUp_pushButton = QtWidgets.QPushButton(Form)
        self.moveUp_pushButton.setObjectName("moveUp_pushButton")
        self.verticalLayout_2.addWidget(self.moveUp_pushButton)
        self.moveDown_pushButton = QtWidgets.QPushButton(Form)
        self.moveDown_pushButton.setObjectName("moveDown_pushButton")
        self.verticalLayout_2.addWidget(self.moveDown_pushButton)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(gqt.fakeTranslate("Form", "Form", None, -1))
        self.label.setText(gqt.fakeTranslate("Form", "Joint Names", None, -1))
        self.jointNamesList.horizontalHeaderItem(0).setText(gqt.fakeTranslate("Form", "Name", None, -1))
        self.add_pushButton.setText(gqt.fakeTranslate("Form", "Add", None, -1))
        self.remove_pushButton.setText(gqt.fakeTranslate("Form", "Remove", None, -1))
        self.removeAll_pushButton.setText(gqt.fakeTranslate("Form", "Remove All", None, -1))
        self.moveUp_pushButton.setText(gqt.fakeTranslate("Form", "Move Up", None, -1))
        self.moveDown_pushButton.setText(gqt.fakeTranslate("Form", "Move Down", None, -1))

