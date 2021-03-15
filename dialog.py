# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'makebeautiful.ui'

#

# Created by: PyQt5 UI code generator 5.12

#

# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ZValue(object):

    def setupUi(self, ZValue):

        ZValue.setObjectName("ZValue")

        ZValue.resize(400, 300)

        self.lineEdit = QtWidgets.QLineEdit(ZValue)

        self.lineEdit.setGeometry(QtCore.QRect(130, 70, 131, 41))

        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(ZValue)

        self.pushButton.setGeometry(QtCore.QRect(130, 150, 131, 41))

        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(ZValue)

        QtCore.QMetaObject.connectSlotsByName(ZValue)

    def retranslateUi(self, ZValue):

        _translate = QtCore.QCoreApplication.translate

        ZValue.setWindowTitle(_translate("ZValue", "Copy Z Cordinate"))

        self.pushButton.setText(_translate("ZValue", "Cofirm"))

import sys

from PyQt5.QtWidgets import QDialog,QApplication

from  makebeautiful import *

class MyForm(QDialog):

    def __init__(self):

        super().__init__()

        self.ui=Ui_ZValue()

        # self.ui.setWindowFlag(Qt.WindowMinimizeButtonHint, True)

        # self.ui.setWindowFlag(Qt.WindowMaximizeButtonHint, True)

        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.dispmessage)

        self.show()

    def dispmessage(self):

        self.ui.lineEdit.setText("Clicked")

if __name__=="__main__":

    app=QApplication(sys.argv)

    w=MyForm()

    w.show()

    sys.exit(app.exec_())

    
    
    
    threadCount = QThreadPool.globalInstance().maxThreadCount()
        self.label.setText(f"Running {threadCount} Threads")
        pool = QThreadPool.globalInstance()
        for i in range(threadCount):
            # 2. Instantiate the subclass of QRunnable
            runnable = Runnable(i)
            # 3. Call start()
            pool.start(runnable)
