import requests
from bs4 import BeautifulSoup

url = 'https://browse.auction.co.kr/list?category=22160000'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

all = soup.find("div",{"id":"section--inner_content_body_container"})
second = all.find("div",{"class":"section--module_wrap"})

title = soup.find("div",{"class":"area--itemcard_title"})

title2 = title.find("span",{"class":"text--title"})
print(title2.text)

price1 = soup.find("div",{"class":"area--itemcard_price"})
price = price1.find("span",{"class":"box__price-coupon"})
print(price.text)

image = title.find("div",{"section":"section--itemcard_img"})
print(image)

# -------------------------------------선생님
a = soup.find("div",{"module-design-id":"17"})
print(a)
b = soup.find("div",{"data-criteo-item-no":"E203326582"})
print(b)

