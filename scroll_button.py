import sys

from functools import partial

from PyQt4 import QtGui,QtCore


def move_scrollbar(vs, value):
    vs.blockSignals(True)
    vs.setValue(value)
    vs.blockSignals(False)

def window():
    app = QtGui.QApplication(sys.argv)
    win = QtGui.QWidget()
    main_horizontal = QtGui.QHBoxLayout()
    verti_1 = QtGui.QVBoxLayout()
    verti_2 = QtGui.QVBoxLayout()
    list1 = QtGui.QListWidget()
    for i in range(20):
        list1.addItem(str(i))

    list2 = QtGui.QListWidget()
    for i in range(20):
        list2.addItem("name" + str(i))

    verti_1.addWidget(list1)
    verti_2.addWidget(list2)

    vs1 = list1.verticalScrollBar()
    vs2 = list2.verticalScrollBar()

    vs1.valueChanged.connect(partial(move_scrollbar, vs2))
    vs2.valueChanged.connect(partial(move_scrollbar, vs1))

    main_horizontal.addLayout(verti_1)
    main_horizontal.addLayout(verti_2)
    win.setLayout(main_horizontal)
    win.resize(400,200)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    window()
