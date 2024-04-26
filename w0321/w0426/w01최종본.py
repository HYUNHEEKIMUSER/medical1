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
url = 'https://flight.naver.com'
browser = webdriver.Chrome()
browser.maximize_window() #창 최대화
browser.get(url)

# class:By.CLASS_NAME / id: By.ID / name: By.NAME / xpath: By.XPATH
# selenium->find_element: 하나/ find_elements: 여러 개
# requests->find, find_all
# XPATH: '//(처음태그)[text()="태그 안에 있는 글자"]' or ex) b[contains(text(),"국")] , b[@class="send"], b[@id="send"]
time.sleep(1)
# 출발지 선택
# elem = browser.find_element(By.XPATH,'//b[text()="ICN"]').click()
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(2)
elem.click()

time.sleep(1)
# 국내 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(2)
elem.click()

time.sleep(1)
# 김포국제공항
elem= browser.find_element(By.XPATH,'//i[text()="김포국제공항"]')  
# elem=browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
time.sleep(2)
elem.click()

time.sleep(1)
# 도착지 선택
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(2)
elem.click()

time.sleep(1)
# 국내 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(3)
elem.click()

time.sleep(1)
# 제주공항 선택
elem = browser.find_element(By.XPATH,'//i[text()="제주국제공항"]')
time.sleep(3)
elem.click()

time.sleep(1)
# 가는 날 선택
elem  =browser.find_element(By.XPATH,'//button[text()="가는 날"]')
time.sleep(3)
elem.click()

time.sleep(1)
# 14일을 선택할 때 14일은 여러 개여서 elements로 해야됨
# 가는 날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="14"]')
time.sleep(3)
# 5월 14일이니까 5월[1]
elem[1].click()

time.sleep(1)
# 오는 날 선택
elem  =browser.find_element(By.XPATH,'//button[text()="오는 날"]')
time.sleep(3)
elem.click()

time.sleep(1)
# 오는 날짜 선택
elem = browser.find_elements(By.XPATH,'//b[text()="15"]')
time.sleep(3)
# 5월 15일이니까 5월[1]
elem[1].click()

time.sleep(1)
# 인원부분 선택 
elem  = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[3]') #태그에 직접적인 단어 없어서
time.sleep(3)
elem.click()

time.sleep(1)
# 인원추가 선택
elem = browser.find_element(By.XPATH,'//button[@class="searchBox_outer__9n6IB"]')
time.sleep(3)
elem.click()

time.sleep(1)
# 항공권검색 선택
elem = browser.find_element(By.XPATH,'//span[text()="항공권 검색"]')
time.sleep(3)
elem.click()
elem.click() #한번 더 클릭해줘야 창이 닫혀서 두번 클릭

# 화면 대기 시간
time.sleep(7)

# 화면 대기 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 최대 30초까지 대기
# elem = WebDriverWait(browser,30).until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="domestic_Flight__sK0eA"]')))
# print(elem)
# print(elem[0].text)

# 화면 스크롤 내리기
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
    
input("enter키 입력 시 종료 >> ")

# 화면닫기
browser.quit()

time.sleep(100)