
from libs.editor.GuiLibs import *
import os, time
from libs.editor.ui.base.AbstractDock import AbstractDock
from libs.editor.ui.assetsdock.Ui_AssetsDock import Ui_AssetsDock

class AssetsDock(AbstractDock):
    
    def __init__(self):
        AbstractDock.__init__(self)
        #self.ui.tree.set_filter(self.ui.filterLineEdit)
        #self.ui.tree.expanded_items = expanded_items
        #t = time.time()
        #self.ui.tree.set_root_path(root_path) #"C:/Users/Public/Documents/Unity Projects/3-5_AngryBots/Assets"
        #---
        self.setWindowTitle("Assets")
    
    def setup_ui(self):
        self.ui = Ui_AssetsDock()
        self.ui.setupUi(self)
    
    def refresh(self):
        self.ui.tree.set_relative_root_path("Assets")
        #self.ui.tree.refresh()
        
    def save_settings(self, settings):
        pass
        #settings.setValue("root path", self.ui.tree.root_path)
        #self.ui.tree.memorize_expanded_items()
        #settings.setValue("expanded", self.ui.tree.expanded_items)
    """
    @staticmethod
    def create_and_load_settings(settings=None):
        if settings != None:
            dock = ProjectAssetsDock(settings.value("root path"), settings.value("expanded"))
        else:
            dock = ProjectAssetsDock()
        return dock
        
    """
    """
    def onCreateButton_clicked(self):
        #ProjectAssetsDock.ACTION_CREATE_FOLDER.triggered.connect(self.)
        ProjectAssetsDock.CREATE_MENU.execute(self, QCursor.pos())
        #ProjectAssetsDock.ACTION_CREATE_FOLDER.triggered.disconnect(self.onCreateFolderAction_clicked)
    """
        

