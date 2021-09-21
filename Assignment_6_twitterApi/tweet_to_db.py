import Parse
import Pdf
import main
import conn_pg
import psycopg2
import conn_Mysql
import main
import Twitter
import re
from Pdf import PDF
from decouple import config

post_object = conn_pg.conn_pg('localhost', 'employee', 'postgres', 'Neosoft$22')
pdf = Pdf.PDF("P","mm","letter")
fileParseObj = Parse.Parse('tweets.csv')


value=fileParseObj.value
header=fileParseObj.header

pdf.add_page()
pdf.alias_nb_pages()
pdf.maketable(header,value)
pdf.output("twitter.pdf",'F')

post_object.getTable('tweets')
post_object.pushData('tweets',value)
post_object.closeConn()

"""
head = parse_obj.fetchHeader()
post_object.createCursor()
post_object.getTable('tweets')
post_object.retrive()

retrieve_data = post_object.fetchData('tweets')
l = pdfObj.withIndex(head, retrieve_data)
post_object.closeConn()
pdfObj.output_table(l, 8)
pdfObj.save_pdf('twitter_3.pdf')
"""
