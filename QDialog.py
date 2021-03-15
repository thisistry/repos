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
    
    
    
    import multiprocessing
proc = multiprocessing.Process(target=your_proc_function, args=())
proc.start()
# Terminate the process
proc.terminate()  # sends a SIGTER

[(t['id'], t['name']) for t in transitions]

# Resolve the issue and assign it to 'pm_user' in one step
jira.transition_issue(issue, '5', assignee={'name': 'pm_user'}, resolution={'id': '3'})

# The above line is equivalent to:
jira.transition_issue(issue, '5', fields={'assignee':{'name': 'pm_user'}, 'resolution':{'id': '3'}})



curl -u <EMAIL-ADDRESS>:<API-TOKEN> -X GET "https://<NAME>.atlassian.net/rest/api/3/issue/<ISSUE_KEY>/transitions"
    
    
    curl -D- -u <EMAIL-ADDRESS>:<API-TOKEN> --data '{"transition": {"id": "21"}}' -H 'Accept: application/json' -H 'Content-Type: application/json' -X POST "https://<NAME>.atlassian.net/rest/api/3/issue/<ISSUE_KEY>/transitions"
