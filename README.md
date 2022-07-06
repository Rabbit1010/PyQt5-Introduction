# PyQt5-Introduction
Qt is a C++ framework for creating native-looking GUI application in desktop or mobile or any other platform. PyQt5 is a Python wrapper for Qt.

This is an simple introduction on how to create GUI application in Python.

## PyQt5 Installation
Use pip installation, (use one of the which it works)
```
pip install PyQt5
pip3 install PyQt5
```
Or use Anaconda Installation
```
conda install -c anaconda pyqt
```

## Download Qt
Download Qt [here](https://www.qt.io/download), choosng the open source version is enough.

## Qt Designer
Use Qt Designer (not Qt Creator) to drag-and-drop design UI elements.
Qt Designer will save your file in .ui format.
Use the following command in conda or windows commnad line to make a .py class file
```
pyuic5 FILENAME.ui -o FILENAME.py
```

## Python GUI class
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

## Starting the GUI object
To run the GUI class, you can use the following code
```python
import sys, os

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

## Connect function call to a button
To connect function button when a button onClick
```python
def retranslateUi(self, MainWindow):
    self.pushButton.clicked.connect(lambda: self.Quick_Demo("test_String"))

def Quick_Demo(self, str):
    print("Quick Demo %s"%(str))
```

# Pyinstaller

You may want to build your Python script to an executable so that people can run it directly without setting up the environments.

## Pyinstaller installation and usage

To install
```bash
pip install pyinstaller
```

To run pyinstaller
```
pyinstaller <YOUR_SCRIPY>.py
```

## Useful options
```--noconsole```
The executable would not open up the Python console

```--onefile``` (default is ```--onedir```)
Instead of spanning all the libraries in a folder (and the .exe can only be executed in that folder), create a one-file bundled executable.
