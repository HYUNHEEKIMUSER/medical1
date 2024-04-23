import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
url = "http://www.naver.com"
# 브라우저 페이지를 열기
browser.get(url)

# selenium은 자동화 프로그램

# 네이버 로그인 버튼을 클릭
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
elem.click()
time.sleep(3)
browser.back() #브라우저 뒤로가기, browser.forward() 앞으로가기
browser.refresh() #F5 새로고침




# 네이버 검색 부분에 검색어를 입력
elem = browser.find_element(By.ID,"query") #id가 query인
elem # 선택되어 있는 elem 요소를 보여줌
elem.click()
elem.send_keys("주식")



# 100초 대기
time.sleep(100)



# soup = BeautifulSoup(browser.page_source,"lxml")