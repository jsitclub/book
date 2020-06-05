from bs4 import BeautifulSoup as bs 
import requests

result=[]
TargetURL="https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query="

# 9788960515987


def CreateBookData(isbnNo):
    
    # isbn 번호 검증
    # a=clsISBN("9788954650700")
    # print(a.checkISBN("9788954650700"))

    
    # isbn 검색결과
    url =TargetURL + isbnNo
    html = requests.get(url)
    soup = bs(html.text,'html.parser')
    
    newurl = soup.find('ul',{"class":'basic'}).find('dt').find('a')['href']
    #print(newurl)

    title = soup.find('ul',{"class":'basic'}).find('dt').find('a').text
    print("제목 : ",title)

    #db에 생성 id,제목, isbn 
    

    # 상세 페이지내용
    html = requests.get(newurl)
    soup = bs(html.text,'html.parser')
    
    img = soup.find('div',{"class":'thumb_type'}).find('a').find('img')['src']
    print("이미지 : ",img)

    author=soup.find('div',{"class":'book_info_inner'}).findAll("a")
    for content in author:
        if "author" in str(content):
            print('저자 : ',content.text)
        elif "publisher" in str(content):
            print('출판사 : ',content.text)
        elif "translator" in str(content):
            print('번역 : ',content.text)


    #result = [t.text for t in cateList]     # another method



#9791160504439
#9788960515987
#9788931414370
CreateBookData("9788970127248")
