import psycopg2

class postconn():
    def __init__(self,host,database,user,password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conection = psycopg2.connect( host='localhost',database='employee',user='postgres',password ='Neosoft$22')


    def createCursor(self):
        self.curs= self.conection.cursor
        return self.curs

    def createTable(self,qu):


