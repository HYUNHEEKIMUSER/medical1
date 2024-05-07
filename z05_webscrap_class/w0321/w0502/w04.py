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

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://www.melon.com/chart/index.htm"
browser.get(url)
time.sleep(2)
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
# selenium

# elem = browser.find_element(By.XPATH,"")


# request
tbody = soup.find("tbody")
trs = tbody.find_all("tr")

# 테이블명 멜론
# 순번 시퀀스번호 melon_seq

for i in range(24):
    first = trs[i]
    # 순위 rank
    first_rank = trs[i].find("span",{"class":"rank"})
    print("1. 순위: "+first_rank.text, sep='\t')
    # 변동순위 v_rank
    first_v_rank = trs[i].find("span",{"class":"rank_wrap"})["title"]
    a = trs[i].find("span",{"title":"순위 동일"})
    if first_v_rank == "순위 동일":
        print("2. 순위는 동일함: ",0)
    else:
        print("2. 변동순위: "+first_v_rank.strip(), sep='\t')
    # 이미지 img
    first_img = trs[i].find("img",{"onerror":"WEBPOCIMG.defaultAlbumImg(this);"})["src"]
    print("3. 이미지 : "+first_img.strip(), sep='\t')
    # 제목 title
    first_title = trs[i].find("div",{"class":"ellipsis rank01"})
    print("4. 제목 : "+first_title.text.strip())
    # 가수 singer
    first_singer = trs[i].find("div",{"class":"ellipsis rank02"})
    print("5. 가수 : "+first_singer.text.strip())
    # 좋아요수 likeNum
    
    r_likeNum = trs[i].find("span",{"class":"cnt"}).nextSibling.strip()
    likeNum = r_likeNum.find("span",{"class":"none"}).nextSibling.strip()
    print("6. 좋아요수 : ",likeNum)
    print('-'*80)
  
  
    sql =f"insert into melon values (\
        melon_seq.nextval,{first_rank},{first_v_rank},'{first_img}',\
        '{first_title}','{first_singer}',{likeNum})"
cursor.execute(sql)
cursor.execute('commit')
cursor.close()
conn.close()    
    
print("-"*30)

# cursor.execute('commit')
# cursor.close()
# conn.close()