

class ApplicationManager:

    @staticmethod
    def name():
        return "Agm3D"
    
    @staticmethod
    def version():
        return "0.1"
    
    @staticmethod
    def name_version():
        return ApplicationManager.name() + " v" + ApplicationManager.version()

    @staticmethod
    def extension(ext):
        if ext == "project file":
            return "agmproj"
        elif ext == "settings":
            return "agmset"