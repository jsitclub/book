from bs4 import BeautifulSoup as bs 
import requests

result=[]
TargetURL='https://book.naver.com/'

#대분류 갖고오기
def GetCategory():
    ## Get html of list area
    url =TargetURL    
    html = requests.get(url)
    soup = bs(html.text,'html.parser')
    cateList = soup.find('div',{"class":'category'}).findAll('a')
    
    #result = [t.text for t in cateList]     # another method
    
    for temp in cateList:
        tempcate=temp['cate']
        if len(tempcate)==3:
            result.append(tempcate+":"+temp.text)
            GetSubCategory(tempcate)
        

#중,소분류 갖고오기
def GetSubCategory(category):
    ## Get html of list area
    url=TargetURL+'category/index.nhn?cate_code='+category    
    html = requests.get(url)
    soup = bs(html.text,'html.parser')
    cateList = soup.find('div',{"id":'family_category'}).findAll('a')
    
    for temp in cateList:
        if '=' in temp['href']:
            result.append(temp['href'].split('=')[1]+":"+temp.text)
    
    

GetCategory()

for s in result:
    # todo : insert DB
    print(s)
