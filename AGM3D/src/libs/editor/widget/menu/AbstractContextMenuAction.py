

from libs.editor.widget.menu.AbstractMenuAction import AbstractMenuAction


class AbstractContextMenuAction(AbstractMenuAction):
    
    def __init__(self, icon, text, widget, shortcut=None):
        AbstractMenuAction.__init__(self, icon, text, shortcut)
        #---
        self.widget = widget
        