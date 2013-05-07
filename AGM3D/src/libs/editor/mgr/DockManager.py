
from libs.editor.GuiLibs import *
from os.path import splitext
from imp import load_source
from inspect import getmembers, isclass
from libs.editor.GuiLibs import *


class DockManager:
    
    DOCKS = {}
    
    
    @staticmethod
    def create():
        DockManager.create_docks()
        
    
    @staticmethod
    def import_docks(path):
        it = QDirIterator(path, "", QDir.Files|QDir.NoDotAndDotDot|QDir.NoSymLinks)
        while True:
            filename = it.fileName()
            if filename != "":
                if(splitext(filename)[1] == ".py"):
                    module = load_source(splitext(filename)[0], it.filePath())
                    #---
                    for name, obj in getmembers(module, isclass):
                        if len(obj.__bases__) > 0 and obj.__bases__[0] == AbstractDock:
                            dock = obj()
                            DockManager.DOCKS[dock.__class__.__name__] = dock
            #---
            if it.hasNext():
                it.next()
            else:
                break
            
    @staticmethod
    def create_docks():
        for dock in DockManager.DOCKS.values():
            MainWindow.instance().addDockWidget(Qt.LeftDockWidgetArea, dock)
        
    @staticmethod
    def refresh_all_docks():
        for dock in DockManager.DOCKS.values():
            dock.refresh() 
            
from libs.editor.ui.base.AbstractDock import AbstractDock
from libs.editor.ui.mainwindow.MainWindow import MainWindow