
from libs.editor.GuiLibs import *
from libs.editor.widget.tree.base.AbstractTreeItem import AbstractTreeItem
from libs.editor.mgr.ProjectManager import ProjectManager
from libs.editor.mgr.IconManager import IconManager
from os.path import relpath, splitext, basename, isdir, join


class FileTreeItem(AbstractTreeItem):
        
    def __init__(self, tree, path):
        AbstractTreeItem.__init__(self)
        #---
        #self.background_changing = False
        self.path = relpath(path, tree.absolute_path())
        self.setText(0, self.filename_prefix())
        #print os.path.abspath(self.path)
        #self.setIcon(0, IconMgr.icon_by_path(path))
        self.setFlags(Qt.ItemIsEditable|Qt.ItemIsEnabled|Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled)
        #self.setFlags(Qt.ItemIsEnabled|Qt.ItemIsSelectable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled)
        #---
        if isdir(path):
            self.setChildIndicatorPolicy(QTreeWidgetItem.ShowIndicator)
            self.setIcon(0, IconManager.application_icon("folder.png"))
        else:
            self.setIcon(0, IconManager.application_icon(splitext(path)[1][1:] + ".png"))
    
    def absolute_path(self):
        return join(self.treeWidget().absolute_path(), self.path)
    
    def filename(self):
        return basename(self.path)
    
    def filename_prefix(self):
        return splitext(self.filename())[0]
    
    def extension(self):
        return splitext(self.filename())[1]
    
    def set_highligthed(self, highligthed):
        self.background_changing = True
        if highligthed:
            brush = QBrush(QColor(50, 255, 50))
        else:
            brush = QBrush(QColor(255, 255, 255))
        self.setBackground(0, brush)
        self.background_changing = False
        
            
            
    
    