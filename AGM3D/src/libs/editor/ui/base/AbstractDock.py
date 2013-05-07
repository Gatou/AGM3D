
from libs.editor.GuiLibs import *
from libs.editor.widget.menu.AbstractMenuAction import AbstractMenuAction
#from agml.modules import DockMgr, IconMgr


class AbstractDock(QDockWidget):
    
    def __init__(self):
        #self.used = True
        QDockWidget.__init__(self)
        #self.title_frame = DockTitleFrame()
        self.setup_ui()
        """
        #self.topLevelChanged.connect(self.onFloating_changed)
        #---
        #self.setTitleBarWidget(self.title_frame)
        #self.setWidget(self.ui.frame_body)
        #self.title_frame.closeButton.setIcon(IconMgr.icon("close.png"))
        #self.title_frame.maximizeButton.setIcon(IconMgr.icon("maximize.png"))
        #self.title_frame.closeButton.clicked.connect(self.close)
        #self.title_frame.maximizeButton.clicked.connect(lambda: self.setFloating(True))
        #---
        #self.ui.frame_body.setStyleSheet("QFrame#frame_body{\
    border-width: 1px;\
    border-style: solid;\
    border-color: rgb(100, 100, 100);\
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0,\
    y2:1, stop:0 rgb(170, 170, 255), stop:1 rgb(160, 160, 255));\
    }")

    def onFloating_changed(self):
        if self.isFloating():
            self.setTitleBarWidget(self.title_frame)
        else:
            self.setTitleBarWidget(self.title_frame)
    """
    def setup_ui(self):
        pass
    
    def refresh(self):
        pass
    """
    def save_settings(self, settings):
        settings.setValue("No data", 0)
    
    def id(self):
        return int(self.objectName()[len("Dock"):])
        
    def showEvent(self, *args, **kwargs):
        return QDockWidget.showEvent(self, *args, **kwargs)
    
    def closeEvent(self, *args, **kwargs):
        #self.deleteLater()
        DockMgr.remove_dock(self)
        return QDockWidget.closeEvent(self, *args, **kwargs)
    
    def setWindowTitle(self, text):
        self.title_frame.label.setText(text)
        return QDockWidget.setWindowTitle(self, text)
    """
"""
class DockTitleFrame(QFrame):
    
    def __init__(self, parent=None):
        QFrame.__init__(self, parent)
        self.setObjectName("frame_title")
        #---
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.setObjectName("frame_title")
        self.horizontalLayout = QHBoxLayout(self)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setContentsMargins(6, 2, 2, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QLabel(self)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.maximizeButton = QPushButton(self)
        self.maximizeButton.setMinimumSize(QSize(18, 18))
        self.maximizeButton.setMaximumSize(QSize(18, 18))
        self.maximizeButton.setText("")
        self.maximizeButton.setObjectName("maximizeButton")
        self.horizontalLayout.addWidget(self.maximizeButton)
        self.closeButton = QPushButton(self)
        self.closeButton.setMinimumSize(QSize(18, 18))
        self.closeButton.setMaximumSize(QSize(18, 18))
        self.closeButton.setText("")
        self.closeButton.setIconSize(QSize(16, 16))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.setStyleSheet("QFrame#frame_title{\
    border-width: 1px;\
    border-bottom-width: 0px;\
    border-style: solid;\
    border-color: rgb(100, 100, 100);\
    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0,\
    y2:1, stop:0 rgb(123, 123, 125), stop:1 rgb(43, 43, 125));\
    }")
"""
        
"""
    def draw_body(element, option, painter, widget):
        r = option.rect
        rect = QRect(r.x(), r.y(), r.width()-1, r.height()-1)
        gradient = QLinearGradient(0, 0, 0, option.rect.height())
        gradient.setColorAt(0, QColor(170, 170, 255))
        gradient.setColorAt(1, QColor(160, 160, 255))
        brush = QBrush(gradient)
        painter.setBrush(brush)
        pen = QPen(QColor(100, 100, 100))
        painter.setPen(pen)
        painter.drawRect(rect)
        
    @staticmethod
    def draw_title(element, option, painter, widget):
        r = option.rect
        rect = QRect(r.x(), r.y(), r.width()-1, r.height())
        gradient = QLinearGradient(0, 0, 0, option.rect.height())
        gradient.setColorAt(0, QColor(123, 123, 125))
        gradient.setColorAt(1, QColor(43, 43, 125))
        brush = QBrush(gradient)
        painter.setBrush(brush)
        pen = QPen(QColor(100, 100, 100))
        painter.setPen(pen)
        painter.drawRect(rect)
"""

class OpenDockAction(AbstractMenuAction):
    
    def __init__(self, dock):
        icon = None
        text = dock.windowTitle()
        AbstractMenuAction.__init__(self, icon, text)
        #self.setToolTip("Close the active project.")
        #self.setStatusTip("Close the active project.")
        #---
        self.path = "Window"
        self.category = 0
        self.priority = 0
        self.dock = dock
        
    def action_performed(self):
        self.dock.setVisible(True)
        
        
        