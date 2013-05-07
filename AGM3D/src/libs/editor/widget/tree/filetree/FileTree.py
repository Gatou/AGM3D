

from libs.editor.GuiLibs import *
from libs.editor.widget.tree.base.AbstractTree import AbstractTree
from libs.editor.widget.tree.filetree.FileTreeItem import FileTreeItem
from os.path import join, isdir, relpath, split
from libs.editor.mgr.ProjectManager import ProjectManager
from libs.editor.widget.tree.filetree.command import *


class FileTree(AbstractTree):
    
    def __init__(self, parent=None):
        AbstractTree.__init__(self, parent)
        #---
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setProperty("showDropIndicator", False)
        self.setDragDropOverwriteMode(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)
        #---
        self.expanded_items = {}
        self.relative_root_path = None
        #self.filter_text = ""
        #self.header().setResizeMode(QHeaderView.ResizeToContents)
        self.drop_item_highligthed = None
        #---
        self.commands = {}
        self.commands["rename"] = RenameCommand.RenameCommand(self)
        self.commands["create folder"] = CreateFolderCommand.CreateFolderCommand(self)
        self.commands["refresh"] = RefreshCommand.RefreshCommand(self)
        self.commands["create file"] = CreateFileCommand.CreateFileCommand(self)
        
    def create_connection(self):
        AbstractTree.create_connection(self)
        #self.itemChanged.connect(self.onItem_changed)
        
    #def onContextMenu(self, point):
    #    TreeFile.MENU.set_sender(self)
    #    TreeFile.MENU.popup(QCursor.pos())
            
    def set_relative_root_path(self, relative_path):
        self.relative_root_path = relative_path
        self.refresh()
        
    def absolute_path(self):
        abolute_path = join(ProjectManager.project_path(), self.relative_root_path)
        #print split(abolute_path)[0]
        return split(abolute_path)[0]
    
    def relative_path(self, abolute_path):
        return relpath(abolute_path, self.absolute_path())
    
    def item_by_path(self, abolute_path):
        path = self.relative_path(abolute_path)
        it = QTreeWidgetItemIterator(self)
        while it.value():
            if it.value().path == path:
                return it.value()
            it.next()
          
    #def abs_path(self):
    #    return os.path.normpath(os.path.join(ProjectMgr.ASSETS_PATH, self.root_path))
        
    #def set_root_path(self, path):
    #    self.root_path = path#os.path.relpath(path, ProjectMgr.ASSETS_PATH)
    #    TreeFileCommands.refresh(self, None, False)
        
    def memorize_expanded_items(self):
        #if self.filtering(): return
        #---
        self.expanded_items.clear()
        it = QTreeWidgetItemIterator(self)
        while it.value():
            item = it.value()
            if item.isExpanded():
                self.expanded_items[item.path] = True
            it.next()
              
    #def filtering(self):
    #    return self.filter_text != ""
        
    #def set_filter(self, line_edit):
    #    self.connect(line_edit, SIGNAL("textChanged(QString)"), self.onFilter_TextChanged)
        
    def refresh(self, parent_item=None):
        if parent_item:
            parent_item.takeChildren()
            path = join(self.absolute_path(), parent_item.path)
            #print path
        else:
            #No item specified, so we want to refresh the entire tree.
            #We get the name of the root folder to add it first in the tree
            self.clear()
            path = self.absolute_path()
            root_folder = split(self.relative_root_path)[1]
        #---
        it = QDirIterator(path, "", QDir.AllDirs|QDir.Files|QDir.NoDotAndDotDot|QDir.NoSymLinks)
        while True:
            filename = it.fileName()
            if filename != "":
                #Add only folder root in all the folder of the root
                if not parent_item and filename != root_folder:
                    if it.hasNext():
                        it.next()
                        continue
                    else:
                        break
                #---
                path = it.filePath()
                item = FileTreeItem(self, path)
                #---
                if not parent_item:
                    self.addTopLevelItem(item)
                else:
                    parent_item.addChild(item)
                #---
                if isdir(item.absolute_path()):
                    try:
                        item.setExpanded(self.expanded_items[item.path])
                    except:
                        pass
            #---
            if it.hasNext():
                it.next()
            else:
                break
        
    #def refresh_root(self):
    #    #clear tree (The default clear method cause an error)
    #    for i in range(0, self.topLevelItemCount()):
    #        self.takeTopLevelItem(0)
    #    #---
    #    self.refresh_dir(self.abs_path(), None)

    #def generate_item(self, path):
    #    item = TreeFileItem()
    #    item.setup(self, path)
    #    #---
    #    return item
    
    def onItem_expanded(self, item):
        AbstractTree.onItem_expanded(self, item)
        #---
        if item.childCount() == 0:
            self.refresh(item)
        if item.childCount() == 0:
            item.setChildIndicatorPolicy(QTreeWidgetItem.DontShowIndicatorWhenChildless)
            
"""
    def dragMoveEvent(self, event):
        QTreeWidget.dragMoveEvent(self, event)
        if self.drop_item_highligthed is not None:
            self.drop_item_highligthed.set_highligthed(False)
            self.drop_item_highligthed = None
        #---
        if event.isAccepted():
            to_item = self.itemAt(self.mapFromGlobal(QCursor.pos()))
            if self.is_drop_enable(event.source(), event.source().selectedItems(), to_item):
                if to_item is not None:
                    if not to_item.isExpanded():
                        to_item.setExpanded(True)
                        to_item.setExpanded(False)
                    self.drop_item_highligthed = to_item
                    self.drop_item_highligthed.set_highligthed(True)
                event.accept()
            else:
                event.ignore()
        
    def dragEnterEvent(self, event):
        event.accept()
        return QTreeWidget.dragEnterEvent(self, event)
    
    def dragLeaveEvent(self, *args, **kwargs):
        if self.drop_item_highligthed is not None:
            self.drop_item_highligthed.set_highligthed(False)
            self.drop_item_highligthed = None
        return QTreeWidget.dragLeaveEvent(self, *args, **kwargs)
    
    def dropEvent(self, event):
        if self.drop_item_highligthed is not None:
            self.drop_item_highligthed.set_highligthed(False)
            self.drop_item_highligthed = None
        #---
        event.setDropAction(Qt.IgnoreAction)
        destination_item = self.itemAt(self.mapFromGlobal(QCursor.pos()))
        source_items = event.source().selectedItems()
        QTreeWidget.dropEvent(self, event)
        TreeFileCommands.move(self, source_items, destination_item)
    
    def is_drop_enable(self, source_tree, selected_items, destination_item):
        for item in selected_items:
            #--- Check if don't drop a parent if their children
            if destination_item is not None:
                if item.abs_path() in destination_item.abs_path():
                    return False
            #---
            occur = 0 #check if we don't have 2 dir we the same name in dragged items
            for item2 in selected_items:
                if item.filename() == item2.filename():
                    occur += 1
            if occur > 1:
                return False
        #---
        if destination_item is None: #The drop destination is the root
            for item in selected_items: #Check if a children doesn't have the same name than a dragged item
                for i in range(0, self.topLevelItemCount()):
                    child_item = self.topLevelItem(i)
                    if child_item is item:
                        return False
                    if child_item.filename() == item.filename():
                        return False
        else: #The drop destination is an item in the tree
            if not os.path.isdir(destination_item.abs_path()): #Check if the drop destination is not a file
                return False
            #---
            for item in selected_items: #Check if a children doesn't have the same name than a dragged item
                for i in range(0, destination_item.childCount()):
                    child_item = destination_item.child(i)
                    if child_item is item:
                        return False
                    if child_item.filename() == item.filename():
                        return False
        return True
        
    def onFilter_TextChanged(self, text):
        self.memorize_expanded_items()
        self.filter_text = text
        #---
        if not self.filtering():
            TreeFileCommands.refresh(self, None, False)
        else:
            #t = time.time()
            self.clear()
            it = QDirIterator(self.abs_path(), "", QDir.Dirs|QDir.Files|QDir.NoDotAndDotDot|QDir.NoSymLinks, QDirIterator.Subdirectories)
            index = 0
            while True:
                if self.filter_text != text:
                    return
                filename = it.fileName()
                path = it.filePath()
                if self.filter_text.lower() in filename.lower():
                    self.addTopLevelItem(self.generate_item(path))
                if it.hasNext():
                    it.next()
                else:
                    break
                index += 1
                if index % 50 == 0:
                    QApplication.processEvents()
            #print time.time() - t
    


    def onItem_changed(self, item, col):
        if item.background_changing: return
        TreeFileCommands.rename(os.path.split(item.path)[0], item.filename_prefix(), str(item.text(0)), item.extension(), self, item)
        
    def keyPressEvent(self, event):
        if not event.isAutoRepeat():
            if event.key() == Qt.Key_Delete:
                self.onDelete()
            elif event.key() == Qt.Key_F5: 
                self.onRefresh()
        return QTreeWidget.keyPressEvent(self, event)
    
    def mousePressEvent(self, *args, **kwargs):
        if self.itemAt(self.mapFromGlobal(QCursor.pos())) is None:
            self.setCurrentItem(None)
        return QTreeWidget.mousePressEvent(self, *args, **kwargs)
    
    def onDelete(self):
        reply = QMessageBox.question(self, AppMgr.NAME, "Delete selection ? (You cannot undo this action)", QMessageBox.Yes, QMessageBox.No)
        if reply == QMessageBox.Yes:
            TreeFileCommands.delete(self, self.selectedItems())
            
    def onRefresh(self):
        if len(self.selectedItems()) == 0:
            DockMgr.refresh_all_fileTree()
        else:
            for item in self.selectedItems():
                TreeFileCommands.refresh(self, item)
    
"""
    
