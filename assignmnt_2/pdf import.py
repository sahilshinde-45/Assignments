import conn_mysql
import conn_psql
import pdfgenerator
import fileclass
import psycopg2


object = conn_mysql.Mysql('localhost','employee','root','Neosoft$22')
post_object = conn_psql.poconn('localhost','student','postgres','Neosoft$22')

pdf_object = pdfgenerator.PDF()
file_obj = fileclass.files("Employees.csv")
#head = file_obj.header()

#POSTGRES
'''
post_object.createCursor()
post_object.fetchtable('student_data')
#post_object.retrive()
result_data=post_object.fetchData('student_data')
l = pdf_object.withIndex(head, result_data)

post_object.endConn()
pdf_object.output_table(l)
my_pdf = pdfgenerator.PDF('P','mm','letter')
pdf_object.save_pdf('student.pdf')
'''
#MySql
object.createCursor
object.fetchtable('emp_data')
#result_data=post_object.fetchData('student_data')
#l = pdf_object.withIndex(head, result_data)

result_data = object.fetchData('emp_data')
#l = pdf_object.withIndex(head, res)
object.endConn()
pdf_object.output_table(result_data)
my_pdf = pdfgenerator.PDF('P','mm','letter')
pdf_object.save_pdf('employee.pdf')

