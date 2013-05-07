
from libs.editor.widget.menu.AbstractMenuAction import AbstractMenuAction

class FileMenuAction(AbstractMenuAction):
    
    def __init__(self):
        icon = None
        text = "File"
        AbstractMenuAction.__init__(self, icon, text)
        #---
        self.path = ""
        self.position = (0, 0)
        
class EditMenuAction(AbstractMenuAction):
    
    def __init__(self):
        icon = None
        text = "Edit"
        AbstractMenuAction.__init__(self, icon, text)
        #---
        self.path = ""
        self.position = (0, 100)
        
class WindowMenuAction(AbstractMenuAction):
    
    def __init__(self):
        icon = None
        text = "Window"
        AbstractMenuAction.__init__(self, icon, text)
        #---
        self.path = ""
        self.position = (0, 500)