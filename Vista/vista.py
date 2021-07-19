# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 557)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(6, 6, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setEnabled(True)
        self.groupBox.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_text = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_text.setFont(font)
        self.lbl_text.setObjectName("lbl_text")
        self.verticalLayout.addWidget(self.lbl_text)
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.line_text = QtWidgets.QLineEdit(self.groupBox)
        self.line_text.setText("")
        self.line_text.setMaxLength(32768)
        self.line_text.setFrame(True)
        self.line_text.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_text.setCursorPosition(0)
        self.line_text.setDragEnabled(False)
        self.line_text.setReadOnly(False)
        self.line_text.setObjectName("line_text")
        self.verticalLayout.addWidget(self.line_text)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_push = QtWidgets.QPushButton(self.groupBox)
        self.btn_push.setObjectName("btn_push")
        self.verticalLayout.addWidget(self.btn_push)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Analizador Léxico"))
        self.groupBox.setTitle(_translate("MainWindow", "Datos de entrada"))
        self.lbl_text.setText(_translate("MainWindow", "Cadena:"))
        self.line_text.setPlaceholderText(_translate("MainWindow", "Ingrese una cadena"))
        self.btn_push.setText(_translate("MainWindow", "Analizar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())