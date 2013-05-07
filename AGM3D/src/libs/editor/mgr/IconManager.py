
from os.path import join
from libs.editor.GuiLibs import *


class IconManager():
    
    @staticmethod
    def application_icon_path():
        return "resources/icons/"
    
    @staticmethod
    def application_icon(filename):
        complete_filename = join(IconManager.application_icon_path(), filename)
        return QIcon(complete_filename)