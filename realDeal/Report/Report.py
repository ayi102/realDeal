import os

class Report():

    def __init__(self, title, fileName):
        self.title    = title
        self.fileName = fileName
        self.contents = []

    def addContent(self, type, line):
        if  type == "Header":
            self._parseHeader(line)
        elif type == "Type":
            self._parseType(line)
        elif type == "Item":
            self._parseItem

    def _parseHeader(self, line):
        self.contents.append("## " + line)

    def _parseType(self, line):
        self.contents.append("### " + line)

    def _parseItem(self, itemLine):
        itemLine.split(',')
        print(itemLine)

    def generateMd(self):
        try:
            os.remove(self.fileName)
        except:
            pass

        fd = open(self.fileName, 'w+')

        for line in self.contents:
            fd.write(line + "\n\n")

        fd.close()