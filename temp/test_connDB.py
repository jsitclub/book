import MySQLdb

conn= MySQLdb.connect(
    user='root',
    passwd='',
    host='localhost',
    db='test_book',
)


cur=conn.cursor()
#cur.execute('insert into Book_Main(code,title,author,isbn) values(1,"장고","aaa","123456789012")')

cur.execute('select * from Book_Main')
for row in cur.fetchall():
   print(row) 
