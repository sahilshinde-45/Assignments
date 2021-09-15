import Parse
import conn_pg
import psycopg2
import conn_Mysql

# POSTGRES---USER.CSV
'''
posobj = conn_pg.postconn('localhost', 'employee', 'postgres', 'Neosoft$22')
fileParseObj = Parse.Parse('user.csv')
cursor = posobj.createCursor()
value1=fileParseObj.value
header=fileParseObj.header

ct = 'create table user_data (Username varchar(50),Identifier varchar(20),First_name varchar(50),last_name varchar(50))'
cursor=posobj.createTable(ct)
posobj.getTable('user_data')
posobj.pushData(value1,'user_data')

posobj.closeConn()

print('REcords created successfully')
  
  '''
    #  POSTGRESS -- EMP.CSV


posobj = conn_pg.postconn('localhost', 'office', 'postgres', 'Neosoft$22')
fileParseObj = Parse.Parse('emp.csv')
cursor = posobj.createCursor()
value1=fileParseObj.value
header=fileParseObj.header

ct = "create table EMPLOYEE_data (EMPLOYEE_ID varchar(10), FIRST_NAME varchar(50),LAST_NAME varchar(50),EMAIL varchar(50),PHONE_NUMBER varchar(20),JOB_ID varchar(25), SALARY varchar(20),DEPARTMENT_ID varchar(10))"

cursor=posobj.createTable(ct)
posobj.getTable('EMPLOYEE_data')
posobj.pushData(value1,'EMPLOYEE_data')

posobj.closeConn()

print('REcords created successfully')













""""
# mySQL -- user.csv

mysqlObj = conn_Mysql.conn_Mysql('localhost','employee','root','Neosoft$22')
fileParseObj = Parse.Parse('user.csv')
cursor = mysqlObj.createCursor()
value1 = fileParseObj.value
header= fileParseObj.header

ct = 'create table user_data (Username varchar(50),Identifier varchar(20),First_name varchar(50),last_name varchar(50))'
cursor=mysqlObj.createTable(ct)
mysqlObj.getTable('user_data')
mysqlObj.pushData(value1,'user_data')

mysqlObj.closeConn()

print('REcords created successfully')

"""

# Mysql -- emp.csv

mysqlObj = conn_Mysql.conn_Mysql('localhost','employee','root','Neosoft$22')
fileParseObj = Parse.Parse('emp.csv')
cursor = mysqlObj.createCursor()
value1 = fileParseObj.value
header= fileParseObj.header

ct =  "CREATE TABLE emp_Data(EMPLOYEE_ID varchar(10), FIRST_NAME varchar(50),LAST_NAME varchar(50),EMAIL varchar(50),PHONE_NUMBER varchar(20),JOB_ID varchar(25), SALARY varchar(20),DEPARTMENT_ID varchar(10))"

cursor=mysqlObj.createTable(ct)
mysqlObj.getTable('emp_Data')
mysqlObj.pushData(value1,'emp_Data')

mysqlObj.closeConn()

print('REcords created successfully')








'''
posobj.createCursor()
value1= fileParseObj.csv_reader()

posobj.createTable(ct)
posobj.getTable('user_data')
posobj.pushData(value1)
posobj.closeConn()
print("records created successfully")
'''

