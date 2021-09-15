import books
import conn_Mysql
import conn_pg
import psycopg2

mysql_object = conn_Mysql.conn_Mysql('localhost', 'book_store', 'root', 'Neosoft$22')
post_object = conn_pg.conn_pg('localhost', 'Book_store', 'postgres', 'Neosoft$22')

# POSTGRES#-----------------------------------

cur = post_object.createCursor()

post_object.createTable(books.person)

post_object.createTable(books.books_1)
post_object.createTable(books.authors)
post_object.createTable(books.genre)
post_object.createTable(books.user_book)
post_object.createTable(books.book_genre)

post_object.getTable('person')
post_object.pushData(books.insert_user,'person')
post_object.getTable('book')
post_object.pushData(books.insert_books_1,'book')
post_object.getTable('author')
post_object.pushData(books.insert_authors,'author')
post_object.getTable('genre')
post_object.pushData(books.insert_genre,'genre')
post_object.getTable('user_book')
post_object.pushData(books.insert_usrbook,'user_book')
post_object.getTable('book_genre')
post_object.pushData(books.insert_book_genre,'book_genre')

cur.execute(
    'select person.first_name,user_book.usrbook_id from person inner join user_book on person.user_id = user_book.user_id')
record = cur.fetchall()
for row in record:
    print(row)
post_object.closeConn()
print("records inserted successfully")

'''
#mysql----------------------------------------------------------------------------------
cur = mysql_object.createCursor()

#mysql_object.createTable(books.person)
#mysql_object.createTable(books.books_1)
#mysql_object.createTable(books.authors)
#mysql_object.createTable(books.genre)
#mysql_object.createTable(books.user_book)
#mysql_object.createTable(books.book_genre)

mysql_object.getTable('person')
mysql_object.pushData(books.insert_user,'person')
mysql_object.getTable('book')
mysql_object.pushData(books.insert_books_1,'book')
mysql_object.getTable('author')
mysql_object.pushData(books.insert_authors,'author')
mysql_object.getTable('genre')
mysql_object.pushData(books.insert_genre,'genre')
mysql_object.getTable('user_book')
mysql_object.pushData(books.insert_usrbook,'user_book')
mysql_object.getTable('book_genre')
mysql_object.pushData(books.insert_book_genre,'book_genre')



cur.execute('select person.first_name,user_book.usrbook_id from person inner join user_book on person.user_id = user_book.user_id')
record = cur.fetchall()
for row in record:
    print(row)
mysql_object.closeConn()
print("records inserted successfully")

'''
