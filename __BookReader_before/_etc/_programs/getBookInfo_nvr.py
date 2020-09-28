from bs4 import BeautifulSoup as bs 
import requests


result=[]
TargetURL="https://book.naver.com/search/search.nhn?sm=sta_hty.book&sug=&where=nexearch&query="

# 9788960515987


def CreateBookData(isbnNo):
    
    # isbn 검색결과
    url =TargetURL + isbnNo
    html = requests.get(url)
    soup = bs(html.text,'html.parser')
    
    title = soup.find('ul',{"class":'basic'}).find('dt').find('a').text
    newurl = soup.find('ul',{"class":'basic'}).find('dt').find('a')['href']
    
    # 상세 페이지내용
    html = requests.get(newurl)
    soup = bs(html.text,'html.parser')
    
    imgurl = soup.find('div',{"class":'thumb_type'}).find('a').find('img')['src']
    
    
    #기타정보(page,date)
    data=soup.find('div',{"class":'book_info_inner'}).findAll("a")
    author=""    
    translator=""
    publisher=""
    
    for content in data:
        if "author" in str(content):
            author+=content.text+","            
        elif "publisher" in str(content):
            publisher=content.text
        elif "translator" in str(content):
            translator+=content.text+","  

    #경우에 따라 줄수가 바뀌므로 1~4번째줄에서 출간일, 페이지 갖고오기
    data = soup.find('div',{'class':'book_info_inner'}).findAll('div')
    publishDate=""
    page=""
    
    for i in range(len(data)):
        if "저자" in  data[i].text:
            #출간일
            publishDate=data[i].text.split("|")[-1]
        elif "페이지" in  data[i].text:
            #페이지
            page=data[i].text.split("|")[0].split()[1]
    
    
    
     
    #분류정보(category)
    data=soup.find('ul',{"class":'history'}).findAll("a")
    
    s=set()
    for a in data:
        s.add(a['href'].split('code=')[1])
    
    s=sorted(s)

    for i in range(len(s)-1):
        if s[i] not in s[i+1]:
            print(s[i])

    print(s[-1])
              
    
    print("이미지 : ",imgurl)
    print("제목 : ",title)
    print("저자 : ",author)
    print("출판사 : ",publisher)
    print("번역 : ",translator)
    print("page:",page)
    print("date:",publishDate)

    

    #result = [t.text for t in cateList]     # another method



#9791160504439
#9788960515987
#9788931414370
#9788970127248
#9791197016806
#9791196977498
CreateBookData("9788960515987")






