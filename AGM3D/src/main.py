

import sys, os
from libs.editor.GuiLibs import *
from libs.editor.mgr.EditorManager import EditorManager
from libs.editor.mgr.MenuManager import MenuManager
from libs.editor.ui.mainwindow.MainWindow import MainWindow

app = QApplication(sys.argv)

#ProjectMgr.open_project("C:/Users/gaetan/Documents/lala")
EditorManager.MAIN_WINDOW = MainWindow()
MenuManager.init()

EditorManager.MAIN_WINDOW.show()
sys.exit(app.exec_())
