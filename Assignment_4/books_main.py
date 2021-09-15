
import books
import conn_Mysql
import conn_postgress
import psycopg2

mysql_object = conn_Mysql.Mysql('localhost', 'book_store', 'root', 'Neosoft$22')
post_object = conn_postgress.poconn('localhost','Book_store','postgres','Neosoft$22')
post_object = conn_postgress.poconn('localhost','Book_store','postgres','Neosoft$22')

#psql

cur = post_object.createCursor()

post_object.createTable(books.person)

post_object.createTable(books.books_1)
post_object.createTable(books.authors)
post_object.createTable(books.genre)
post_object.createTable(books.user_book)
post_object.createTable(books.book_genre)

post_object.fetchtable('person')
post_object.pushTable(books.insert_user)
post_object.fetchtable('book')
post_object.pushTable(books.insert_books_1)
post_object.fetchtable('author')
post_object.pushTable(books.insert_authors)
post_object.fetchtable('genre')
post_object.pushTable(books.insert_genre)
post_object.fetchtable('user_book')
post_object.pushTable(books.insert_usrbook)
post_object.fetchtable('book_genre')
post_object.pushTable(books.insert_book_genre)



cur.execute('select person.first_name,user_book.usrbook_id from person inner join user_book on person.user_id = user_book.user_id')
record = cur.fetchall()
for row in record:
    print(row)
post_object.endConn()
print("records inserted successfully")




#mysql
cur = mysql_object.createCursor()

#mysql_object.createTable(books.person)

#mysql_object.createTable(books.books_1)
#mysql_object.createTable(books.authors)
#mysql_object.createTable(books.genre)
#mysql_object.createTable(books.user_book)
#mysql_object.createTable(books.book_genre)

mysql_object.fetchtable('person')
mysql_object.pushTable(books.insert_user)
mysql_object.fetchtable('book')
mysql_object.pushTable(books.insert_books_1)
mysql_object.fetchtable('author')
mysql_object.pushTable(books.insert_authors)
mysql_object.fetchtable('genre')
mysql_object.pushTable(books.insert_genre)
mysql_object.fetchtable('user_book')
mysql_object.pushTable(books.insert_usrbook)
mysql_object.fetchtable('book_genre')
mysql_object.pushTable(books.insert_book_genre)



cur.execute('select person.first_name,user_book.usrbook_id from person inner join user_book on person.user_id = user_book.user_id')
record = cur.fetchall()
for row in record:
    print(row)
mysql_object.endConn()
print("records inserted successfully")


