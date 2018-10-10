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
To run the class, you can use the following code
```python
if __name__ == "__main__":
    # Safe start for Spyder IDE
    app = QtCore.QCoreApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    # Initialize and run Qt UI        
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Exiting UI
    if any('SPYDER' in name for name in os.environ):
        # Safe exit for Spyder IDE
        app.exec_()
    else:        
        sys.exit(app.exec_())
```
To connect function button when on click
```python
def retranslateUi(self, MainWindow):
    self.pushButton.clicked.connect(lambda: self.Quick_Demo("test_String"))

def Quick_Demo(self, str):
    print("Quick Demo %s"%(str))
```
