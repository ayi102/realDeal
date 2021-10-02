import os

class Report():

    def __init__(self, title, fileName):
        self.title    = title
        self.fileName = fileName
        self.contents = []

    def addContent(self, lines):
        lineToAdd = ""
        for line in lines:
            if line == "Header":
                lineToAdd = "# "
            elif line == "Type":
                lineToAdd = "## "
            elif line == "Item":
                lineToAdd = ""
            else:
                lineToAdd = lineToAdd + line
                self.contents.append(lineToAdd)
                lineToAdd = ""

    def generateMd(self):
        try:
            os.remove(self.fileName)
        except:
            pass

        fd = open(self.fileName, 'w+')

        for line in self.contents:
            fd.write(line + "\n\n")

        fd.close()