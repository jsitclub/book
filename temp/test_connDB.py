import MySQLdb

conn= MySQLdb.connect(
    user='root',
    passwd='',
    host='localhost',
    db='test',
    charset='utf8',
)

#create database test_book;
#use test_book;
#create table Book_Main(code varchar(20),title varchar(50),author varchar(30),isbn varchar(13));
#insert into Book_Main(code,title,author,isbn) values('1','aa','νΈνΈ','rr');

cur=conn.cursor()
#cur.execute('insert into Book_Main(code,title,author,isbn) values(1,"μ₯κ³ ","aaa","123456789012")')
cur.execute('insert into test_table(a) values("h하나둘h")')
conn.commit()

# cur.execute('select * from Book_Main')
# for row in cur.fetchall():
#    print(row) 
