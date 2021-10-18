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
            self._parseItem(line)
        elif type == "Equation":
            self._parseEquation(line)

    def _parseHeader(self, line):
        self.contents.append("## " + line)
        self.contents.append('|Category| Value ($)| Type Percentage (%) | Total Percentage (%)|')
        self.contents.append('|--|--|--|--|')

    def _parseItem(self, itemLine):
        mdString = '|'
        itemList = itemLine.split(',')
        for item in itemList:
            mdString = mdString + item + '|'
        self.contents.append(mdString)

    def _parseType(self,type):
        self.contents.append('|**' + type + '**| | | |')

    def _parseEquation(self, line):
        self.contents.append("## " + line)
        self.contents.append('|Variable| Value |')
        self.contents.append('|--|--|')

    def generateMd(self):
        try:
            os.remove(self.fileName)
        except:
            pass

        fd = open(self.fileName, 'w+')

        fd.write('# ' + self.title + '\n')
        for line in self.contents:
            fd.write(line + "\n")

        fd.close()