import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

# 야놀자 홈페이지 이동
url = "https://www.yanolja.com/?utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-327025203539&gad_source=1&gclid=EAIaIQobChMIo-mchMjuhQMVNGwPAh0_OAGuEAAYASAAEgKHcPD_BwE"
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)
browser.get(url)
time.sleep(2)
soup = BeautifulSoup(browser.page_source,'lxml')

# 검색 창에 호텔이라고 글자
time.sleep(3)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/section/header/section/a[2]/div/div')
time.sleep(3)
elem.click()
time.sleep(1)
elem.click()
time.sleep(5)

# time.sleep(10)
# elem = browser.find_element(By.CLASS_NAME,"SearchInput_input__342U2")
# time.sleep(5)
# elem.send_keys("호텔")
# time.sleep(5)
# 날짜 선택 6월 5일, 6월 6일 클릭
time.sleep(5)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[2]/div[1]/button/span/svg/path')
time.sleep(1)
elem.click()
time.sleep(1)
elem.click()
time.sleep(30)
elem = browser.find_element(By.CLASS_NAME,'CalendarDay CalendarDay_1 CalendarDay__default CalendarDay__default_2 CalendarDay__firstDayOfWeek CalendarDay__firstDayOfWeek_3')
time.sleep(1)
elem[3].click()
time.sleep(1)
elem[4].click()
time.sleep(1)
# 확인버튼 클릭 
time.sleep(1)
elem = browser.find_element(By.XPATH,'//button[text()=확인]')
time.sleep(1)
elem.click()
# 검색창 클릭 > enter키 입력
time.sleep(1)
elem = browser.find_element(By.CLASS_NAME,'SearchInput_button__tUMEN SearchInput_buttonSubmit__3D83k')
time.sleep(1)
elem.click()
time.sleep(1)
elem.click()
time.sleep(10)
# 검색 진행
time.sleep(10)
# 스크롤 이동 반복
prev_height = browser.execute_script('return document.body.scrollHeight')
print("최초 높이: ",prev_height)
while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    curr_height=browser.execute_script('return document.body.scrollHeight')
    if prev_height == curr_height:
        break
    prev_height = curr_height
    print("현재 높이: ",curr_height)
browser.quit()
# 정보장이 띄워지면 이미지 제목 평점 평가수 금액 저장
# 야놀자 테이블
# yno, img, title, grade, grade_num, price