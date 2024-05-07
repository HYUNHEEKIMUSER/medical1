import requests
from bs4 import BeautifulSoup

url="https://www.gmarket.co.kr/n/best"
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

first = soup.find("p",{"class":"no1"})
price = soup.find("div",{"class":"item_price"})
print(first.text)
print(price.text)

onetofive = soup.find("div",{"class":"best-list"})
li01 = onetofive.find('li')
print(li01.p.text)
print("제목: ",li01.find("a",{"class":"itemname"}).text)
print("가격: ",li01.find("div",{"class":"s-price"}).strong.span.text)

lis = onetofive.find_all("li")
print("갯수: ",len(lis))
for li in lis[0:4]:
    print("순위: ",li.p.text)
    print("제목: ",li.find("a",{"class":"itemname"}).text)
    print("가격: ",li.find("div",{"class":"s-price"}).strong.span.text)
    print("-"*50)