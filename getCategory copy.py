from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

#국내소설,해외소설
wfs=['001001001']
result=["001001001:가정 살림"]

# 아래주소로 가서 검색할것!!!
# http://www.yes24.com/24/Category/Display/001001004004008002
# 만들어놓은 코드는 depth2까지만 검색!!

url='http://www.yes24.com/24/category/bestseller?CategoryNumber='+wfs[0]+'&sumgb=06'
html = requests.get(url)
soup = bs(html.text,'html.parser')

#### get all of menu
lstcate = soup.select("#category"+ wfs[0]+" > ul")
print(1,lstcate)
for temp in lstcate:
    tempid=temp['id'][8:]
    #print(tempid)
    wfs.append(tempid)
    result.append(tempid+":"+temp.find('a').text)
    #print(temp['id'][8:])
    #print(temp.find('a'))
    # print(temp)
wfs.pop(0)

print(wfs)
print(result)
