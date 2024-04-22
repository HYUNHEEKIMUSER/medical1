import requests
from bs4 import BeautifulSoup

url = 'https://browse.auction.co.kr/list?category=22160000&k=31&p=1'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# with open("auction.html",'w',encoding='utf8') as f: f.write(soup.prettify())

# divs = section.find_all("div",{"class":"section--module_wrap"})
# print(len(divs))
section = soup.find("div",{"id":"section--inner_content_body_container"})
# print(section.find("div",{"class":"section--itemcard"}))
# itemcard = section.find("div",{"class":"section--itemcard_info"})
# print("제목: ",itemcard.find("span",{"class":"text--title"}).text)
# # replace함수,를 제거 int 타입변경 '{0:,}'.format(num)
# print("금액: ",int((itemcard.find("strong",{"class":"text__price-seller"}).text).replace(",","")))
# price =int((itemcard.find("strong",{"class":"text__price-seller"}).text).replace(",",""))
# print("금액: ",'{0:,}'.format(price))
# print("-"*40)
# print("후기평점: ",section.find("div",{"class":"section--itemcard_info_score"}))

# ----------------------------------------------
itemcard = section.find("div",{"class":"section--itemcard_info"})
itemcards = section.find_all("div",{"class":"secton--itemcard_info"})
print("갯수: ",len(itemcards))

for i,itemcard in enumerate(itemcards[0:5]):
    print("[",i+1,"번째]")
    print("제목: ",itemcards[2].find("span",{"class":"text--title"}).text)
    price =int((itemcard.find("strong",{"class":"text__price-seller"}).text).replace(",",""))
    print("금액: ",'{0:,}'.format(price))
    print("후기평점: ",itemcard.find("ul",{"class":"list--score"}))
    
if itemcard.find("ul",{"class":"list--score"}).text == "":
    print("후기평점: ")
else: 
    list_score=  itemcard.find("ul",{"class":"list--score"})
    # print("정수형 변경 전 구매건수: ",list_score.find("span",{"class":"text--buycnt"}).text)
    print("후기평점: ",list_score.find("span",{"class":"for-ally"}).text)
    try:
        buycnt = int(list_score.find("span",{"class":"text--buycnt"}).text[4:])
        if buycnt>2: 
            print("구매건수: ",buycnt)
        else : 
            print("구매건수가 적어 생략합니다.")
    except:
        print("구매건수가 없습니다.")
print("-"*40)