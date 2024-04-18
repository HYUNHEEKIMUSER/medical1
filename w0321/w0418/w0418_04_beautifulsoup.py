import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36r"}
res = requests.get(url,headers=headers)
res.raise_for_status()



# print(res.text)
soup = BeautifulSoup(res.text,"lxml") # text를 html파싱(변경) (B)첫 글자 대문자: 클래스

# print(type(soup))
# with open("stock2.html",'w',encoding='utf8') as f:
#     f.write(soup.prettify())

# print(soup.prettify) #html 소스를 정렬해서 출력해줌

print("<title>: ",soup.title) #태그를 입력하면 그 태그를 찾아줌
print("<title> text: ",soup.title.text) #태그의 글자를 가져옴  
print("<title> text: ",soup.title.get_text()) #태그의 글자를 가져옴->(): 함수임 id는 유일 / class= 여러 개
print("<a> 태그: ",soup.a)
print("<a> 태그글자: ",soup.a.text)
print("<a> 속성전체: ",soup.a.attrs) # 태그의 속상값을 모두 가져옴

print("<a>[1개 속성]: ",soup.a["href"]) #태그의 1개 속성 가져옴.