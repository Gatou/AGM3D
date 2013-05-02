
from libs.editor.GuiLibs import *
from libs.editor.widget.menu.MenuAction import MenuAction


class Action1(MenuAction):
    
    def __init__(self):
        MenuAction.__init__(self, "Jean robert")
        #self.text = name
        
class Action2(MenuAction):
    
    def __init__(self):
        MenuAction.__init__(self, "Trop baleze")
        #self.text = name