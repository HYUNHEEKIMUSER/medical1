import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
url = "https://jumin.mois.go.kr/ageStatMonth.do"
browser.get(url)
time.sleep(3)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

res = requests.get(url,headers=headers)
res.raise_for_status()
soup=BeautifulSoup(res.text,'lxml')

# 서울특별시 ,인천, 경기도 3개의 인구를 웹스크래핑
# replace(",","")
# split()
tb = soup.find("table",{"id":"contextTable"})
tbody = tb.find("tbody")
# print(tbody)
trs = tbody.find_all("tr")
tds = trs[1].find("td",{"title":"2024년 03월 / 계"})
seoul =tds.text
print("서울특별시 인구수: ",tds.text)
tds2 = trs[4].find("td",{"title":"2024년 03월 / 계"})
incheon = tds2.text
print("인천직할시 인구: ",tds2.text)
tds3 = trs[9].find("td",{"title":"2024년 03월 / 계"})
gyounggi = tds3.text
print("경기도 인구: ",tds3.text)

total=int(seoul.replace(",",""))+int(incheon.replace(",",""))+int(gyounggi.replace(",",""))

print("합계 인구: ",format(total,","))



