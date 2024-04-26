import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

# 브라우저 열기
url = 'https://flight.naver.com/flights/domestic/GMP-CJU-20240514/CJU-GMP-20240515?adult=2&fareType=YC'
browser = webdriver.Chrome()
browser.maximize_window() #창 최대화
browser.get(url)

# 페이지 로딩 대기시간
elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))
print(elem)
print(elem[0].text)


#  화면 스크롤 내리기
# 현재 스크롤 높이 검색
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이: ",prev_height)

# prev_height만큼 내리기
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

    # 재조정된 스크롤 높이
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break # 같으면 중단

    prev_height = curr_height
    print("현재높이 : ",curr_height)
    
soup = BeautifulSoup(browser.page_source,'lxml')

flights = soup.find_all("div",{"class":"domestic_Flight__sK0eA"})
print("항공권 갯수: ", len(flights))
print(flights[0])

# soup에서 웹스크래핑을 진행함.







with open("flight.html",'w',encoding='utf8') as f: f.write(soup.prettify())