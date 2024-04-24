import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

url = "http://www.naver.com"
# 크롬브라우저 열기
browser = webdriver.Chrome()
# 네이버페이지 이동
browser.get(url)
time.sleep(3)
# 로그인버튼 선택
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
# 로그인버튼 클릭
elem.click()
time.sleep(random.randint(2,5))
# 아이디 입력창 검색
elem = browser.find_element(By.ID,"id")
# 아이디 글자 입력 
elem.send_keys("aaa")
time.sleep(random.randint(2,5))
elem = browser.find_element(By.ID,'pw')
elem.send_keys("1111")
time.sleep(random.randint(2,5))
# 로그인 버튼 클릭
elem = browser.find_element(By.CLASS_NAME,'btn_login')
time.sleep(random.randint(2,5))
elem.click()

# 완료
time.sleep(10)