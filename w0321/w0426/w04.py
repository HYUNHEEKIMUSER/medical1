import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 스크롤 내린 후 제일 마지막 제목 출력 (냥줍천사)
url = "https://watcha.com/browse/webtoon"
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
print(soup.prettify())
with open("webtoon2.html",'w',encoding='utf8') as f:
    f.write(soup.prettify())

# 브라우저 열기
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)


# 스크롤 내리기
# 1.현재 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이: ",prev_height)



# 2.현재 높이에서 스크롤 내리기
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    
    # 재조정된 스크롤 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height =curr_height
    print("현재높이: ",curr_height)
    
total = soup.find("div",{"class":"custom-1ddjhv e1n12t0f0"})
total_section = soup.find_all("section",{"class":"custom-11ytuur e1134x5i3"})

print(len(total_section))
# last_div_ul = last[1].find("ul",{"class":"evjjsye0 custom-plh92q-Row e8ldpmn0"})
# lis = last_div_ul.find_all("li")
# print(lis[1].find("a",{"class":"custom-4zleql e1bnpttb2"}))
# lis = total.find_all("li")
# cat = lis[1].find("a",{"class":"custom-4zleql e1bnpttb2"})
# print(cat.text)

    
    
    
    