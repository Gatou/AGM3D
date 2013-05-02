
from libs.editor.GuiLibs import *
from Ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow):
    
    def __init__(self):
        #__builtin__.MAIN_WINDOW = self
        QMainWindow.__init__(self)
        self.setup_ui()
        
    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centralWidget().hide()
        
