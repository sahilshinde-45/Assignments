import conn_pg
import parse
import conn_Mysql

pg_obj = conn_pg.conn_pg('localhost', 'Book_store', 'root', 'Neosft$22')
sql_obj = conn_Mysql.conn_Mysql('localhost', 'book_store', 'root', 'Neosoft$22')

fileobj = parse.Parse('author.csv')

# postgress
'''
cur = pg_obj.createCursor()
pg_obj.fetchtable('book')
fetched_table = pg_obj.fetchData()
fileobj.writefile('books.csv', 'w')
csv_writer = fileobj.writeTableToCsv()
csv_writer.writerow([col[0] for col in cur.description])
for row in fetched_table:
    csv_writer.writerow(row)
fileobj.closefile()
'''

# sql
value1= fileobj.value
header= fileobj.header
cur = sql_obj.createCursor()
sql_obj.getTable('author')
fetched_table = sql_obj.pushData('author',value1)
fileobj.writefile('author.csv', 'w')
csv_writer = fileobj.writeTableToCsv()
csv_writer.writerow([col[0] for col in cur.description])
for row in fetched_table:
    csv_writer.writerow(row)
sql_obj.closeConn()

print('REcords created successfully')



