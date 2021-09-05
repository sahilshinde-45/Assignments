import fileClass
import csv
import Con_psql

post_object = Con_psql.poconn('localhost', 'student', 'postgres', 'Neosoft$22')
file_object = fileClass.files('Student.csv', '|')

# POSTGRES CODE
cursor = post_object.createCursor()
value1 = file_object.parsefile()
ct = 'create table student_data (Student_ID varchar(100),First_name varchar(100),location varchar(100))'
post_object.createTable(ct)
post_object.fetchtable('student_data')
post_object.pushTable(value1)
file_object.closefile()
post_object.endConn()
print('REcords created successfully')
