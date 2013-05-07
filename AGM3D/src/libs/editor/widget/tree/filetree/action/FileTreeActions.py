
from libs.editor.GuiLibs import QDesktopServices, QUrl, Qt, QShortcut
from libs.editor.widget.menu.AbstractContextMenuAction import AbstractContextMenuAction
from libs.editor.widget.tree.filetree.FileTree import FileTree
from libs.editor.ui.assetsdock.AssetsDock import AssetsDock
from libs.editor.mgr.DockManager import DockManager
from libs.editor.mgr.IconManager import IconManager
from os.path import normpath, split


class CreateMenuAction(AbstractContextMenuAction):
    
    def __init__(self):
        icon = IconManager.application_icon("new.png")
        text = "Create"
        widget = DockManager.DOCKS["AssetsDock"].ui.tree
        AbstractContextMenuAction.__init__(self, icon, text, widget)
        #---
        self.position = (0, 0)
        self.is_menu = True

class ShowInExplorerAction(AbstractContextMenuAction):
    
    def __init__(self):
        icon = IconManager.application_icon("explorer.png")
        text = "Show in Explorer"
        widget = DockManager.DOCKS["AssetsDock"].ui.tree
        AbstractContextMenuAction.__init__(self, icon, text, widget)
        #---
        self.position = (0, 100)
        
    def action_performed(self):
        path = normpath(self.widget.currentItem().absolute_path())
        path = split(path)[0]
        QDesktopServices.openUrl(QUrl("file:///" +path))
        
class RenameAction(AbstractContextMenuAction):
    
    
    def __init__(self):
        icon = None
        text = "Rename"
        widget = DockManager.DOCKS["AssetsDock"].ui.tree
        AbstractContextMenuAction.__init__(self, icon, text, widget)
        #---
        self.position = (200, 0)
        
    def action_performed(self):
        command = self.widget.commands["rename"]
        command.execute()
        
class RefreshAction(AbstractContextMenuAction):
    
    
    def __init__(self):
        icon = IconManager.application_icon("refresh.png")
        text = "Refresh"
        shortcut = "F5"
        widget = DockManager.DOCKS["AssetsDock"].ui.tree
        AbstractContextMenuAction.__init__(self, icon, text, widget, shortcut)
        self.setShortcutContext(Qt.ApplicationShortcut)
        #---
        #.shortcut = QShortcut("F5", self.widget, self.action_performed, Qt.WidgetShortcut)
        self.position = (300, 0)
        
    def action_performed(self):
        command = self.widget.commands["refresh"]
        command.execute()
