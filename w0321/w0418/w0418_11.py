import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36r"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,'lxml')

t_top = soup.find("table",{"class":"type_5"})
trs = t_top.find_all("tr")
td1=trs[2:7]
td2=trs[9:15]


for td in td1:
   print(td.text.strip())

for td in td2:
  print(td.text.strip())