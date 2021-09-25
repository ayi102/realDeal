import os

class Utilities():

    @classmethod
    def get_absolute_path(self, relativePath):
        currentPath = os.path.dirname(os.path.abspath(__file__))
        absPath     = os.path.join(currentPath, relativePath)

        return absPath