
from libs.editor.widget.menu.AbstractMenuAction import AbstractMenuAction
from libs.editor.mgr.IconManager import IconManager
from libs.editor.mgr.ProjectManager import ProjectManager
from libs.editor.mgr.ApplicationManager import ApplicationManager
from libs.editor.ui.projectwindow.ProjectWindow import ProjectWindow
from libs.editor.GuiLibs import QFileDialog
from libs.editor.ui.mainwindow.MainWindow import MainWindow
from os.path import dirname

class NewProjectAction(AbstractMenuAction):
    
    def __init__(self):
        icon = IconManager.application_icon("new.png")
        text = "New Project..."
        shortcut = "Ctrl+N"
        AbstractMenuAction.__init__(self, icon, text, shortcut)
        self.setToolTip("Create a new project.")
        self.setStatusTip("Create a new project.")
        #---
        self.path = "File"
        self.position = (0, 0)
        self.toolbar_position = (0, 0)
        
    def is_enabled(self):
        return True
    
    def action_performed(self):
        window = ProjectWindow()
        window.exec_()
        
class OpenProjectAction(AbstractMenuAction):
    
    def __init__(self):
        icon = IconManager.application_icon("open.png")
        text = "Open Project..."
        shortcut = "Ctrl+O"
        AbstractMenuAction.__init__(self, icon, text, shortcut)
        self.setToolTip("Open an existing project.")
        self.setStatusTip("Open an existing project.")
        #---
        self.path = "File"
        self.position = (0, 100)
        self.toolbar_position = (0, 100)
        
    def is_enabled(self):
        return True
    
    def action_performed(self):
        filter_text = ApplicationManager.name() + " (*." + ApplicationManager.extension("project file") + ")"
        path = QFileDialog.getOpenFileName(MainWindow.instance(), "Open Project", "", filter_text);
        path = str(path[0])
        if path != "":
            ProjectManager.open_project(dirname(path))
        
        
class CloseProjectAction(AbstractMenuAction):
    
    def __init__(self):
        icon = None
        text = "Close Project"
        AbstractMenuAction.__init__(self, icon, text)
        self.setToolTip("Close the active project.")
        self.setStatusTip("Close the active project.")
        #---
        self.path = "File"
        self.position = (0, 200)
        self.is_menu = False
        
    def action_performed(self):
        ProjectManager.close_project()

class SaveProjectAction(AbstractMenuAction):
    
    def __init__(self):
        icon = IconManager.application_icon("floppy.png")
        text = "Save Project"
        shortcut = "Ctrl+S"
        AbstractMenuAction.__init__(self, icon, text, shortcut)
        self.setToolTip("Save the active project.")
        self.setStatusTip("Save the active project.")
        #---
        self.path = "File"
        self.position = (0, 300)
        self.toolbar_position = (0, 200)
        
    def action_performed(self):
        pass