# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGraphicsView, QLabel,
    QLineEdit, QListView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(885, 708)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.scanButton = QPushButton(self.centralwidget)
        self.scanButton.setObjectName(u"scanButton")
        self.scanButton.setGeometry(QRect(450, 10, 89, 25))
        self.scanDeviceButton = QPushButton(self.centralwidget)
        self.scanDeviceButton.setObjectName(u"scanDeviceButton")
        self.scanDeviceButton.setGeometry(QRect(450, 50, 89, 25))
        self.scrapeButton = QPushButton(self.centralwidget)
        self.scrapeButton.setObjectName(u"scrapeButton")
        self.scrapeButton.setGeometry(QRect(540, 10, 89, 25))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 91, 17))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 91, 17))
        self.friendlyNameTextField = QLineEdit(self.centralwidget)
        self.friendlyNameTextField.setObjectName(u"friendlyNameTextField")
        self.friendlyNameTextField.setGeometry(QRect(120, 50, 321, 25))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(20, 110, 491, 531))
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(530, 110, 341, 241))
        self.romsPathTextField = QComboBox(self.centralwidget)
        self.romsPathTextField.setObjectName(u"romsPathTextField")
        self.romsPathTextField.setGeometry(QRect(120, 10, 321, 25))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 885, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RetroMan", None))
        self.scanButton.setText(QCoreApplication.translate("MainWindow", u"Scan library", None))
        self.scanDeviceButton.setText(QCoreApplication.translate("MainWindow", u"Scan device", None))
        self.scrapeButton.setText(QCoreApplication.translate("MainWindow", u"Scrape", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Library path", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Device name", None))
    # retranslateUi

