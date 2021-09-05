import mysql.connector
import fileclass
import csv


class Mysql():
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.mydb = mysql.connector.connect(host='localhost', user='root', password='Neosoft$22',
                                            database=self.database)


    def createCursor(self):
        self.cursor = self.mydb.cursor()
        return self.cursor

    # def run(self,querry):
    #    return self.cursor.execute(querry)
    def createTable(self, query):
        return self.cursor.execute(query)

    def fetchData(self, table_name):
        self.table_name = table_name
        self.cursor.execute("SELECT * from {}".format(self.table_name))
        # print(table_name)
        return (self.cursor.fetchall())

    def fetchtable(self, table_name):
        self.table_name = table_name
        return table_name

    def pushTable(self, pT):
        for row in pT:
            self.cursor.execute("insert into {} values {}".format(self.table_name, tuple(row)))

    def endConn(self):
        self.mydb.commit()
        self.cursor.close()
        self.mydb.close()
