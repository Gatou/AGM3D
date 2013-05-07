
import os
from libs.editor.GuiLibs import *
from libs.editor.mgr.MenuManager import MenuManager
from libs.editor.mgr.DockManager import DockManager
from libs.editor.ui.base.AbstractDock import OpenDockAction
from libs.editor.ui.assetsdock.AssetsDock import AssetsDock

class EditorManager:

    @staticmethod
    def create():
        EditorManager.search_editor_packages(os.getcwd(), "DOCK")
        DockManager.create()
        #---
        EditorManager.search_editor_packages(os.getcwd(), "ACTION")
        EditorManager.import_docks_actions()
        MenuManager.create()
        #---
        
    @staticmethod  
    def search_editor_packages(path, type):
        it = QDirIterator(path, "", QDir.AllDirs|QDir.NoDotAndDotDot|QDir.NoSymLinks)
        while True:
            subpath = it.filePath()
            if subpath != "":
                if type == "DOCK" and type in it.fileName().upper():
                    DockManager.import_docks(subpath)
                elif type == "ACTION" and type in it.fileName().upper():
                    MenuManager.import_actions(subpath)
                EditorManager.search_editor_packages(subpath, type)
            #---
            if it.hasNext():
                it.next()
            else:
                break
            
    @staticmethod
    def import_docks_actions():
        for dock in DockManager.DOCKS.values():
            action = OpenDockAction(dock)
            try:
                MenuManager.ACTIONS["Window"]
            except:
                MenuManager.ACTIONS["Window"] = []
            MenuManager.ACTIONS["Window"].append(action)
        