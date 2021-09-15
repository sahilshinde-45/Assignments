import Parse

import conn_pg
import psycopg2
import conn_Mysql


#postgress----------------------------------

posobj = conn_pg.conn_pg('localhost', 'employee', 'postgres', 'Neosoft$22')
fileParseObj = Parse.Parse('laptop.csv')
cursor = posobj.createCursor()
value1=fileParseObj.value
header=fileParseObj.header

ct = 'create table Laptop(sr varchar(100), Description varchar(200),Processor varchar(100),RAM varchar(100),OperatingSystem varchar(100),Storage varchar(100),Display varchar(100),Warranty varchar(100),Price varchar(100))'

cursor=posobj.createTable(ct)
posobj.getTable('Laptop')
posobj.pushData(value1,'Laptop')

posobj.closeConn()

print('REcords created successfully')



#MYSQL______________________________


mysqlObj = conn_Mysql.conn_Mysql('localhost','employee','root','Neosoft$22')
fileParseObj = Parse.Parse('laptop.csv')
cursor = mysqlObj.createCursor()
value1 = fileParseObj.value
header= fileParseObj.header

ct = 'create table Laptop(sr varchar(100), Description varchar(200),Processor varchar(100),RAM varchar(100),OperatingSystem varchar(100),Storage varchar(100),Display varchar(100),Warranty varchar(100),Price varchar(100))'

cursor=mysqlObj.createTable(ct)
mysqlObj.getTable('Laptop')
mysqlObj.pushData(value1,'Laptop')

mysqlObj.closeConn()

print('REcords created successfully')

