
from libs.editor.widget.menu.AbstractContextMenuAction import AbstractContextMenuAction
from libs.editor.mgr.DockManager import DockManager
from libs.editor.mgr.IconManager import IconManager
from os.path import isdir


class CreateFolderAction(AbstractContextMenuAction):
    
    def __init__(self):
        icon = IconManager.application_icon("folder.png")
        text = "Folder"
        widget = DockManager.DOCKS["AssetsDock"].ui.tree
        AbstractContextMenuAction.__init__(self, icon, text, widget)
        #---
        self.path = "Create"
        self.position = (0, 0)
        #---
        
    def is_enabled(self):
        item = self.widget.currentItem()
        return isdir(item.absolute_path())
        
    def action_performed(self):
        command = self.widget.commands["create folder"]
        command.execute()
        
        
class CreateFileAction(AbstractContextMenuAction):
    
    def __init__(self):
        icon = None
        text = "Python Script"
        widget = DockManager.DOCKS["AssetsDock"].ui.tree
        AbstractContextMenuAction.__init__(self, icon, text, widget)
        #---
        self.path = "Create"
        self.position = (100, 0)
        #---
        
    def is_enabled(self):
        item = self.widget.currentItem()
        return isdir(item.absolute_path())
        
    def action_performed(self):
        command = self.widget.commands["create file"]
        command.execute("newPythonScript", "py")