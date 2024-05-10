import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By  #요소선택할 때
from selenium.webdriver.common.keys import Keys #키워드 입력할 때
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

url = "http://www.naver.com"

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화
browser.get(url)

# 요소선택, 문자입력, ENTER 키입력, 클릭, 스크롤이동, 마우스 이동
elem = browser.find_element(By.ID,"query")
elem.send_keys("시가총액")
elem.send_keys(Keys.ENTER)  #inter박스에서 enter키 입력

# 시가총액 더보기 클릭
elem = browser.find_element(By.XPATH,"/html/body/div[3]/div[2]/div/div[1]/section[1]/div/div[2]/div[2]/div[1]/div[2]/a")
elem.click()
time.sleep(100)