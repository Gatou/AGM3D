

import sys, os
from libs.editor.GuiLibs import *
from libs.editor.ui.mainwindow.MainWindow import MainWindow
from libs.editor.mgr.EditorManager import EditorManager

app = QApplication(sys.argv)

#ProjectManager.open_project("C:/Users/gaetan/Documents/lala")
#print MainWindow()
#print MainWindow()
#EditorManager.MAIN_WINDOW = MainWindow()

MainWindow.instance()
EditorManager.create()

MainWindow.instance().show()

from libs.editor.mgr.ProjectManager import ProjectManager
ProjectManager.open_project("C:\\Users\\gaetan\\Documents\\lala")

#MenuManager.add_menu("File/Import", 0, 0)



sys.exit(app.exec_())
