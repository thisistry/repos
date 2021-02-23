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


sudo ssh-keygen -f "/root/.ssh/known_hosts" -R 10.10.6.16

  cb = QtGui.QApplication.clipboard()
    cb.clear(mode=cb.Clipboard )
    cb.setText("Clipboard Text", mode=cb.Clipboard)
