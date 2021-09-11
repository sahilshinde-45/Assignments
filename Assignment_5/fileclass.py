import csv


class files:

    def __init__(self, filename, delimiter=','):
        self.filename = filename
        self.delimiter = delimiter
        #self.openFile()

    def openFile(self):
        self.f = open('{}'.format(self.filename), 'r')
        self.csv_reader = csv.reader(self.f, delimiter=self.delimiter)
        self.header = next(self.csv_reader)
        '''self.v =[]
        for line in self.csv_reader:
           self.v.append(line)'''

    def finalFile(self):
        return self.header,self.v

    def header(self):
        heading = self.header
        return heading

    def parsefile(self):
        return self.v

    def closefile(self):
        return self.f.close()

    def createHeader(self,header):
        self.header = header
        self.f.write(self.header)

    def writefile(self,filename,method):
        self.filename=filename
        self.method=method
        self.f=open(self.filename,method)

    def display(self):
        s=[]
        for line in self.v:
            s.append(line)
        print(s)

    def writeTableToCsv(self):
        self.write_csv =open('{}'.format(self.filename),'w',newline='')
        self.csv_writter = csv.writer(self.write_csv)
        return self.csv_writter
