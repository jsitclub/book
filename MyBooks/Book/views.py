from django.shortcuts import render
from django.http import HttpResponse
from .models import *

from bs4 import BeautifulSoup as bs 
import requests
from urllib.request import urlretrieve #그림파일 저장
    
##===============================

# Create your views here.
def index(request):
    return HttpResponse("hello")




def setBookInfo(request):
    result=[]
    TargetURL="https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query="
    isbnNo='9788934972464'
    
    #9791160504439
    #9788960515987
    #9788931414370
    #9788970127248
    #9791197016806
    #9788934972464
    
    
    # todo: isbn 번호 검증
    # a=clsISBN("9788954650700")
    # print(a.checkISBN("9788954650700"))
   
    #isbn으로 검색 후(결과1건예상) 상세페이지로 이동 후 상세정보 갖고오기
    # isbn 검색결과
    url =TargetURL + isbnNo
    html = requests.get(url)
    soup = bs(html.text,'html.parser')
    
    title = soup.find('ul',{"class":'basic'}).find('dt').find('a').text
    newurl = soup.find('ul',{"class":'basic'}).find('dt').find('a')['href']
    
    # 상세 페이지로 이동
    html = requests.get(newurl)
    soup = bs(html.text,'html.parser')
    
    
    #기타정보(page,date)
    data=soup.find('div',{"class":'book_info_inner'}).findAll("a")
    author=""
    publisher=""
    translator=""
    for content in data:
        if "author" in str(content):
            author+=content.text+","            
        elif "publisher" in str(content):
            publisher=content.text
        elif "translator" in str(content):
            translator+=content.text+","  

    #경우에 따라 줄수가 바뀌므로 1~4번째줄에서 출간일, 페이지 갖고오기
    data = soup.find('div',{'class':'book_info_inner'}).findAll('div')
    page=""
    publishDate=""
    for i in range(len(data)):
        if "저자" in  data[i].text:
            #출간일
            publishDate=data[i].text.split("|")[-1]
        elif "페이지" in  data[i].text:
            #페이지
            page=data[i].text.split("|")[0].split()[1]
        
    book=Book(
        title=title,
        author=author,
        translator=translator,
        isbn=isbnNo,
        page=page,
        publisher=publisher,
        publishdate=publishDate.replace(".","-"),
        )
    book.save()
    
    
    bookid = Book.objects.get(isbn=isbnNo).id
    print(bookid)
    
    #커버 다운로드 및 저장
    imgurl = soup.find('div',{"class":'thumb_type'}).find('a').find('img')['src']
    
    urlretrieve( imgurl , bookid+'.jpg') #주소, 파일경로+파일명+확장자
   
    
    
    #분류정보(category) 저장
    data=soup.find('ul',{"class":'history'}).findAll("a")
    
    s=set()
    for a in data:
        s.add(a['href'].split('code=')[1])
    
    s=sorted(s)
    for i in range(len(s)-1):
        if s[i] not in s[i+1]:
            temp=Book_Cate(bookcode=bookid,catecode=s[i])
            temp.save()
    temp=Book_Cate(bookcode=bookid,catecode=s[-1])
    temp.save()
       
    
    
    html="<html><ul>"
    html+="<li>이미지 : "+imgurl+"</li>"
    html+="<li>제목 : "+title+"</li>"
    html+="<li>저자 : "+author+"</li>"
    html+="<li>출판사 : "+publisher+"</li>"
    html+="<li>번역 : "+translator+"</li>"
    html+="<li>page: "+page+"</li>"
    html+="<li>date: "+publishDate+"</li>"
    html+="</ul></html>"
    
    
    return HttpResponse(html)
  
    

    
#===============================
#category 갖고오기

def setCategory(request):
    category=GetCategory()
    for key in category:
        cate=Category(code=key,content=category[key])
        cate.save()
    return HttpResponse("카테고리 저장 완료")


#대분류 갖고오기
TargetURL='https://book.naver.com/'

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

#===============================


