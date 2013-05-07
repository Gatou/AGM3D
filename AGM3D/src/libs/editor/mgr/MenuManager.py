
from libs.editor.GuiLibs import *
from os.path import splitext
from imp import load_source
from inspect import getmembers, isclass
from libs.editor.ui.mainwindow.MainWindow import MainWindow

class MenuManager:
       
    #MENU_BAR = []     
    ACTIONS = {}
    MENUS = {}
    CONTEXT_MENUS = {}
    CONTEXT_ACTIONS = {}
    
    @staticmethod
    def create():
        MenuManager.create_menubar()
        MenuManager.populate_menubar()
        MenuManager.populate_toolbar()
        MenuManager.check_all_actions_enabled()
        #---
        MenuManager.create_context_menus()
        

    
    @staticmethod
    def import_actions(path):
        it = QDirIterator(path, "", QDir.Files|QDir.NoDotAndDotDot|QDir.NoSymLinks)
        while True:
            filename = it.fileName()
            if filename != "":
                if(splitext(filename)[1] == ".py"):
                    module = load_source(splitext(filename)[0], it.filePath())
                    #---
                    for name, obj in getmembers(module, isclass):
                        if len(obj.__bases__) > 0:
                            if obj.__bases__[0] == AbstractContextMenuAction:
                                if "ABSTRACT" in name.upper(): continue
                                action = obj()
                                try:
                                    MenuManager.CONTEXT_ACTIONS[action.widget]
                                except:
                                    MenuManager.CONTEXT_ACTIONS[action.widget] = {}
                                try:
                                    MenuManager.CONTEXT_ACTIONS[action.widget][action.path]
                                except:
                                    MenuManager.CONTEXT_ACTIONS[action.widget][action.path] = []
                                MenuManager.CONTEXT_ACTIONS[action.widget][action.path].append(action)
                                
                            elif obj.__bases__[0] == AbstractMenuAction:
                                if "ABSTRACT" in name.upper(): continue
                                action = obj()
                                try:
                                    MenuManager.ACTIONS[action.path]
                                except:
                                    MenuManager.ACTIONS[action.path] = []
                                MenuManager.ACTIONS[action.path].append(action)
                                
            #---
            if it.hasNext():
                it.next()
            else:
                break
        
    @staticmethod
    def add_menu(name, priority):
        MenuManager.MENU_BAR.append((name, priority))
        #menubar = MainWindow.instance().ui.menubar
        
    @staticmethod
    def menu(path):
        #names = name.split("/")
        #for name in names:
        try:
            MenuManager.MENUS[path]
        except:
            MenuManager.MENUS[path] = Menu()
        #name = names[-1]
        #print MenuManager.MENUS
        return MenuManager.MENUS[path]
        
    @staticmethod
    def create_menubar():
        menubar = MainWindow.instance().ui.menubar
        menubar_items = []
        for path, actions in MenuManager.ACTIONS.items():
            if path == "":
                for action in actions:
                    menubar_items.append((action.text(), action.position[1]))
        #---
        for action_desc in sorted(menubar_items, key=lambda (name, priority): priority):
            menu = Menu(action_desc[0])
            menubar.addMenu(menu)
            MenuManager.MENUS[action_desc[0]] = menu
            
    @staticmethod
    def populate_menubar():
        menus = {}
        for path, actions in MenuManager.ACTIONS.items():
            try:
                menus[path]
            except:
                menus[path] = {}
            categories = {}
            menus[path] = categories
            for action in actions:
                try:
                    categories[action.position[0]]
                except:
                    categories[action.position[0]] = []
                categories[action.position[0]].append((action.position[1], action))
        #---
        for path, categories in menus.items():
            menu = MenuManager.menu(path)
            sorted_categories = categories.keys()
            sorted_categories.sort()
            for category in sorted_categories:
                menu.addSeparator()
                for action in sorted(categories[category], key=lambda (priority, action): priority):
                    act = action[1]
                    menu.addAction(act)
                    if act.is_menu:
                        act.setMenu(MenuManager.menu(act.path + act.text()))
         
    @staticmethod       
    def populate_toolbar():
        toolbar = MainWindow.instance().ui.toolBar
        #---
        categories = {}
        for path, actions in MenuManager.ACTIONS.items():
            for action in actions:
                if action.toolbar_position:
                    category, priority = action.toolbar_position
                    try:
                        categories[category]
                    except:
                        categories[category] = []
                    categories[category].append((priority, action))
        #---
        sorted_categories = categories.keys()
        sorted_categories.sort()
        for category in sorted_categories:
            if len(toolbar.actions()) != 0:
                toolbar.addSeparator()
            for action in sorted(categories[category], key=lambda (priority, action): priority):
                toolbar.addAction(action[1])
                
    @staticmethod
    def check_all_actions_enabled():
        for actions in MenuManager.ACTIONS.values():
            for action in actions:
                action.check_enabled()
        
    @staticmethod
    def context_menu(widget, path):
        try:
            MenuManager.CONTEXT_MENUS[widget]
        except:
            MenuManager.CONTEXT_MENUS[widget] = {}
        try:
            MenuManager.CONTEXT_MENUS[widget][path]
        except:
            MenuManager.CONTEXT_MENUS[widget][path] = Menu()
                
        #name = names[-1]
        #print MenuManager.MENUS
        return MenuManager.CONTEXT_MENUS[widget][path]
            
    @staticmethod
    def create_context_menus():
        for widget in MenuManager.CONTEXT_ACTIONS.keys():
            widget.enable_context_menu()
            #---
            menus = {}
            for path, actions in MenuManager.CONTEXT_ACTIONS[widget].items():
                try:
                    menus[path]
                except:
                    menus[path] = {}
                categories = {}
                menus[path] = categories
                for action in actions:
                    try:
                        categories[action.position[0]]
                    except:
                        categories[action.position[0]] = []
                    categories[action.position[0]].append((action.position[1], action))
            #---
            for path, categories in menus.items():
                menu = MenuManager.context_menu(widget, path)
                sorted_categories = categories.keys()
                sorted_categories.sort()
                for category in sorted_categories:
                    menu.addSeparator()
                    for action in sorted(categories[category], key=lambda (priority, action): priority):
                        act = action[1]
                        menu.addAction(act)
                        if act.is_menu:
                            act.setMenu(MenuManager.context_menu(widget, act.path + act.text()))
                        #widget.addAction(act)
                
from libs.editor.widget.menu.Menu import Menu
from libs.editor.widget.menu.AbstractMenuAction import AbstractMenuAction
from libs.editor.widget.menu.AbstractContextMenuAction import AbstractContextMenuAction