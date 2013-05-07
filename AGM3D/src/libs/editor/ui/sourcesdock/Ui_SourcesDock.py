# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SourcesDock.ui'
#
# Created: Tue May 07 21:28:26 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_SourcesDock(object):
    def setupUi(self, SourcesDock):
        SourcesDock.setObjectName("SourcesDock")
        SourcesDock.resize(400, 300)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.horizontalLayout = QtGui.QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tree = FileTree(self.dockWidgetContents)
        self.tree.setObjectName("tree")
        self.tree.headerItem().setText(0, "1")
        self.horizontalLayout.addWidget(self.tree)
        SourcesDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(SourcesDock)
        QtCore.QMetaObject.connectSlotsByName(SourcesDock)

    def retranslateUi(self, SourcesDock):
        SourcesDock.setWindowTitle(QtGui.QApplication.translate("SourcesDock", "DockWidget", None, QtGui.QApplication.UnicodeUTF8))

from libs.editor.widget.tree.filetree.FileTree import FileTree
