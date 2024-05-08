import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers={"User-Agent" :"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
type_tr=soup.find("tr",{"class":"type1"})


print("th: ",type_tr.th) #맨 첫 번째꺼
print("find_next_slibling: ",type_tr.th.find_next_sibling("th")) #현재 th에서 다음 th를 찾아줌.
print("next: ",type_tr.th.next) #th태그 다음 단락 <next_sibling은 글자를 나오게 하고 그냥 text는 th포함해서 순서대로 나옴>
print("next2: ",type_tr.th.next.next)
print("next3: ",type_tr.th.next.next.next)

