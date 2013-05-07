cd C:\Users\gaetan\Desktop\AGM3D\AGM3D\src\libs\editor\ui
set PATH=%PATH%;C:\Python27\Scripts
set PATH=%PATH%;C:\Python27\Lib\site-packages\PySide

(

cd C:\Users\gaetan\Documents\GitHub\AGM3D\AGM3D\src\libs\editor\ui\mainwindow
pyside-uic MainWindow.ui -o Ui_MainWindow.py

cd C:\Users\gaetan\Documents\GitHub\AGM3D\AGM3D\src\libs\editor\ui\projectwindow
pyside-uic ProjectWindow.ui -o Ui_ProjectWindow.py

cd C:\Users\gaetan\Documents\GitHub\AGM3D\AGM3D\src\libs\editor\ui\assetsdock
pyside-uic AssetsDock.ui -o Ui_AssetsDock.py

cd C:\Users\gaetan\Documents\GitHub\AGM3D\AGM3D\src\libs\editor\ui\sourcesdock
pyside-uic SourcesDock.ui -o Ui_SourcesDock.py
)
