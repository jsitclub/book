from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

#국내소설,해외소설
result=["001:국내소설","002:해외소설"]

urlMain='http://www.yes24.com/24/Category/Display/'
removeStr='24/Category/Display/'            #링크에서 코드만 추출할때 사용


def GetCategory(category):
    ## Get html of list area
    url=urlMain+category
    html = requests.get(url)
    soup = bs(html.text,'html.parser')
    cateLiArea = soup.find('div',{"class":'cateLiArea'})


    ## Get all of <a>
    LstDepth23 = cateLiArea.findAll('a')
    for temp in LstDepth23:
        result.append(str(temp['href'][len(removeStr)+1:]).strip() + ":" + str(temp.text).strip())
        # todo : insert DB

GetCategory('001')
GetCategory('002')
print(result)
