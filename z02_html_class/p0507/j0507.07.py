import oracledb
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
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
url = "https://search.daum.net/search?w=tot&q=2019%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
res = requests.get(url,headers=headers)
res.raise_for_status()

soup=BeautifulSoup(res.text,"lxml")
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)

time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()="2019"]')
elem.click()
time.sleep(2)

time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()=" 극한직업 "]')
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//strong[@class="tit-g clamp-g"]')
title = soup.find("strong",{"class":"tit-g clamp-g"})
score = soup.find("span",{"class":"gem-star-point"})
score1=score.find("span",{"class":"ico-pmp"}).nextSibling.strip()
people = soup.find("dd",{"xpath":"//*[@id='em1Coll']/div/c-container/c-card/div/c-doc-content/div/div[2]/c-list-grid-desc/dl/dd[6]"})
print("제목 : ",title)
print("관객수 : ",score1)
print("평점 : ",people)

browser.back()

time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()="2020"]')
elem.click()
time.sleep(2)

time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()=" 남산의 부장들 "]')
elem.click()
time.sleep(2)

title = soup.find("strong",{"class":"tit-g clamp-g"})
score = soup.find("span",{"class":"ico-pmp"}).nextSibling
people = soup.find("dd",{"xpath":"//*[@id='em1Coll']/div/c-container/c-card/div/c-doc-content/div/div[2]/c-list-grid-desc/dl/dd[6]"})
print("제목 : ",title)
print("관객수 : ",score)
print("평점 : ",people)

browser.back()

time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()="2021"]')
elem.click()
time.sleep(2)

time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()=" 모가디슈 "]')
elem.click()
time.sleep(2)


title = soup.find("strong",{"class":"tit-g clamp-g"})
score = soup.find("span",{"class":"ico-pmp"}).nextSibling
people = soup.find("dd",{"xpath":"//*[@id='em1Coll']/div/c-container/c-card/div/c-doc-content/div/div[2]/c-list-grid-desc/dl/dd[6]"})
print("제목 : ",title)
print("관객수 : ",score)
print("평점 : ",people)

browser.back()


time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()="2022"]')
elem.click()
time.sleep(2)

time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()=" 범죄도시2 "]')
elem.click()
time.sleep(2)

title = soup.find("strong",{"class":"tit-g clamp-g"})
score = soup.find("span",{"class":"ico-pmp"}).nextSibling
people = soup.find("dd",{"xpath":"//*[@id='em1Coll']/div/c-container/c-card/div/c-doc-content/div/div[2]/c-list-grid-desc/dl/dd[6]"})
print("제목 : ",title)
print("관객수 : ",score)
print("평점 : ",people)

browser.back()

time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()="2023"]')
elem.click()
time.sleep(2)

time.sleep(2)
elem = browser.find_element(By.XPATH,'//a[text()=" 서울의 봄 "]')
elem.click()
time.sleep(2)

title = soup.find("strong",{"class":"tit-g clamp-g"})
score = soup.find("span",{"class":"ico-pmp"}).nextSibling
people = soup.find("dd",{"xpath":"//*[@id='em1Coll']/div/c-container/c-card/div/c-doc-content/div/div[2]/c-list-grid-desc/dl/dd[6]"})
print("제목 : ",title)
print("관객수 : ",score)
print("평점 : ",people)

browser.back()