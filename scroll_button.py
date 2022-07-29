# -*- coding: utf-8 -*-
 
# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
 
from PyQt4 import QtCore, QtGui
 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
 
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
 
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(485, 785)
        Dialog.setMinimumSize(QtCore.QSize(485, 400))
        Dialog.setMaximumSize(QtCore.QSize(495, 785))
        Dialog.setSizeIncrement(QtCore.QSize(1, 1))
        Dialog.setMouseTracking(False)
        Dialog.setAutoFillBackground(False)
        Dialog.setModal(False)
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 736, 471, 49))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.SaveCancelLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.SaveCancelLayout.setContentsMargins(0, 8, 5, 0)
        self.SaveCancelLayout.setSpacing(10)
        self.SaveCancelLayout.setObjectName(_fromUtf8("SaveCancelLayout"))
        self.cancelButton = QtGui.QPushButton(self.layoutWidget)
        self.cancelButton.setMaximumSize(QtCore.QSize(200, 40))
        self.cancelButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.SaveCancelLayout.addWidget(self.cancelButton)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setGeometry(QtCore.QRect(10, 40, 471, 691))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 469, 689))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.layoutWidget1 = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 20, 471, 631))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout.setMargin(9)
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.line_4 = QtGui.QFrame(self.layoutWidget1)
        self.line_4.setMaximumSize(QtCore.QSize(465, 16777215))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.gridLayout.addWidget(self.line_4, 0, 0, 1, 4)
        self.logEnable = QtGui.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.logEnable.setFont(font)
        self.logEnable.setChecked(True)
        self.logEnable.setObjectName(_fromUtf8("logEnable"))
        self.buttonGroup_logging = QtGui.QButtonGroup(Dialog)
        self.buttonGroup_logging.setObjectName(_fromUtf8("buttonGroup_logging"))
        self.buttonGroup_logging.addButton(self.logEnable)
        self.gridLayout.addWidget(self.logEnable, 1, 1, 1, 1)
        self.logDisable = QtGui.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.logDisable.setFont(font)
        self.logDisable.setObjectName(_fromUtf8("logDisable"))
        self.buttonGroup_logging.addButton(self.logDisable)
        self.gridLayout.addWidget(self.logDisable, 1, 2, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
 
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
 
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Test Editor", None))
        self.cancelButton.setText(_translate("Dialog", "Stop and exit", None))
        self.logEnable.setText(_translate("Dialog", "enable logfile", None))
        self.logDisable.setText(_translate("Dialog", "disable logfile", None))
 
 
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
