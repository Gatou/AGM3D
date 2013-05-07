
import os
from os.path import join, normpath, basename, exists


class ProjectManager:
    
    __PROJECT_PATH = None
    __ASSETS_PATH = None
    __SOURCES_PATH = None
    __SETTINGS_PATH = None
    __ASSETS_FOLDERS = ["Scripts", "Animations", "Sounds", "Characters", "Tiles", "System", "Pictures"]

    @staticmethod
    def project_path():
        return ProjectManager.__PROJECT_PATH
    
    @staticmethod
    def assets_path():
        return ProjectManager.__ASSETS_PATH
    
    @staticmethod
    def sources_path():
        return ProjectManager.__SOURCES_PATH
    
    @staticmethod
    def settings_path():
        return ProjectManager.__SETTINGS_PATH
    
    @staticmethod
    def create_new_project(path):
        path = normpath(path)
        #Create usefull path (project, assets, etc...)
        ProjectManager.__create_paths(path);
        #Create project folders
        os.makedirs(ProjectManager.project_path())
        #Create assets folders
        os.makedirs(ProjectManager.assets_path())
        for folder_name in ProjectManager.__ASSETS_FOLDERS:
            os.makedirs(join(ProjectManager.assets_path(), folder_name))
        #Create sources folders
        os.makedirs(ProjectManager.sources_path())
        #Create project settings folder
        os.makedirs(ProjectManager.settings_path())
        #create .proj file
        file = open(join(ProjectManager.project_path(), "." + ApplicationManager.extension("project file")), "w")
        file.write(ApplicationManager.name_version())
        file.close()
        #---
        ProjectManager.open_project(ProjectManager.project_path());
    
    @staticmethod
    def open_project(path):
        path = normpath(path)
        #---
        ProjectManager.close_project()
        if not exists(path): 
            print "lol"
            return
        #---
        ProjectManager.__create_paths(path)
        #ProjectManager.check_project_valid()
        
        if ProjectManager.is_project_opened():
            ProjectManager.__project_opening()
            
            """
            DataMgr.init();
            loadSettings();
            WidgetMgr.MAIN_WINDOW.refresh();
            WidgetMgr.MAIN_WINDOW.setVisible(true);
            
            """
        #SaveMgr.clear();
        
    @staticmethod
    def __project_opening():
        MainWindow.instance().setWindowTitle(basename(ProjectManager.project_path()) + " - " + ApplicationManager.name_version())
        MenuManager.check_all_actions_enabled()
        DockManager.refresh_all_docks()
        
    @staticmethod
    def close_project():
        if ProjectManager.is_project_opened():
            MainWindow.instance().setWindowTitle(ApplicationManager.name_version())
            #saveSettings();
        
        #WidgetMgr.MAIN_WINDOW.setProjectStateEnabled(false);
        ProjectManager.__PROJECT_PATH = None
        ProjectManager.__SOURCES_PATH = None
        ProjectManager.__ASSETS_PATH = None
        ProjectManager.__SETTINGS_PATH = None
        MenuManager.check_all_actions_enabled()
    
    @staticmethod
    def __create_paths(project_path):
        ProjectManager.__PROJECT_PATH = normpath(project_path)
        ProjectManager.__ASSETS_PATH = join(ProjectManager.project_path(), "Assets")
        ProjectManager.__SETTINGS_PATH = join(ProjectManager.project_path(), "ProjectSettings")
        ProjectManager.__SOURCES_PATH = join(ProjectManager.project_path(), "Sources")
        
    @staticmethod
    def is_project_opened():
        return ProjectManager.project_path() != None
       
        
from libs.editor.mgr.ApplicationManager import ApplicationManager
from libs.editor.ui.mainwindow.MainWindow import MainWindow
from libs.editor.mgr.MenuManager import MenuManager
from libs.editor.mgr.DockManager import DockManager
