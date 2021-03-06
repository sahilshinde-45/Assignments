import psycopg2


class conn_pg():
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = psycopg2.connect(host='localhost', database='employee', user='postgres',
                                           password='Neosoft$22')
        self.cur = 0

    def createCursor(self):
        self.cur = self.connection.cursor()
        return self.cur

    def createTable(self, query):
        return self.cur.execute(query)

    '''def fetchData(self,table_name):
        self.table_name = table_name
        return self.cur.execute("SELECT * from {}".format(self.table_name))
        return (self.cur.fetchall()) # returns a list of tuples.'''

    def getTable(self, table_name):
        self.table_name = table_name
        return table_name

    def pushData(self, pT, table_name):
        for row in pT:
            self.cur.execute("insert into {} values {}".format(table_name, tuple(row)))

    def closeConn(self):
        self.cur.close()
        self.connection.commit()
