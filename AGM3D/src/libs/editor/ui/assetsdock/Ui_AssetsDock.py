# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AssetsDock.ui'
#
# Created: Tue May 07 21:28:26 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AssetsDock(object):
    def setupUi(self, AssetsDock):
        AssetsDock.setObjectName("AssetsDock")
        AssetsDock.resize(400, 300)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tree = FileTree(self.dockWidgetContents)
        self.tree.setObjectName("tree")
        self.tree.headerItem().setText(0, "1")
        self.horizontalLayout.addWidget(self.tree)
        AssetsDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(AssetsDock)
        QtCore.QMetaObject.connectSlotsByName(AssetsDock)

    def retranslateUi(self, AssetsDock):
        AssetsDock.setWindowTitle(QtGui.QApplication.translate("AssetsDock", "DockWidget", None, QtGui.QApplication.UnicodeUTF8))

from libs.editor.widget.tree.filetree.FileTree import FileTree
