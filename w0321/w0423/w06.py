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
tb = soup.find("tbody")
trs = tb.find_all("tr")
tds = trs[1].find_all("td")

print("tds 개수:",len(tds))
print("인구수 :", tds[2].text)





# print("서울특별시 인구: ",)
# print("인천직할시 인구: ",)
# print("경기도 인구: ",)
# print("합계 인구: ",)



