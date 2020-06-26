from bs4 import BeautifulSoup as bs 
import requests


TargetURL='https://book.naver.com/'

#대분류 갖고오기
def GetCategory():
    ## Get html of list area
    url =TargetURL    
    html = requests.get(url)
    soup = bs(html.text,'html.parser')
    cateList = soup.find('div',{"class":'category'}).findAll('a')
    
    tempDict = {t['cate']:t.text for t in cateList}     # another method
    #print(tempDict)
    result=dict(tempDict)
    
    for key in tempDict:
        if len(key)==3:
            result.update(GetSubCategory(key))
    
    return result       
    
    
#중,소분류 갖고오기
def GetSubCategory(category):
    
    result={}
    
    ## Get html of list area
    url=TargetURL+'category/index.nhn?cate_code='+category    
    html = requests.get(url)
    soup = bs(html.text,'html.parser')
    cateList = soup.find('div',{"id":'family_category'}).findAll('a')
    
    for temp in cateList:
        if '=' in temp['href']:
            result[temp['href'].split('=')[1]]=temp.text

    return result
    
            
################################     
if __name__=='__main__':
    GetCategory()
    
