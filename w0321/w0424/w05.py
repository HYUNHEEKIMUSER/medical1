import requests
from bs4 import BeautifulSoup
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers= {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

url = "https://www.daum.net/"
browser = webdriver.Chrome()
browser.get(url)
time.sleep(3)
elem = browser.find_element(By.CLASS_NAME,"btn_login")
elem.click()
time.sleep(3)


# # ------------자동로그인--------------------------

# input_js = 'document.getElementById("id").value="{id}";\
#             document.getElementById("pw").value="{pw}";\
#             '.format(id='deargirl419',pw='비번')
# time.sleep(3)
# browser.execute_script(input_js)

# # ----------- 자동로그인-----------------------------

# 로그인 버튼
# elem = browser.find_element(By.XPATH,"")
elem=browser.find_element(By.ID,"loginId--1")
elem.send_keys("deargirl419")
time.sleep(random.randint(2,5))
elem = browser.find_element(By.ID,"password--2")
elem.send_keys("1111")
time.sleep(3)
elem =browser.find_element(By.CLASS_NAME,"btn_g highlight submit")
time.sleep(3)
elem.click()
time.sleep(10)


