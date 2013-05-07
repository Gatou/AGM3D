
import os
from os.path import join, split, normpath
from libs.editor.mgr.ProjectManager import ProjectManager
from libs.editor.GuiLibs import QLineEdit, Qt

class RenameCommand():
    
    def __init__(self, tree):
        self.tree = tree
        
    def execute(self):
        item = self.tree.currentItem()
        self.rename_lineEdit = RenameLineEdit(self)
        self.rename_lineEdit.setMaximumHeight(16)
        self.rename_lineEdit.editingFinished.connect(self.end_edit_item)
        self.rename_lineEdit.setText(item.text(0))
        self.tree.setItemWidget(item, 0, self.rename_lineEdit)
        self.rename_lineEdit.selectAll()
        self.rename_lineEdit.setFocus()
        
    def end_edit_item(self, edit_canceled=False):
        self.rename_lineEdit.editingFinished.disconnect(self.end_edit_item)
        item = self.tree.currentItem()
        self.tree.setItemWidget(item, 0, None)
        #---
        if edit_canceled:
            return
        text = self.rename_lineEdit.text()
        item.setText(0, text)
        self.rename()
            
        
    def rename(self):
        item = self.tree.currentItem()
        path = split(item.path)[0]
        from_name = item.filename_prefix()
        to_name = str(item.text(0))
        if from_name == to_name:
            return
        #---
        old_path = normpath(join(path, from_name) + item.extension())
        new_path = normpath(join(path, to_name) + item.extension())
        absolute_old_path = normpath(join(self.tree.absolute_path(), old_path))
        absolute_new_path = normpath(join(self.tree.absolute_path(), new_path))
        #---
        if not self.tree.absolute_path() in absolute_new_path:
            return
        print "(DEBUG: RenameCommand): renaming item"
        print absolute_old_path, absolute_new_path
        #---
        try:
            os.rename(absolute_old_path, absolute_new_path)
            item.path = new_path
            #---
            for item in item.all_children():
                item.path = item.path.replace(old_path, new_path, 1)
            #---
            self.tree.memorize_expanded_items()
        except:
            raise "ERROR (RenameCommand): Rename incorrect (" + absolute_old_path + ") to (" + absolute_new_path +")"
            item.setText(0, from_name)
            
        
class RenameLineEdit(QLineEdit):
    
    def __init__(self, command):
        QLineEdit.__init__(self)
        self.command = command
        
    def keyPressEvent (self, event):
        if event.key() == Qt.Key_Escape:
            self.command.end_edit_item(True)
        else:
            QLineEdit.keyPressEvent(self, event)
            
        