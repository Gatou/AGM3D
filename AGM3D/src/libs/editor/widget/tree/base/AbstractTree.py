
from libs.editor.GuiLibs import *
from libs.editor.widget.menu.Menu import Menu
from libs.editor.mgr.MenuManager import MenuManager


class AbstractTree(QTreeWidget):
    
    def __init__(self, parent=None):
        QTreeWidget.__init__(self, parent)
        #---
        self.header().setResizeMode(QHeaderView.ResizeToContents)
        self.setUniformRowHeights(True)
        self.header().setVisible(False)
        self.header().setStretchLastSection(False)
        #---
        self.create_connection()
        
    def create_connection(self):
        self.connect(self, SIGNAL("itemExpanded (QTreeWidgetItem *)"), self.onItem_expanded)
        self.connect(self, SIGNAL("itemExpanded (QTreeWidgetItem *)"), self.onItem_collapsed)
        
    def resizeEvent(self, *args, **kwargs):
        self.header().setMinimumSectionSize(self.viewport().width())
        return QTreeWidget.resizeEvent(self, *args, **kwargs)
    
    def onContextMenu(self, pos):
        MenuManager.context_menu(self, "").popup(QCursor.pos())
    
    def onItem_expanded(self, item):
        pass
    
    def onItem_collapsed(self, item):
        pass
    
    def enable_context_menu(self): 
        #self.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self, SIGNAL("customContextMenuRequested(const QPoint &)"), self.onContextMenu)
        
    