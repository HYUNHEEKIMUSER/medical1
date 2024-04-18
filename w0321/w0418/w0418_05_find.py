import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers={"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
print(soup)

#태그로 찾는 방법- title, get_text(), text, a.attrs, a["href"]
#find: 태그정보 찾기 함수, 클래스로 찾는 방법 / attrs = 속성값
print(soup.find(attrs={"class":"box_type_l"}))

print(soup.find("tr",attrs={"class":"type1"})) #find(하나만 찾을 때), find_all, class
type_tr = soup.find("tr",{'class':'type1'})
print("th: ",type_tr.th) #첫 번째 만나는 th 태그를 찾아줌 (처음에 만난)
print(type_tr.find_all("th")) #th 다 찾고 싶을 때, 리스트 배열로 넘어옴
ths = type_tr.find_all("th")
for th in ths:
     print("제목: ",th.text)