# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2

import sys, os
import numpy as np
import myBitmapClass as bmp
import scipy.ndimage as ndimage
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QImage

class Ui_MainWindow(object):       
    
    # Constructor, initialize the image array
    def __init__(self):
        self.image = np.zeros((512,512))
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 685)
        MainWindow.setMinimumSize(QtCore.QSize(800, 685))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 1000))
        MainWindow.setWhatsThis("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(540, 10, 241, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(540, 180, 241, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_2.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_2.addWidget(self.pushButton_6)
        self.pushButton_7 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_2.addWidget(self.pushButton_7)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(540, 360, 241, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_9 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_3.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_3.addWidget(self.pushButton_8)
        self.pushButton_10 = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_3.addWidget(self.pushButton_10)
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(540, 540, 241, 101))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.pushButton_12 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_4.addWidget(self.pushButton_12)
        self.pushButton_11 = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_4.addWidget(self.pushButton_11)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 512, 512))
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(320, 540, 181, 101))
        self.pushButton_13.setObjectName("pushButton_13")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing HW1"))
        self.pushButton.setText(_translate("MainWindow", "Read Lena.raw"))
        self.pushButton.clicked.connect(lambda: self.Read_Image("lena.raw"))
        self.pushButton_2.setText(_translate("MainWindow", "Read Baboon.raw"))
        self.pushButton_2.clicked.connect(lambda: self.Read_Image("BABOON.raw"))
        self.pushButton_3.setText(_translate("MainWindow", "Write image into .bmp file"))
        self.pushButton_3.clicked.connect(lambda: self.Write_Image())
        self.pushButton_4.setText(_translate("MainWindow", "Sobel Mask"))
        self.pushButton_4.clicked.connect(self.Sobel_Mask)
        self.pushButton_5.setText(_translate("MainWindow", "Laplacian Mask"))
        self.pushButton_5.clicked.connect(self.Laplacian_Mask)
        self.pushButton_6.setText(_translate("MainWindow", "Averaging Mask"))
        self.pushButton_6.clicked.connect(self.Averaging_Mask)
        self.pushButton_7.setText(_translate("MainWindow", "Gaussian Mask"))
        self.pushButton_7.clicked.connect(self.Gaussian_Mask)
        self.pushButton_9.setText(_translate("MainWindow", "Add Gaussian noise with σ= 1"))
        self.pushButton_9.clicked.connect(lambda: self.Read_Image("BABOON.raw"))
        self.pushButton_8.setText(_translate("MainWindow", "Add Gaussian noise with σ= 5"))
        self.pushButton_8.clicked.connect(lambda: self.Read_Image("BABOON.raw"))
        self.pushButton_10.setText(_translate("MainWindow", "Add Gaussian noise with σ= 10"))
        self.pushButton_10.clicked.connect(lambda: self.Read_Image("BABOON.raw"))
        self.pushButton_12.setText(_translate("MainWindow", "Smoothing Filter"))
        self.pushButton_12.clicked.connect(self.Smoothing_Filter)
        self.pushButton_11.setText(_translate("MainWindow", "Generate 100 Gaussian noise image \n"
" and average them"))
        self.pushButton_11.clicked.connect(self.Generate_100_Gaussian)
        self.pushButton_13.setText(_translate("MainWindow", "Quick Demo\n"
"Produce all images in ./out"))
        self.pushButton_13.clicked.connect(lambda: self.Quick_Demo())

    def Update_GUI_Image(self):
        # Tell the Qt GUI element to update the image
        self.label.setPixmap(QPixmap.fromImage(QImage(self.image, self.image.shape[0], self.image.shape[1], QImage.Format_Grayscale8) ));     
    
    def Quick_Demo(self):
        # Produce all the required images in just one click!
        print("Quick Demo, all the images output to ./out folder")
        
    ############################################################################
    # HW 1 Function starts here                                                #
    ############################################################################
    
    def Read_Image(self, file_name):
        print("Read image : %s"%(file_name))
        try:
            # Read the file as byte data (8-bit unsigned integer)
            self.image = np.fromfile(file_name, dtype=np.uint8)
            # Resize it into 512x512 array
            self.image = np.resize(self.image,(512,512))
            self.Update_GUI_Image()            
        except IOError as e:
            raise IOError("Could not read file , %s"%(e))
    
    def Write_Image(self):
        print("Attempt to write current image to .bmp file ......")
        # Check if file already exist
        for i in range (1,100):
            fname = "image_out%d.bmp"%(i)
            if os.path.isfile(fname)==False:
                break;
            if i>=99:
                raise IOError("Too many output files (max 100), delete \"image_out99.bmp\"")
        # Create Bitmap instance
        b = bmp.Bitmap(512,512)
        for i in range(0,512):
            for j in range (0,512):
                b.Set_Pixel_Gray(j,511-i,self.image[i,j])
        b.Write_File(fname)        
        print("Write image to \"%s\""%(fname))
    
    def Sobel_Mask(self, MainWindow):
        print("Apply Sobel mask to the image")
        sobel_vertical_filter = np.array([[-1, 0, 1],
                             [-2, 0, 2],
                             [-1, 0, 1]])
        vertical_image = ndimage.filters.correlate(self.image, sobel_vertical_filter, mode='constant')
        sobel_horizontal_filter = np.array([[-1, -2, -1],
                             [0, 0, 0],
                             [1, 2, 1]])
        horizontal_image = ndimage.filters.correlate(self.image, sobel_horizontal_filter, mode='constant')
        self.image = vertical_image + horizontal_image
        self.Update_GUI_Image()            
        
    def Laplacian_Mask(self, MainWindow):
        print("Apply Laplacian mask to the image")
        laplacian_filter = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]])
        self.image = ndimage.filters.correlate(self.image, laplacian_filter, mode='constant')
        self.Update_GUI_Image()            
        
    def Averaging_Mask(self, MainWindow):
        print("Apply Averaging mask to the image")
        averaging_filter = np.ones((12,12),dtype=int)
        # making the filter sum to 1
        averaging_filter = averaging_filter.astype(np.float) / np.sum(averaging_filter)
        self.image = ndimage.filters.correlate(self.image, averaging_filter, mode='constant')
        self.Update_GUI_Image()            
        
    def Gaussian_Mask(self, MainWindow):
        print("Apply Gaussian mask to the image")
        gaussian_filter = Gauss2D(shape=(12,12), sigma=5)
        self.image = ndimage.filters.correlate(self.image, gaussian_filter, mode='constant')
        self.Update_GUI_Image()            
        
    def Smoothing_Filter(self, MainWindow):
        print("Apply smoothing filter to the image")
        
    def Generate_100_Gaussian(self, MainWindow):
        print("Generate 100 Gaussian noise image and average them")

    ############################################################################
    # HW 1 Function ends here                                                  #
    ############################################################################

def Gauss2D(shape=(3, 3), sigma=0.5):
    # Return a 2D Gaussian Filter
    m, n = [(ss-1.)/2. for ss in shape]
    y, x = np.ogrid[-m:m+1,-n:n+1]
    h = np.exp(-(x*x + y*y) / (2.*sigma*sigma))
    h[ h < np.finfo(h.dtype).eps*h.max() ] = 0
    sumh = h.sum()
    if sumh != 0:
        h /= sumh
    return h

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