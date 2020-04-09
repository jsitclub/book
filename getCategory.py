from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

html = requests.get('http://www.yes24.com/24/category/bestseller')
# pprint(html.text)

soup = bs(html.text,'html.parser')

#### get all of menu
html_menu = soup.find('div',{'id':'bestMenu'})
#print(html_menu)

cate_all=html_menu.findAll('a')
#print(cate_all)


for data in cate_all:
#     #print(str(i).zfill(3),cate2Name[i].text)
     print(data)
