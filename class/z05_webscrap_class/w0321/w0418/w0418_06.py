import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

t_table= soup.find("table",{"class":"type_5"})
trs = t_table.find_all("tr")
td = trs[2]
print(td)

tds = td.find_all("td")
for td in tds:
    print(td.text.strip()) #글자만 나오게 하는 것
    
