
from os.path import exists, join, normpath
import os

class CreateFolderCommand():
    
    def __init__(self, tree):
        self.tree = tree
        
    def execute(self):
        item = self.tree.currentItem()
        if item:
            path = item.absolute_path()
        else:
            path = self.tree.absolute_path()
        #---
        folder_name = self.find_folder_name(path)
        complete_folder_path = normpath(join(path, folder_name))
        #---
        if not self.tree.absolute_path() in complete_folder_path:
            return
        if exists(complete_folder_path):
            return
        #---
        try:
            os.makedirs(complete_folder_path)
            if item:
                item.setExpanded(True)
            self.tree.refresh(item)
            new_item = self.tree.item_by_path(complete_folder_path)
            self.tree.setCurrentItem(new_item)
            self.tree.commands["rename"].execute()
        except:
            raise "ERROR (CreateFolderCommand): Error during folder creation"

            
    def find_folder_name(self, path):
        base_name = "New Folder"
        folder_name = base_name
        folder_path = join(path, folder_name)
        index = 0
        while exists(folder_path):
            index += 1
            folder_name = base_name + " " + str(index)
            folder_path = join(path, folder_name)
        #---
        return folder_name