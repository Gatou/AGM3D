
from libs.editor.GuiLibs import *


class AbstractDialog(QDialog):
    
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.setup_ui()
        #self.setStyleSheet(AgmStyle.dialog_window())
        self.refreshing = False
        self.setup_connection()
        
    def setup_ui(self):
        pass
    
    def setup_connection(self):
        pass
    
    def accept(self):
        self.hide()
        
    def reject(self):
        self.hide()
        
    def refresh(self):
        pass
    
    def show(self):
        self.refresh()
        QDialog.show(self)
    
    def exec_(self):
        self.refresh()
        QDialog.exec_(self)
    