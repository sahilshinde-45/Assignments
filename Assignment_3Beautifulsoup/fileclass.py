import csv


class files:

    def __init__(self, filename, delimiter=','):
        self.filename = filename
        self.delimiter = delimiter
        self.openFile()

    def openFile(self):
        self.f = open('{}'.format(self.filename), 'r')
        self.csv_reader = csv.reader(self.f, delimiter=self.delimiter)
        self.header = next(self.csv_reader)

    def header(self):
        heading = self.header
        return heading

    def parsefile(self):
        return self.csv_reader

    def closefile(self):
        return self.f.close()
