class MainForm(QtGui.QWidget):
    def __init__(self, parent=None):
        super(MainForm, self).__init__()
        # init window

        self.hbox = QtGui.QHBoxLayout(self)

        self.btnbox = QtGui.QVBoxLayout()

        self.scroll = QtGui.QScrollArea(self)

        self.table = QtGui.QTableWidget(self)

        self.spltr = QtGui.QSplitter(QtCore.Qt.Horizontal)

        self.setWindowTitle("...")

        self.table.setColumnCount(3)
        self.table.move(11,220)
        self.table.verticalHeader().hide()
        self.table.setHorizontalHeaderLabels(["Key","Full","HR"])

        dic = {}
        for i in range(30):
            dic['foo '+str(i)] = [i]

        for key, val1 in sorted(dic.iteritems()):
            btn = QtGui.QPushButton(key, self)
            self.btnbox.addWidget(btn)

        # must place layout into a widget before adding to QScrollArea
        holder = QtGui.QWidget()
        holder.setLayout(self.btnbox)
        self.scroll.setWidget(holder)  
        self.spltr.addWidget(self.scroll)
        self.spltr.addWidget(self.table)         

        self.hbox.addWidget(self.spltr)
