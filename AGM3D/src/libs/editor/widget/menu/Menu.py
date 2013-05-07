
from libs.editor.GuiLibs import *
from libs.editor.widget.menu.AbstractMenuAction import AbstractMenuAction     
        
        
class Menu(QMenu):
        
    def __init__(self, text=None):
        QMenu.__init__(self, text)

    def showEvent(self, *args, **kwargs):
        self.check_actions_enabled()
        return QMenu.showEvent(self, *args, **kwargs)
    
    #def popup(self, *args, **kwargs):
    #    print "lala"
    #    self.check_actions_enabled()
    #    return QMenu.popup(self, *args, **kwargs)
           
    def check_actions_enabled(self):
        for action in self.actions():
            if isinstance(action, AbstractMenuAction):
                action.check_enabled()