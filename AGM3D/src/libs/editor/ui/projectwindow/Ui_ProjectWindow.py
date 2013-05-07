# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProjectWindow.ui'
#
# Created: Tue May 07 21:28:25 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ProjectWindow(object):
    def setupUi(self, ProjectWindow):
        ProjectWindow.setObjectName("ProjectWindow")
        ProjectWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        ProjectWindow.resize(342, 139)
        ProjectWindow.setModal(True)
        self.verticalLayout = QtGui.QVBoxLayout(ProjectWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(ProjectWindow)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nameLineEdit = QtGui.QLineEdit(ProjectWindow)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.horizontalLayout.addWidget(self.nameLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtGui.QLabel(ProjectWindow)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.locationLineEdit = QtGui.QLineEdit(ProjectWindow)
        self.locationLineEdit.setReadOnly(True)
        self.locationLineEdit.setObjectName("locationLineEdit")
        self.horizontalLayout_2.addWidget(self.locationLineEdit)
        self.selectLocationButton = QtGui.QToolButton(ProjectWindow)
        self.selectLocationButton.setObjectName("selectLocationButton")
        self.horizontalLayout_2.addWidget(self.selectLocationButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.buttonBox = QtGui.QDialogButtonBox(ProjectWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ProjectWindow)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), ProjectWindow.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), ProjectWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(ProjectWindow)

    def retranslateUi(self, ProjectWindow):
        ProjectWindow.setWindowTitle(QtGui.QApplication.translate("ProjectWindow", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProjectWindow", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("ProjectWindow", "Project Location:", None, QtGui.QApplication.UnicodeUTF8))
        self.selectLocationButton.setText(QtGui.QApplication.translate("ProjectWindow", "...", None, QtGui.QApplication.UnicodeUTF8))

