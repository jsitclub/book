import MySQLdb

conn=MySQLdb.connect(
		user='root'
		,passwd='rootpswd'
		,host='localhost'
		,db='test_book'
		)
cur=conn.cursor()

cur.execute('drop table test;')

cur.execute('create table test(\
                code varchar(15) primary key\
                ,category varchar(50)\
                ,datetime datetime);')
                
cur.execute("insert into test(code,category) values('123','가나다');")
              
cur.execute('select * from test')
for row in cur.fetchall():
   print(row) 
