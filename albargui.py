# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'albargui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_albargui(object):
    def setupUi(self, albargui):
        albargui.setObjectName("albargui")
        albargui.resize(836, 595)
        self.centralwidget = QtWidgets.QWidget(albargui)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 811, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/ADMIN/Downloads/7LP8.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(530, 450, 75, 23))
        self.pushButton.setStyleSheet("\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 450, 75, 23))
        self.pushButton_2.setStyleSheet("\n"
"background-color: rgb(0, 85, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        albargui.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(albargui)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 21))
        self.menubar.setObjectName("menubar")
        albargui.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(albargui)
        self.statusbar.setObjectName("statusbar")
        albargui.setStatusBar(self.statusbar)

        self.retranslateUi(albargui)
        QtCore.QMetaObject.connectSlotsByName(albargui)

    def retranslateUi(self, albargui):
        _translate = QtCore.QCoreApplication.translate
        albargui.setWindowTitle(_translate("albargui", "MainWindow"))
        self.pushButton.setText(_translate("albargui", "RUN"))
        self.pushButton_2.setText(_translate("albargui", "TERMINATE"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    albargui = QtWidgets.QMainWindow()
    ui = Ui_albargui()
    ui.setupUi(albargui)
    albargui.show()
    sys.exit(app.exec_())