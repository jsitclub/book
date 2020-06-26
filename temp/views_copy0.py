#mysqlclient의 모듈을 그대로 이용하여 연결

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import MySQLdb			# mysqlclient
import time

#속도측정 테스트
def q100k(cur):
    t = time.time()
    for _ in range(10000):
        cur.execute("SELECT 1,2,3,4,5,6")
        res = cur.fetchall()
        assert len(res) == 1
        assert res[0] == (1, 2, 3, 4, 5, 6)
    return time.time() - t

def index(request):
       
    conn= MySQLdb.connect(
        user='root',
        passwd='rootpswd',
        host='localhost',
        db='sql_test',
    )

    cur=conn.cursor()

    return HttpResponse(q100k(cur))
    
#    return HttpResponse("hello")