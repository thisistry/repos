class MainForm(QDialog):

    def __init__(self, fn=None,parent=None):
        super(MainForm, self).__init__(parent,\
           flags=Qt.WindowMinimizeButtonHint|Qt.WindowMaximizeButtonHint)

        
        def closeEvent(self, evnt):
        if self._want_to_close:
            super(MyDialog, self).closeEvent(evnt)
        else:
            evnt.ignore()
            self.setWindowState(QtCore.Qt.WindowMinimized)
QObject::connect: Cannot queue arguments of type 'QTextCursor'
(Make sure 'QTextCursor' is registered using qRegisterMetaType().)




"./eclipse --launcher.suppressErrors -nosplash -data " + l1_Path + \
                " -application org.eclipse.cdt.managedbuilder.core.headlessbuild -import " + path_import + " -build Project/Debug" + " -Ea PATH=" + icc