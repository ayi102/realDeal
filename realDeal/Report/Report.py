
class Report():

    def __init__(self, title):
        self.title   = title
        self.contents = []

    def addLine(self, line):
        self.contents.append(line)

    def print(self):
        print(self.title)
        for line in self.contents:
            print(line)