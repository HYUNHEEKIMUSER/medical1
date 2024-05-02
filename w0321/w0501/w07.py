import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36","Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화


url = 'https://www.yeogi.com/domestic-accommodations?searchType=KEYWORD&keyword=%ED%98%B8%ED%85%94&checkIn=2024-06-05&checkOut=2024-06-06&personal=2&freeForm=true&page=1'
# conn = oracledb.connect(user = "ora_user",password="1111",dsn = "localhost:1521/xe")
# cursor = conn.cursor()
# sql =""
# cursor.close()
# conn.close()

browser.get(url)
soup = BeautifulSoup(browser.page_source,'lxml')

title = soup.find_all('a',{"class":"gc-thumbnail-type-seller-card css-wels0m"})
for i in range(5):
    hotel = title[i+1].find("h3",{"class":"gc-thumbnail-type-seller-card-title css-1asqkxl"})
    print("제목: ",hotel.text)
# 지역
    region = title[i+1].find("span",{"class":"css-1rzfout"})
    print("지역: ",region.text)
# 평점
    score = title[i+1].find("div",{"class":"css-wtzmcu"})
    print("평점: ",score.text)
# 평가수
    comments = title[i+1].find("span",{"class":"css-oj6onp"})
    print("평가수: ",comments.text)
# 이미지링크
    picture = title[i+1].find("img",{"class":"thumbnail-image desktop:hover:bg-backgroundOverlayDarkInactive"})["src"]
    # print("이미지: ",picture)
    try:
        img = hotel.find("img")["src"]
        print("이미지 링크", img)
    except:
        print("이미지없음")
# 가격
    price = title[i+1].find("div",{"class":"css-yeouz0"})
    if price == "":
        print("6. 가격 없음")
    else: 
        print("가격: ",price.text)  