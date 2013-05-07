
from os.path import exists, join, normpath
import os

class CreateFileCommand():
    
    def __init__(self, tree):
        self.tree = tree
        
    def execute(self, default_filename, extension):
        item = self.tree.currentItem()
        if item:
            path = item.absolute_path()
        else:
            path = self.tree.absolute_path()
        #---
        file_name = self.find_file_name(path, default_filename, extension)
        print file_name
        complete_file_path = normpath(join(path, file_name))
        #---
        if not self.tree.absolute_path() in complete_file_path:
            return
        if exists(complete_file_path):
            return
        #---
        try:
            open(complete_file_path, "w").close()
            if item:
                item.setExpanded(True)
            self.tree.refresh(item)
            new_item = self.tree.item_by_path(complete_file_path)
            self.tree.setCurrentItem(new_item)
            self.tree.commands["rename"].execute()
        except:
            raise "ERROR (CreateFileCommand): Error during file creation"

            
    def find_file_name(self, path, default_filename, extension):
        base_name = default_filename
        file_name = base_name + "." + extension
        file_path = join(path, file_name)
        index = 0
        print file_path
        while exists(file_path):
            index += 1
            file_name = base_name + str(index) + "." + extension
            file_path = join(path, file_name)
        #---
        return file_name