import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "https://flight.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(1)
elem= browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(1)
elem.click()

time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
# 실제구문 -1개 가져오기 -> browser.find_element(By.XPATH,//i[text()="김포국제공항"]')
# 실제구문 -여러개 가져오기(find_elements) -> browser.find_elements(By.XPATH,'//b[text()="15"]')
# 문자열과 일치할 때'//button[text()="국내"]' / 문자열이 포함되어 있을 때 '//i[contains(text(),"김포국제공항")]'
# id를 가지고 '//i[@id="_next"]'
# class를 가지고 '//i[@class="_next"]'

# 김포국제공항 검색
time.sleep(1)
elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
time.sleep(1)
elem.click()


time.sleep(1)
elem= browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(1)
elem.click()

time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()

time.sleep(1)
elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
time.sleep(1)
elem.click()

# 가는 날 부분 선택
elem = browser.find_element(By.XPATH,'//button[text()="가는 날"]').click()
time.sleep(1)

# 가는 날짜선택
elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
print("14일 갯수: ",len(elem))
time.sleep(2)
elem[1].click()

# 오는 날 부분 선택
elem = browser.find_element(By.XPATH,'//button[text()="오는 날"]')
elem.click()
time.sleep(1)

# 오는 날짜선택
elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
print("15일 갯수: ",len(elem))
time.sleep(2)
elem[1].click()

# 인원수 선택
elem= browser.find_element(By.XPATH,'//button[contains(text(),"성인")]').click()
time.sleep(1)
# 한명 추가
elem= browser.find_element(By.CLASS_NAME,'searchBox_outer__9n6IB').click()
time.sleep(1)
# 항공권 선택
# 인원수 선택창 받기 위해 두번
time.sleep(1)
browser.find_element(By.XPATH,'//span[text()="항공권 검색"]').click()
browser.find_element(By.XPATH,'//span[text()="항공권 검색"]').click()
 
# 스크롤 이동 domestic_Flight__sK0eA
time.sleep(7)

# 화면 스크롤 내리기
prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이: ",prev_height)
while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
            break
    prev_height = curr_height
    print("현재높이: ",curr_height)

soup = BeautifulSoup(browser.page_source,"lxml")
with open("flight.html","w",encoding="utf8") as f: f.write(soup.prettify())

input("enter키를 입력하면 프로그램을 종료")
browser.quit()
# time.sleep(100)


