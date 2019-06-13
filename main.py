#!/usr/bin/env python

from PyQt4 import QtGui # Import the PyQt4 module we'll need
from PyQt4 import QtCore
import sys # We need sys so that we can pass argv to QApplication
import os
import re
import MainDialog

class MainDialogWindow(QtGui.QDialog, MainDialog.Ui_Dialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        # self.buttonBox.rejected.connect(self.close)
        # self.textResults.setText( QtCore.QString(text) )
        # self.textResults.setReadOnly(True)

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainDialogWindow()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function