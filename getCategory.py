from bs4 import BeautifulSoup as bs 
from pprint import pprint
import requests

html = requests.get('http://www.yes24.com/Mall/Main/Book/001?CategoryNumber=001')
# pprint(html.text)

soup = bs(html.text,'html.parser')

#### get cate2Name
cateList = soup.find('div',{'class':'cateLi cateLiTp_1'})
cate2Name=cateList.findAll('em',{'class':'txt'})

for i in range(len(cate2Name)):
    print(str(i).zfill(3),cate2Name[i].text)

#### get cate2Code


#print(fine_dust)

# f=open("data.txt","w")
# f.write(str(data1))
# f.close()

