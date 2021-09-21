import csv
from typing import List


class Parse:


    def __init__(self, filename):

        self.filename = filename
        self.csv_reader()
        self.write(self.header,self.value)
        self.encoding = 'utf-8'


    def csv_reader(self):

        with open('tweets.csv', 'r') as file:
            csvreader = csv.reader(file, delimiter=',')
            self.header = next(csvreader)
            self.value=[]
            for row in csvreader:
                self.value.append(row)
                print(row)
            print("csv records read successfully ")

    def fetchHeader(self):
        return self.header

    def fetchValue(self):
        return self.value

    def parsefile(self):
        return self.csv_reader()

    def write(self, header, value):
        self.header = header
        self.value = value
        with open('tweets.csv', 'w', newline="") as file:
            write = csv.writer(file)
            write.writerow(self.header)
            write.writerows(self.value)
            print("success records entered in database")
