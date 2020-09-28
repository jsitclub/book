
## MySQL에 연결하는 class를 만들어 공통으로 사용하려고.

##진행중... 미완료

#mysqlclient를 설치후 사용

import MySQLdb

class DBConn: 
    
    def __init__(self):
        return __connect()
        
    def __connect(self):
        conn= MySQLdb.connect(
            user='root',
            passwd='',
            host='localhost',
            db='test',
            charset='utf8',
        )
        return conn
    

conn=DBConn()
cur=conn.cursor()
cur.execute("select 'dd'")