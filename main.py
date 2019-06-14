#!/usr/bin/env python

from PyQt4 import QtGui # Import the PyQt4 module we'll need
from PyQt4 import QtCore
import sys # We need sys so that we can pass argv to QApplication
import os
import re
import MainWindow  # This file holds our MainWindow and all design related things

"""
Notes:
patch of the PyInstaller/depend/bindepend.py https://github.com/Loran425/pyinstaller/commit/14b6e65642e4b07a4358bab278019a48dedf7460

Lib\site-packages\PyQt4\pyuic4 MainWindow.ui  -o MainWindow.py
Scripts\pyinstaller.exe --onefile --windowed --icon options.ico  --name "Options Fodler Pickler" "NRB Pickle Options FWW.spec" main.py

ToDo's
"""


class MainAppWindow(QtGui.QMainWindow, MainWindow.Ui_MainWindow):

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        
        self.actionCancel.setEnabled(False)
        self.btnCancel.hide()

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = MainAppWindow()                 # We set the form to be our Main App Wehdiw (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
                       # run the main function