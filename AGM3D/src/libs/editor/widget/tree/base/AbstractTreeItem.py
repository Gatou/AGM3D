
from libs.editor.GuiLibs import *


class AbstractTreeItem(QTreeWidgetItem):
    
    def all_children(self):
        result = []
        self.__all_children_rec(self, result)
        return result
    
    def __all_children_rec(self, parent_item, result):
        for i in range(0, parent_item.childCount()):
            item = parent_item.child(i)
            result.append(item)
            self.__all_children_rec(item, result)
            
"""
class PropTreeItem(TreeItemBase):
    
    def __init__(self, *args, **kwargs):
        TreeItemBase.__init__(self, *args, **kwargs)
        self.__props = {}
        
    def set_property(self, key, value):
        self.__props[key] = value
        
    def property(self, key):
        return self.__props[key]
"""