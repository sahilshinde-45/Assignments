import csv
from typing import List


class Parse:

    def __init__(self, filename):
        self.filename = filename
        self.csv_reader()
        self.write(self.header,self.value)



    def csv_reader(self):

        with open('emp.csv', 'r') as file:
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
        with open('emp.csv', 'w', newline="") as file:
            write = csv.writer(file)
            write.writerow(self.header)
            write.writerows(self.value)
            print("success records entered in database")




'''
file = open('user.csv')
type(file)
csvreader = csv.reader(file)

header = []
header = next(csvreader)
#print(header)

rows = []
for row in csvreader:
    rows.append(row)
#print(rows)

file.close()

'''
