
from libs.editor.ui.base.AbstractDialog import AbstractDialog
from libs.editor.ui.projectwindow.Ui_ProjectWindow import Ui_ProjectWindow
from os.path import exists, normpath, join
from libs.editor.GuiLibs import *
from libs.editor.mgr.ProjectManager import ProjectManager

class ProjectWindow(AbstractDialog):

    def __init__(self, parent=None):
        AbstractDialog.__init__(self, parent)
        self.__project_path = ""
        
    def setup_ui(self):
        self.ui = Ui_ProjectWindow()
        self.ui.setupUi(self)
        
    def setup_connection(self):
        self.ui.nameLineEdit.textChanged.connect(self.__onNameLineEdit_edited)
        self.ui.selectLocationButton.clicked.connect(self.__onLocationButton_clicked)
        
    def __onNameLineEdit_edited(self):
        if not self.refreshing:
            self.__check_ok_enabled()
            self.ui.locationLineEdit.setText(self.__complete_path())

    def __check_ok_enabled(self):
        if self.ui.nameLineEdit.text() == "":
            #warningLabel.setText(" "); !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        elif exists(self.__complete_path()):
            #warningLabel.setText("A folder with that name already exists."); !!!!!!!!!!!!!!!!!!!!
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(False)
        else:
            #warningLabel.setText(" "); !!!!!!!!!!!!!!
            self.ui.buttonBox.button(QDialogButtonBox.Ok).setEnabled(True)
    
    def __complete_path(self):
        return normpath(join(self.__project_path, str(self.ui.nameLineEdit.text())))
    
    def refresh(self):
        self.refreshing = True
        self.__project_path = self.__default_location()
        self.ui.nameLineEdit.setText("")
        self.ui.locationLineEdit.setText(self.__project_path)
        self.__check_ok_enabled()
        self.refreshing = False
        
    def __onLocationButton_clicked(self):
        path = QFileDialog.getExistingDirectory(self, "Open Directory",
                                                 self.__project_path,
                                                 QFileDialog.ShowDirsOnly
                                                 | QFileDialog.DontResolveSymlinks);
        if path != "":
            self.__project_path = str(path)
            self.ui.locationLineEdit.setText(self.__complete_path())
        self.__check_ok_enabled()
    
    def __default_location(self):
        return QDesktopServices.storageLocation(QDesktopServices.DocumentsLocation)
            
    def accept(self):
        ProjectManager.create_new_project(self.__complete_path())
        AbstractDialog.accept(self)
        
    #def reject(self):
    #    DialogWindow.reject(self)

