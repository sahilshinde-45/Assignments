import conn_postgress
import fileclass
import con_sql

pg_obj = conn_postgress.poconn('localhost', 'Book_store', 'root', 'Neosft$22')
sql_obj = con_sql.Mysql('localhost', 'book_store', 'root', 'Neosoft$22')

fileobj = fileclass.files('author.csv')

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
cur = sql_obj.createCursor()
sql_obj.fetchtable('author')
fetched_table = sql_obj.fetchData('author')
fileobj.writefile('author.csv', 'w')
csv_writer = fileobj.writeTableToCsv()
csv_writer.writerow([col[0] for col in cur.description])
for row in fetched_table:
    csv_writer.writerow(row)
fileobj.closefile()
