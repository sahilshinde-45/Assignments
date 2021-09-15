

import csv
from typing import List


class Parse:
    def __init__(self, filename):
        self.filename = filename
        self.csv_reader()
        self.write(self.header,self.value)



    def csv_reader(self):

        with open('laptop.csv', 'r') as file:
            csvreader = csv.reader(file, delimiter=',')
            self.header = next(csvreader)
            self.value=[]
            for row in csvreader:
                self.value.append(row)
            print("csv records read successfully ")

    def parsefile(self):
        return self.csv_reader()

    def write(self, header, value):
        self.header = header
        self.value = value
        with open('laptop.csv', 'w', newline="") as file:
            write = csv.writer(file)
            write.writerow(self.header)
            write.writerows(self.value)
            print("success records entered in database")





'''
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
    '''
