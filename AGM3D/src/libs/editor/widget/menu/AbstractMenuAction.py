

from libs.editor.GuiLibs import *


class AbstractMenuAction(QAction):
    
    def __init__(self, icon, text, shortcut=None):
        self.__object = QObject()
        
        if not icon:
            icon = QIcon()
            
        QAction.__init__(self, icon, text, self.__object)
        if shortcut != None:
            self.setShortcut(shortcut)
        #---
        self.path = ""
        self.position = (0, 0)
        self.is_menu = False
        self.toolbar_position = None
        #---
        self.triggered.connect(self.action_performed)
        
    def check_enabled(self):
        self.setEnabled(self.is_enabled())

    def is_enabled(self):
        return ProjectManager.is_project_opened()
    
    def action_performed(self):
        raise NotImplementedError, "You need to implement this method"

from libs.editor.mgr.ProjectManager import ProjectManager