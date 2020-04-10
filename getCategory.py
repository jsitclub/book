from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

#국내소설,해외소설
wfs=['001','002']
result=["001:국내소설","002:해외소설"]
urlYes='http://www.yes24.com/24/Category/Display/'
removeStr='24/Category/Display/'


def GetCategory(category):
    ## Get html of list area
    url=urlYes+category
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
