import csv

class files():


    def __init__(self,filename,delimiter = ','):
        self.filename = filename
        self.delimiter = delimiter
        self.openFile()

    def openFile(self):
       self.f =  open('{}'.format(self.filename),'r')
       self.csv_reader = csv.reader(self.f,delimiter = self.delimiter)
       self.header=next(self.csv_reader)
       self.v =[]
       for line in self.csv_reader:
           self.v.append(line)
       print(self.v)
       return self.v

    def header(self):
        for i in self.header:
            print(i)
        print(self.header)
        return self.header

    def createHeader(self,header):
        self.header = header
        self.f.write(self.header)

    def parsefile(self):

        return self.v

    def closefile(self):
        return self.f.close()

    '''
    import csv
import Con_posql

class files():


    def __init__(self,filename,delimiter = ',',encoding = 'utf-8'):
        self.filename = filename
        self.delimiter = delimiter
        self.encoding = encoding
        self.openFile()

    def openFile(self):
        
       self.f =  open('{}'.format(self.filename),'r')  
       self.csv_reader = csv.reader(self.f,delimiter = self.delimiter)
       self.header=next(self.csv_reader)
       self.v =[]
       for line in self.csv_reader:
           self.v.append(line)
       #print(self.v)
       return self.v
       
    def finalFile(self):
        return self.header,self.v
        

    def parsefile(self):
        
        return self.v

    def getHeader(self):
        return self.header

    def closefile(self):
        return self.f.close()

    def createHeader(self,header):
        self.header = header
        self.f.write(self.header)

    def openWrite(self,filename,method):
        self.filename = filename
        self.method = method
        self.f=open(self.filename,method)

    def showfile(self):
        s = []
        for line in self.v:
            s.append(line)
        print(s)

    def writeTableToFile(self):
    '''
