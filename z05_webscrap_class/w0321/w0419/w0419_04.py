import requests
from bs4 import BeautifulSoup

url="https://www.coupang.com/"
url="https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/123.0.0.0", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")

# second = soup.find("li",{"class":"search-product"})
# price = second.find("div",{"class":"price-area"})
# print(price.text.strip())


total = soup.find("ul", {"id":"productList"})
all = total.find_all("div")



# for div in all[0:10]:
    # print("열개: ",total.find("span",{"class":"rating-total-count"}).text)
    
# again = total.find("li",{"id":"151497626"})
# print(again)

# --------------------------------------
print("선생님: ",soup.find("ul",{"class":"search-product-list"}).find_all("li"))
ul_search=soup.find("ul",{"class":"search-product-list"})
# 모든상품 검색
lis = ul_search.find_all("li")
# print("리스트 갯수: ",len(lis))
print(lis[0])
print("-"*40)
print(lis[1])

for i,li in enumerate(lis[0:10]):
    # 광고상품 제외
    if "search-product__ad-bagde" in li["class"]:
        continue
    
    #평점이 5.0이상 - 문자와 숫자 비교에러
    if float(li.find("em",{"class":"rating"}).text) < 5.0:
        continue
     # 평가인원 수 200명 이상인 경우 출력
    if int(li.find("span",{"class":"rating-total-count"}).text[1:-1])< 200:
        continue
    
    print("[",i+1,"번째 상품]")
    print("li class: ",li["class"])
    # 왼쪽 오른쪽 공백제거
    print("제목: ",li.find("div",{"class":"name"}).text.strip())
    print("가격: ",li.find("strong",{"class":"price-value"}).text)
    print("평점: ",li.find("em",{"class":"rating"}).text)
    # 평가인원 수 200명 이상인 경우 출력
    print("평가인원수: ",li.find("span",{"class":"rating-total-count"}).text[1:-1])
    print("-"*30)

