
from libs.editor.GuiLibs import *
from libs.editor.ui.mainwindow.Ui_MainWindow import Ui_MainWindow

class MainWindow(QMainWindow):

    __instance = None
    
    @staticmethod
    def instance():
        if not MainWindow.__instance:
            MainWindow.__instance = MainWindow()
        return MainWindow.__instance
     
    def __init__(self):
        QMainWindow.__init__(self)
        self.setup_ui()
        
    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.centralWidget().hide()
        
