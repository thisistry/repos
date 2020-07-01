class MainForm(QDialog):

    def __init__(self, fn=None,parent=None):
        super(MainForm, self).__init__(parent,\
           flags=Qt.WindowMinimizeButtonHint|Qt.WindowMaximizeButtonHint)
