import requests
from bs4 import BeautifulSoup
url = "https://browse.auction.co.kr/list?category=22160000&k=31&p=1"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()
# 데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")

first = soup.find("div",{"id":"section--inner_content_body_container"})
second = first.find("div",{"module-design-id":"17"})
third = second.find("div",{"data-criteo-item-no":"E203326582"})
fourth= third.find("div",{"class":"area--itemcard_title"})
print("제목: ",fourth.text)
fifth = third.find("strong",{"class":"text__price-seller"})
print("가격: ",fifth.text)
sixth = third.find("span",{"class":"text--reviewcnt"})
print("별점:",sixth.text)
print("별점:",sixth.text[3])
