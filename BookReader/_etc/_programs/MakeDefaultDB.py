##테이블을 모두 지우고 새로 만든다.

import MySQLdb

conn= MySQLdb.connect(
    user='root',
    passwd='',
    host='localhost',
    db='test_book',
    charset='utf8',
)

print("주의 !! 모든 데이터가 지워집니다.")
print("Warnning!! Drop all data!")
ans=input("계속 하겠습니까?('YES' or 'NO') : ")

if ans.upper()!='YES':
    exit()

cur=conn.cursor()

### CREATE DATABASE <dbname> CHARACTER SET utf8;

stmt = "SHOW TABLES LIKE 'Book_Main';"
cur.execute(stmt)
result = cur.fetchone()
if result:
    cur.execute('drop table Book_Main')
    
cur.execute('''create table Book_Main
                (code varchar(15) primary key
                ,title varchar(20)
                ,author varchar(20)
                ,translator varchar(20)
                ,isbn varchar(13)
                ,page int
                ,publisher varchar(20)
                ,publishdate datetime
                ,datetime datetime)
                 CHARACTER SET utf8 COLLATE utf8_general_ci;
            ''')
conn.commit()
print("Book_Main Table made.")

# stmt = "SHOW TABLES LIKE 'Category';"
# cur.execute(stmt)
# result = cur.fetchone()
# if result:
#     cur.execute('drop table Category')
    
# cur.execute('''create table Category 
#                 (code varchar(15) primary key
#                 ,category varchar(50)
#                 ,datetime datetime)
#                  CHARACTER SET utf8 COLLATE utf8_general_ci;
#             ''')

conn.commit()
print("Category Table made.")

stmt = "SHOW TABLES LIKE 'test';"
cur.execute(stmt)
result = cur.fetchone()
if result:
    cur.execute('drop table test')
    
cur.execute('''create table test
                (code varchar(15) primary key
                ,category varchar(50)
                ,datetime datetime)
                CHARACTER SET utf8 COLLATE utf8_general_ci;
            ''')
conn.commit()
print("test Table made.")



# cur.execute('select * from Book_Main')
# for row in cur.fetchall():
#    print(row) 
