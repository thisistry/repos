self.centralwidget = QtGui.QWidget(MainWindow)
    self.centralwidget.setObjectName("centralwidget")

    self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
    self.verticalLayout.setObjectName("verticalLayout")

    self.scrollArea = QtGui.QScrollArea()
    self.scrollArea.setWidgetResizable(False)
    self.scrollArea.setObjectName("scrollArea")
    self.scrollArea.setMinimumHeight(400)
    self.scrollArea.setMinimumWidth(400)
    self.scrollArea.setMaximumHeight(1200)
    self.scrollArea.setMaximumWidth(1200)

    self.verticalLayout.addWidget(self.scrollArea)

    self.scrollAreaWidgetContents = QtGui.QWidget(self.scrollArea)
    self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1400, 1200))
    self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

    self.callchildGUIs(self.scrollAreaWidgetContents)

    self.scrollArea.setWidget(self.scrollAreaWidgetContents)
    self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
    self.verticalLayout_2.setObjectName("verticalLayout_2")

    MainWindow.setCentralWidget(self.centralwidget)
