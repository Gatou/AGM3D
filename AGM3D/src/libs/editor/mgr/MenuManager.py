
from libs.editor.GuiLibs import *
import os
import os.path
import imp, inspect
from libs.editor.widget.menu.MenuAction import MenuAction
from libs.editor.mgr.EditorManager import EditorManager

class MenuManager:
            
    ACTIONS = []
    
    @staticmethod
    def init():
        
        MenuManager.create_menu_file()
        
    @staticmethod
    def create_menu_file():
        path = os.getcwd()
        MenuManager.search_actions(path)
      
    @staticmethod  
    def search_actions(path):
        #it = QDirIterator("", "", QDir.AllDirs|QDir.Files|QDir.NoDotAndDotDot|QDir.NoSymLinks)
        it = QDirIterator(path, "", QDir.AllDirs|QDir.NoDotAndDotDot|QDir.NoSymLinks)
        while True:
            subpath = it.filePath()
            if subpath != "":
                if it.fileName() == "action":
                    MenuManager.import_actions(subpath)
                MenuManager.search_actions(subpath)
            #---
            if it.hasNext():
                it.next()
            else:
                break
            
    @staticmethod
    def import_actions(path):
        it = QDirIterator(path, "", QDir.Files|QDir.NoDotAndDotDot|QDir.NoSymLinks)
        while True:
            filename = it.fileName()
            
            if filename != "":
                if(os.path.splitext(filename)[1] == ".py"):
                    module = imp.load_source(os.path.splitext(filename)[0], it.filePath())
                    for name, obj in inspect.getmembers(module):
                            if inspect.isclass(obj):
                                if obj.__bases__[0] == MenuAction:
                                    action = obj()
                                    EditorManager.MAIN_WINDOW.ui.menuFile.addAction(action)
                                    MenuManager.ACTIONS.append(action)
                                
            #---
            if it.hasNext():
                it.next()
            else:
                break
        