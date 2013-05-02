

from PySide.QtCore import *
from PySide.QtGui import *

class MenuAction(QAction):
    
    def __init__(self, text, slot=None, icon=QIcon(), shortcut=None):
        
        self.widget = QObject()
        
        if icon == None:
            icon = QIcon()
        QAction.__init__(self, icon, text, self.widget)
        """
        if slot != None:
            self.triggered.connect(slot)
        self.setShortcut(shortcut)
        self.__conditions = []
        """
        
    def reset_conditions(self):
        self.__conditions = []
        
    def add_condition(self, method):
        self.__conditions.append(method)
        
    def check_conditions(self):
        for method in self.__conditions:
            method()