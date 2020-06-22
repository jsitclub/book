from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://book.naver.com/bookdb/book_detail.nhn?bid=16362423')
#pprint(html.text)

soup = bs(html.text,'html.parser')
data1 = soup.find('div',{'class':'book_info_inner'})
#print(data1)

data2 = data1.findAll('div')
print(data2[3].text)