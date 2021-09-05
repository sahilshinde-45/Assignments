import fileclass
import csv
import con_psql
import psycopg2
import mysql_conn

post_object = con_psql.poconn('localhost','student','postgres','Neosoft$22')
file_object = fileclass.files('laptop.csv',',')
object = mysql_conn.Mysql('localhost','employee','root','Neosoft$22')


#POSTGRES CODE
cursor = post_object.createCursor()
value1 = file_object.parsefile()
ct = 'create table Laptop_data (sr varchar(100), Description varchar(200),Processor varchar(100),RAM varchar(100),OperatingSystem varchar(100),Storage varchar(100),Display varchar(100),Warranty varchar(100),Price varchar(100))'
post_object.createTable(ct)
post_object.fetchtable('Laptop_data')
post_object.pushTable(value1)
file_object.closefile()
post_object.endConn()
print('REcords created successfully')

#mysql

# MYSQL CODE
cursor=object.createCursor()
value=file_object.parsefile()
ct = 'create table Laptop_data (sr varchar(100), Description varchar(200),Processor varchar(100),RAM varchar(100),OperatingSystem varchar(100),Storage varchar(100),Display varchar(100),Warranty varchar(100),Price varchar(100))'
object.createTable(ct)
object.fetchtable('Laptop_data')
object.pushTable(value)
file_object.closefile()
object.endConn()
print ("Records created successfully")

