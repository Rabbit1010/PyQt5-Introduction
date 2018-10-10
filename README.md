# PyQt5-Introduction
An introduction on how to use PyQt5 to create GUI application in Python

# Installation
Use whatever works
```
pip3 install pyqt5
pip install pyqt5
pip install PtQt5
```

# Qt Designer
Use Qt Designer (not Qt Creator) to drag-and-drop UI elements.
Qt Designer will save your file in .ui format.
Use the following command in cmd to make a .py class file
```
pyuic5 FILENAME.ui -o FILENAME.py
```

# In Python
In the .py class there would be a class like this
```python
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 250, 121, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
```
